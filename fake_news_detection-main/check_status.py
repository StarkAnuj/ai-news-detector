#!/usr/bin/env python3
"""
System Status Checker - Run this to verify everything is working
"""

import sys
import os

def check_environment():
    print("🔍 Checking Python Environment...")
    print(f"Python Version: {sys.version}")
    print(f"Python Path: {sys.executable}")
    print()

def check_packages():
    print("📦 Checking Required Packages...")
    packages = [
        'flask', 'sklearn', 'pandas', 'numpy', 
        'nltk', 'joblib', 'matplotlib', 'seaborn', 'requests'
    ]
    
    all_installed = True
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def check_files():
    print("\n📁 Checking Project Files...")
    required_files = [
        'app/app.py',
        'app/templates/index.html',
        'app/templates/result.html',
        'model/train_model.py',
        'requirements.txt'
    ]
    
    all_present = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            all_present = False
    
    return all_present

def main():
    print("=" * 60)
    print("    FAKE NEWS DETECTION SYSTEM - STATUS CHECK")
    print("=" * 60)
    print()
    
    check_environment()
    
    packages_ok = check_packages()
    files_ok = check_files()
    
    print("\n" + "=" * 60)
    if packages_ok and files_ok:
        print("🎉 SYSTEM READY!")
        print("✅ All packages installed")
        print("✅ All files present")
        print("\nNext steps:")
        print("1. Train the model: python model/train_model.py")
        print("2. Start the app: python app/app.py")
        print("3. Open browser: http://localhost:5000")
    else:
        print("⚠️  SYSTEM NOT READY")
        if not packages_ok:
            print("❌ Some packages missing - run: pip install -r requirements.txt")
        if not files_ok:
            print("❌ Some files missing - check project structure")
    print("=" * 60)

if __name__ == "__main__":
    main()
