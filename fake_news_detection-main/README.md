# Fake News Detection System

A machine learning-powered web application for detecting fake news articles. This project combines natural language processing (NLP) techniques with supervised learning algorithms to classify news articles as real or fake.

## Features

- **Machine Learning Model**: Uses TF-IDF vectorization and multiple algorithms (Logistic Regression, Random Forest, Naive Bayes)
- **Web Interface**: Clean, modern web interface built with Flask and Bootstrap
- **Real-time Analysis**: Instant prediction with confidence scores
- **Detailed Explanations**: Shows important words and content analysis
- **Online Dataset**: Automatically downloads training data from reliable sources
- **Model Training Interface**: Web-based model training with progress tracking

## Project Structure

```
fake-news-detector/
├── app/
│   ├── app.py              # Flask web application
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css   # Styling
│   │   ├── js/
│   │   │   └── main.js     # JavaScript functions
│   │   └── images/         # Static images
│   └── templates/
│       ├── index.html      # Main page
│       ├── result.html     # Results page
│       └── train.html      # Training page
├── model/
│   ├── train_model.py      # Model training script
│   ├── model.pkl          # Trained model (generated)
│   └── vectorizer.pkl     # TF-IDF vectorizer (generated)
├── data/                   # Dataset storage (auto-created)
├── requirements.txt        # Python dependencies
├── main.py                # Main runner script
├── run.bat                # Windows batch script
└── README.md              # This file
```

## Installation & Setup

### Option 1: Quick Start (Recommended)

1. **Clone or download** this repository
2. **Run the main script**:
   ```bash
   python main.py
   ```
3. **Select option 4** for full setup (installs dependencies, trains model, and runs app)

### Option 2: Manual Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Train the model**:
   ```bash
   cd model
   python train_model.py
   cd ..
   ```

3. **Run the web application**:
   ```bash
   cd app
   python app.py
   ```

### Option 3: Windows Batch File

Simply double-click `run.bat` on Windows systems.

## 📂 Project Structure

```
Portfolio/
├── app.py             # Main Flask application
├── main.py            # Entry point for the application
├── .replit            # Replit configuration
├── pyproject.toml     # Python project dependencies
├── static/            # Static assets
│   ├── css/           # Stylesheet files
│   ├── js/            # JavaScript files
│   └── images/        # Image assets
├── templates/         # HTML templates
│   └── index.html     # Main portfolio template
└── attached_assets/   # Uploaded assets (resumes, etc.)
```

## 🚀 Getting Started

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/AnujNandal/Portfolio.git
   cd Portfolio
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

### Deploying on Replit

1. Fork this repository to your GitHub account
2. Create a new Replit project from your GitHub repository
3. Replit will automatically detect the project configuration
4. Click the "Run" button to start the application

## 💡 Customization

### Changing the Theme

The portfolio comes with both dark and light themes. Users can switch between them using the theme toggle button in the top-right corner.

### Updating Personal Information

1. Edit the `templates/index.html` file to update your personal information
2. Replace placeholder images in the `static/images/` directory with your own
3. Update project details in the Projects section of the HTML

## 📝 License

This project is open source and available under the [MIT License](LICENSE).