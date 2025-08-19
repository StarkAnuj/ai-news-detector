import pandas as pd
import numpy as np
import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
import requests
import zipfile
from io import BytesIO

# Download NLTK resources
print("Downloading NLTK data...")
try:
    # Download all required NLTK data
    nltk.download('punkt', quiet=True)
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('omw-1.4', quiet=True)  # Additional wordnet data
    print("✓ NLTK data downloaded successfully!")
except Exception as e:
    print(f"Warning: NLTK download issue: {e}")
    print("Continuing with training...")

# Ensure directories exist
os.makedirs('../data', exist_ok=True)
os.makedirs('../model', exist_ok=True)

def download_dataset():
    """Download fake news dataset from Kaggle (GitHub mirror)"""
    print("Downloading fake news dataset...")
    
    # URLs for the dataset files
    true_url = "https://raw.githubusercontent.com/KamalGalrani/Fake-News-Detection/master/True.csv"
    fake_url = "https://raw.githubusercontent.com/KamalGalrani/Fake-News-Detection/master/Fake.csv"
    
    try:
        # Download True.csv
        if not os.path.exists('../data/True.csv'):
            print("Downloading True.csv...")
            response = requests.get(true_url)
            response.raise_for_status()
            with open('../data/True.csv', 'wb') as f:
                f.write(response.content)
            print("True.csv downloaded successfully!")
        
        # Download Fake.csv
        if not os.path.exists('../data/Fake.csv'):
            print("Downloading Fake.csv...")
            response = requests.get(fake_url)
            response.raise_for_status()
            with open('../data/Fake.csv', 'wb') as f:
                f.write(response.content)
            print("Fake.csv downloaded successfully!")
            
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        print("Creating sample dataset instead...")
        create_sample_dataset()

def create_sample_dataset():
    """Create a sample dataset for testing if download fails"""
    print("Creating sample dataset...")
    
    # Sample real news
    real_news = [
        "The president announced new economic policies during today's press conference. The new measures are expected to boost employment rates.",
        "Scientists at MIT have developed a new technology that could revolutionize renewable energy production. The research was published in Nature journal.",
        "The stock market closed higher today after positive earnings reports from major tech companies. Investors showed confidence in the market.",
        "Local authorities have announced plans to improve public transportation in the city. The project will begin next month.",
        "A new study shows that regular exercise can significantly improve mental health. The research involved 1000 participants over two years."
    ]
    
    # Sample fake news
    fake_news = [
        "BREAKING: Aliens have landed in Area 51 and the government is hiding it from us! Secret documents revealed shocking truth!",
        "Miracle cure found! This one weird trick will make you lose 50 pounds in a week! Doctors hate this secret!",
        "SHOCKING: Celebrity spotted doing something completely normal! You won't believe what happened next!",
        "Government plans to control your mind with 5G towers! Here's how to protect yourself with aluminum foil!",
        "Scientists discover that drinking water is actually dangerous! Big pharma doesn't want you to know this!"
    ]
    
    # Create DataFrames
    true_df = pd.DataFrame({
        'title': ['Real News ' + str(i) for i in range(len(real_news))],
        'text': real_news,
        'subject': ['politics', 'science', 'business', 'local', 'health'],
        'date': ['2024-01-01'] * len(real_news)
    })
    
    fake_df = pd.DataFrame({
        'title': ['Fake News ' + str(i) for i in range(len(fake_news))],
        'text': fake_news,
        'subject': ['conspiracy', 'health', 'celebrity', 'technology', 'health'],
        'date': ['2024-01-01'] * len(fake_news)
    })
    
    # Save sample datasets
    true_df.to_csv('../data/True.csv', index=False)
    fake_df.to_csv('../data/Fake.csv', index=False)
    print("Sample dataset created successfully!")

# Function to load and combine datasets
def load_data():
    print("Loading datasets...")
    
    # Download dataset if not exists
    if not os.path.exists('../data/True.csv') or not os.path.exists('../data/Fake.csv'):
        download_dataset()
    
    try:
        true_news = pd.read_csv('../data/True.csv')
        fake_news = pd.read_csv('../data/Fake.csv')
        
        # Add labels
        true_news['label'] = 1  # 1 for real
        fake_news['label'] = 0  # 0 for fake
        
        # Combine datasets
        combined_data = pd.concat([true_news, fake_news], ignore_index=True)
        
        # Shuffle data
        combined_data = combined_data.sample(frac=1).reset_index(drop=True)
        
        print(f"Dataset loaded with {len(combined_data)} entries")
        print(f"Real news: {len(true_news)}, Fake news: {len(fake_news)}")
        return combined_data
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Text cleaning function
def clean_text(text):
    if isinstance(text, str):
        # Remove URLs
        text = re.sub(r'http\S+', '', text)
        # Remove non-alphabetic characters
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Convert to lowercase
        text = text.lower()
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    return ""

