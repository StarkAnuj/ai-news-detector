# Fake News Detection System 🔍

A machine learning-powered web application for detecting fake news articles using Natural Language Processing (NLP) and supervised learning algorithms.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## 🌟 Features

- **🤖 Machine Learning Models**: Logistic Regression, Random Forest, Naive Bayes
- **🌐 Web Interface**: Modern, responsive web application built with Flask
- **⚡ Real-time Analysis**: Instant predictions with confidence scores
- **📊 Detailed Explanations**: Shows important words and content analysis
- **🔄 Online Dataset**: Automatically downloads training data from reliable sources
- **🎯 High Accuracy**: Achieves 92-96% accuracy on test data
- **📱 Mobile Responsive**: Works perfectly on all device sizes

## 🚀 Quick Start

### Option 1: One-Click Setup (Windows)
```bash
# Clone the repository
git clone https://github.com/AnujNandal/fake_news_detection.git
cd fake_news_detection

# Run the setup script
start.bat
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
cd model
python train_model.py
cd ..

# Start the application
cd app
python app.py
```

### Option 3: Interactive Setup
```bash
python main.py
# Select option 4 for complete setup
```

## 🌐 Web Application

Once running, access the application at: **http://localhost:5000**

### Main Interface
- **Text Input**: Large text area for news articles
- **Sample Testing**: Pre-loaded examples for quick testing
- **Model Training**: Web-based interface to retrain models
- **Real-time Results**: Instant analysis with visual feedback

### Features Available
- ✅ **Real vs Fake Classification**
- 📊 **Confidence Scores** (0-100%)
- 🔍 **Important Words Analysis**
- 📈 **Content Complexity Assessment**
- 🎨 **Visual Progress Indicators**

## 📁 Project Structure

```
fake_news_detection/
├── app/                        # Flask web application
│   ├── app.py                 # Main Flask application
│   ├── templates/             # HTML templates
│   │   ├── index.html        # Main interface
│   │   ├── result.html       # Results page
│   │   └── train.html        # Training interface
│   └── static/               # CSS, JS, images
│       ├── css/style.css     # Styling
│       ├── js/main.js        # JavaScript functions
│       └── images/           # Static images
├── model/                     # Machine learning components
│   ├── train_model.py        # Training script
│   ├── model.pkl            # Trained model (generated)
│   └── vectorizer.pkl       # TF-IDF vectorizer (generated)
├── data/                     # Dataset storage (auto-created)
├── requirements.txt          # Python dependencies
├── main.py                  # Interactive launcher
├── start.bat               # Windows quick start
├── setup_nltk.py          # NLTK data setup
└── README.md              # This file
```

## 🧠 How It Works

### 1. Text Processing Pipeline
1. **Text Cleaning**: Remove URLs, special characters, normalize case
2. **Tokenization**: Split text into individual words using NLTK
3. **Stop Word Removal**: Filter out common words (the, is, and, etc.)
4. **Lemmatization**: Convert words to their base form
5. **TF-IDF Vectorization**: Transform text into numerical features

### 2. Machine Learning Models
- **Logistic Regression**: Linear classifier with excellent interpretability
- **Random Forest**: Ensemble method for improved accuracy
- **Naive Bayes**: Fast, efficient probabilistic classifier

The system automatically selects the best-performing model based on accuracy metrics.

### 3. Dataset
- **Source**: Real fake news dataset from Kaggle
- **Size**: 40,000+ verified articles
- **Real News**: Articles from reliable, fact-checked sources
- **Fake News**: Confirmed false articles from fact-checking organizations

## 📊 Performance Metrics

- **Accuracy**: 92-96%
- **Precision**: 90-95%
- **Recall**: 90-95%
- **Training Time**: 2-5 minutes
- **Prediction Time**: < 1 second

## 🛠️ Technical Requirements

### System Requirements
- **Python**: 3.7 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 500MB for datasets and models
- **Internet**: Required for initial dataset download

### Dependencies
```
flask==2.3.3
scikit-learn==1.3.0
pandas==2.0.3
numpy==1.24.3
nltk==3.8.1
joblib==1.3.2
matplotlib==3.7.2
seaborn==0.12.2
requests==2.31.0
beautifulsoup4==4.12.2
lxml==4.9.3
openpyxl==3.1.2
```

## 🔧 API Usage

The system provides RESTful API endpoints for programmatic access:

```python
import requests

# Make prediction request
response = requests.post('http://localhost:5000/api/predict', 
                        json={'news_text': 'Your news article here'})

result = response.json()
print(f"Result: {result['result']}")
print(f"Confidence: {result['confidence']}%")
```

## 📱 Screenshots

### Main Interface
Clean, intuitive interface for entering news articles and getting predictions.

### Results Page
Detailed analysis with confidence scores, important words, and visual indicators.

### Training Interface
Web-based model training with real-time progress updates.

## 🚦 Getting Started

1. **Clone this repository**
2. **Install Python 3.7+**
3. **Run the setup script** (`start.bat` on Windows or `python main.py`)
4. **Access the web interface** at http://localhost:5000
5. **Start analyzing news articles!**

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
git clone https://github.com/AnujNandal/fake_news_detection.git
cd fake_news_detection
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is designed for educational and research purposes. While it achieves high accuracy, it should not be the sole basis for determining news authenticity. Always verify information from multiple reliable sources and use critical thinking when evaluating news content.

## 👨‍💻 Author

**Anuj Nandal**
- GitHub: [@AnujNandal](https://github.com/AnujNandal)
- Portfolio: [Your Portfolio URL]

## 🙏 Acknowledgments

- Dataset providers and the open-source community
- NLTK and scikit-learn development teams
- Flask and Bootstrap frameworks
- All contributors and users of this project

---

⭐ **Star this repository if you found it helpful!** ⭐
