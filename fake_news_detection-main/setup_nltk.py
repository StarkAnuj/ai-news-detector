#!/usr/bin/env python3
"""
NLTK Data Downloader
This script downloads all required NLTK data for the fake news detection system.
"""

import nltk
import sys

def download_nltk_data():
    """Download all required NLTK data"""
    print("Downloading NLTK data...")
    print("This may take a few minutes on first run...")
    
    # List of required NLTK data
    required_data = [
        'punkt',
        'punkt_tab', 
        'stopwords',
        'wordnet',
        'omw-1.4',
        'averaged_perceptron_tagger',
        'vader_lexicon'
    ]
    
    success_count = 0
    total_count = len(required_data)
    
    for data_name in required_data:
        try:
            print(f"Downloading {data_name}...")
            nltk.download(data_name, quiet=True)
            print(f"✓ {data_name} downloaded successfully")
            success_count += 1
        except Exception as e:
            print(f"✗ Failed to download {data_name}: {e}")
    
    print(f"\nDownload Summary: {success_count}/{total_count} items downloaded successfully")
    
    if success_count == total_count:
        print("🎉 All NLTK data downloaded successfully!")
        return True
    else:
        print("⚠️ Some downloads failed, but the system should still work")
        return False

def test_nltk_functionality():
    """Test basic NLTK functionality"""
    print("\nTesting NLTK functionality...")
    
    try:
        # Test tokenization
        from nltk.tokenize import word_tokenize
        tokens = word_tokenize("This is a test sentence.")
        print(f"✓ Tokenization works: {tokens}")
        
        # Test stopwords
        from nltk.corpus import stopwords
        stop_words = set(stopwords.words('english'))
        print(f"✓ Stopwords loaded: {len(stop_words)} words")
        
        # Test lemmatization
        from nltk.stem import WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()
        lemma = lemmatizer.lemmatize("running", "v")
        print(f"✓ Lemmatization works: running -> {lemma}")
        
        print("🎉 All NLTK functionality is working!")
        return True
        
    except Exception as e:
        print(f"✗ NLTK test failed: {e}")
        return False

def main():
    print("=" * 60)
    print("           NLTK DATA SETUP")
    print("=" * 60)
    
    download_success = download_nltk_data()
    test_success = test_nltk_functionality()
    
    print("\n" + "=" * 60)
    if download_success and test_success:
        print("✅ NLTK setup completed successfully!")
        print("You can now run the model training.")
    else:
        print("⚠️ NLTK setup had some issues but may still work.")
        print("Try running the training script to see if it works.")
    print("=" * 60)

if __name__ == "__main__":
    main()