# Text preprocessing with NLTK
def preprocess_text(text):
    if not isinstance(text, str) or text == "":
        return ""
    
    # Tokenize
    tokens = nltk.word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    
    return " ".join(lemmatized)

def main():
    # Load and preprocess data
    data = load_data()
    
    if data is None:
        print("Failed to load data. Exiting...")
        return
    
    # Save combined data for future use
    data.to_csv('../data/fake_real_news.csv', index=False)
    
    print("Cleaning and preprocessing text...")
    # First basic cleaning
    data['cleaned_text'] = data['text'].apply(clean_text)
    
    # Apply NLTK preprocessing
    data['processed_text'] = data['cleaned_text'].apply(preprocess_text)
    
    # Remove rows with empty processed text
    data = data[data['processed_text'] != '']
    
    if len(data) == 0:
        print("No valid text data found after preprocessing. Exiting...")
        return
    
    # Feature extraction using TF-IDF
    print("Vectorizing text...")
    vectorizer = TfidfVectorizer(max_df=0.7, min_df=2, max_features=20000, ngram_range=(1, 2), stop_words='english')
    X = vectorizer.fit_transform(data['processed_text'])
    y = data['label']
    
    print(f"Feature matrix shape: {X.shape}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train models
    print("Training models...")
    
    # Logistic Regression
    lr_model = LogisticRegression(max_iter=1000)
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)
    lr_accuracy = accuracy_score(y_test, lr_pred)
    
    # Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_pred)
    
    # Naive Bayes
    nb_model = MultinomialNB()
    nb_model.fit(X_train, y_train)
    nb_pred = nb_model.predict(X_test)
    nb_accuracy = accuracy_score(y_test, nb_pred)
    
    # Compare models
    print(f"Logistic Regression Accuracy: {lr_accuracy:.4f}")
    print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
    print(f"Naive Bayes Accuracy: {nb_accuracy:.4f}")
    
    # Select best model (for this example, let's choose logistic regression)
    best_model = lr_model
    best_pred = lr_pred
    
    if rf_accuracy > lr_accuracy and rf_accuracy > nb_accuracy:
        best_model = rf_model
        best_pred = rf_pred
        print("Random Forest selected as best model")
    elif nb_accuracy > lr_accuracy and nb_accuracy > rf_accuracy:
        best_model = nb_model
        best_pred = nb_pred
        print("Naive Bayes selected as best model")
    else:
        print("Logistic Regression selected as best model")
    
    # Evaluate best model
    print("\nDetailed Evaluation of Best Model:")
    accuracy = accuracy_score(y_test, best_pred)
    precision = precision_score(y_test, best_pred)
    recall = recall_score(y_test, best_pred)
    cm = confusion_matrix(y_test, best_pred)
    
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print("Confusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(classification_report(y_test, best_pred))
    
    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.ylabel('Actual Label')
    plt.xlabel('Predicted Label')
    
    # Create the images directory if it doesn't exist
    images_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'app', 'static', 'images')
    os.makedirs(images_dir, exist_ok=True)
    
    plt.savefig(os.path.join(images_dir, 'confusion_matrix.png'), dpi=300, bbox_inches='tight')
    plt.close()  # Close the plot to free memory
    
    # Save model and vectorizer
    print("Saving model and vectorizer...")
    model_dir = os.path.dirname(os.path.abspath(__file__))
    joblib.dump(best_model, os.path.join(model_dir, 'model.pkl'))
    joblib.dump(vectorizer, os.path.join(model_dir, 'vectorizer.pkl'))
    
    print("Training complete! Model and vectorizer saved.")
    print(f"Model saved at: {os.path.join(model_dir, 'model.pkl')}")
    print(f"Vectorizer saved at: {os.path.join(model_dir, 'vectorizer.pkl')}")

    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'model_type': type(best_model).__name__
    }

if __name__ == "__main__":
    main()