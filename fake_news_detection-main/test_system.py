#!/usr/bin/env python3
"""
Test script for the Fake News Detection System
This script runs some basic tests to ensure everything is working correctly.
"""

import os
import sys

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    try:
        import flask
        import sklearn
        import pandas
        import nltk
        import joblib
        import matplotlib
        import seaborn
        import requests
        print("✓ All imports successful!")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_file_structure():
    """Test if all required files exist"""
    print("\nTesting file structure...")
    required_files = [
        'app/app.py',
        'app/templates/index.html',
        'app/templates/result.html',
        'app/templates/train.html',
        'model/train_model.py',
        'requirements.txt',
        'main.py'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("✗ Missing files:")
        for file in missing_files:
            print(f"  - {file}")
        return False
    else:
        print("✓ All required files present!")
        return True

def test_sample_prediction():
    """Test the text processing functions"""
    print("\nTesting text processing...")
    try:
        # Import the text processing functions
        sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))
        from app import clean_text, preprocess_text
        
        # Test text
        sample_text = "This is a SAMPLE news article with URLs http://example.com and special characters!@#"
        
        # Test cleaning
        cleaned = clean_text(sample_text)
        print(f"Original: {sample_text}")
        print(f"Cleaned: {cleaned}")
        
        # Test preprocessing (requires NLTK data)
        try:
            processed = preprocess_text(cleaned)
            print(f"Processed: {processed}")
            print("✓ Text processing successful!")
            return True
        except Exception as e:
            print(f"⚠ Preprocessing failed (NLTK data may be missing): {e}")
            return False
            
    except Exception as e:
        print(f"✗ Text processing error: {e}")
        return False

def main():
    print("=" * 50)
    print("    FAKE NEWS DETECTION SYSTEM - TEST")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_file_structure,
        test_sample_prediction
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print("-" * 30)
    
    print(f"\nTest Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! The system should work correctly.")
        print("\nNext steps:")
        print("1. Run 'python main.py' to start the system")
        print("2. Choose option 4 for full setup")
        print("3. Access the web interface at http://localhost:5000")
    else:
        print("⚠ Some tests failed. Please check the errors above.")
        print("\nRecommended actions:")
        print("1. Install requirements: pip install -r requirements.txt")
        print("2. Check file structure")
        print("3. Run the main script: python main.py")

if __name__ == "__main__":
    main()
