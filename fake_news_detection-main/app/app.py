from flask import Flask, render_template, request, jsonify
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os

# Download NLTK resources if not already downloaded
print("Checking NLTK data...")
try:
    nltk.data.find('tokenizers/punkt')
    print("✓ NLTK punkt found")
except LookupError:
    print("Downloading punkt...")
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('tokenizers/punkt_tab')
    print("✓ NLTK punkt_tab found")
except LookupError:
    print("Downloading punkt_tab...")
    nltk.download('punkt_tab', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
    print("✓ NLTK stopwords found")
except LookupError:
    print("Downloading stopwords...")
    nltk.download('stopwords', quiet=True)
    
try:
    nltk.data.find('corpora/wordnet')
    print("✓ NLTK wordnet found")
except LookupError:
    print("Downloading wordnet...")
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)

app = Flask(__name__)

# Load model and vectorizer with error handling
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'model.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model', 'vectorizer.pkl')

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("Model and vectorizer loaded successfully!")
except FileNotFoundError as e:
    print(f"Model files not found: {e}")
    print("Please run the training script first to generate the model files.")
    model = None
    vectorizer = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    vectorizer = None

# Text cleaning function (same as in train_model.py)
def clean_text(text):
    if isinstance(text, str):
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        text = text.lower()
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    return ""

# Text preprocessing with NLTK (same as in train_model.py)
def preprocess_text(text):
    if not isinstance(text, str) or text == "":
        return ""
    
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    
    return " ".join(lemmatized)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Check if model is loaded
        if model is None or vectorizer is None:
            return render_template('result.html', error="Model not loaded. Please train the model first.")
        
        # Get news text from form
        news_text = request.form.get('news_text', '')
        
        if not news_text:
            return render_template('result.html', error="Please enter news text to analyze")
        
        try:
            # Clean and preprocess the text
            cleaned_text = clean_text(news_text)
            processed_text = preprocess_text(cleaned_text)
            
            if not processed_text:
                return render_template('result.html', error="Unable to process the text. Please try different text.")
            
            # Vectorize the text
            vectorized_text = vectorizer.transform([processed_text])
            
            # Predict
            prediction = model.predict(vectorized_text)[0]
            
            # Get prediction probability
            probability = model.predict_proba(vectorized_text)[0]
            confidence = probability[1] if prediction == 1 else probability[0]
            confidence = round(confidence * 100, 2)
            
            result = "Real" if prediction == 1 else "Fake"
            
            # Extract important words for explanation
            feature_names = vectorizer.get_feature_names_out()
            tfidf_values = vectorized_text.toarray()[0]
            
            # Get top 5 important words
            important_indices = tfidf_values.argsort()[-10:][::-1]
            important_words = [feature_names[i] for i in important_indices if tfidf_values[i] > 0]
            important_words = important_words[:5]  # Limit to 5 words
            
            # Basic content analysis
            word_count = len(news_text.split())
            complexity = "High" if word_count > 300 else "Medium" if word_count > 100 else "Low"
            
            return render_template('result.html', 
                                   result=result, 
                                   confidence=confidence, 
                                   news_text=news_text,
                                   important_words=important_words,
                                   word_count=word_count,
                                   complexity=complexity)
        
        except Exception as e:
            print(f"Prediction error: {e}")
            return render_template('result.html', error=f"Error during prediction: {str(e)}")

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions (useful for AJAX requests)"""
    if model is None or vectorizer is None:
        return jsonify({"error": "Model not loaded"}), 500
    
    data = request.json
    news_text = data.get('news_text', '')
    
    if not news_text:
        return jsonify({"error": "No news text provided"}), 400
    
    try:
        # Clean and preprocess
        cleaned_text = clean_text(news_text)
        processed_text = preprocess_text(cleaned_text)
        
        if not processed_text:
            return jsonify({"error": "Unable to process text"}), 400
        
        # Vectorize and predict
        vectorized_text = vectorizer.transform([processed_text])
        prediction = model.predict(vectorized_text)[0]
        
        # Get confidence
        probability = model.predict_proba(vectorized_text)[0]
        confidence = probability[1] if prediction == 1 else probability[0]
        
        result = "Real" if prediction == 1 else "Fake"
        
        return jsonify({
            "result": result,
            "confidence": round(confidence * 100, 2),
            "prediction": int(prediction)
        })
    
    except Exception as e:
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)