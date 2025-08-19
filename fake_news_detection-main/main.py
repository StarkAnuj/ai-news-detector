#!/usr/bin/env python3
"""
Fake News Detection System - Main Runner
This script provides options to train the model and run the web application.
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing packages: {e}")
        return False

def train_model():
    """Train the machine learning model"""
    print("\nTraining the model...")
    try:
        # Change to model directory and run training
        model_dir = os.path.join(os.path.dirname(__file__), 'model')
        train_script = os.path.join(model_dir, 'train_model.py')
        
        if not os.path.exists(train_script):
            print(f"✗ Training script not found at {train_script}")
            return False
            
        subprocess.check_call([sys.executable, train_script], cwd=model_dir)
        print("✓ Model training completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error training model: {e}")
        return False

def run_app():
    """Run the Flask web application"""
    print("\nStarting the web application...")
    try:
        app_dir = os.path.join(os.path.dirname(__file__), 'app')
        app_script = os.path.join(app_dir, 'app.py')
        
        if not os.path.exists(app_script):
            print(f"✗ App script not found at {app_script}")
            return False
            
        # Change to app directory and run the Flask app
        os.chdir(app_dir)
        subprocess.call([sys.executable, 'app.py'])
        return True
    except KeyboardInterrupt:
        print("\n✓ Application stopped by user")
        return True
    except Exception as e:
        print(f"✗ Error running application: {e}")
        return False

def check_model_exists():
    """Check if the trained model exists"""
    model_path = os.path.join(os.path.dirname(__file__), 'model', 'model.pkl')
    vectorizer_path = os.path.join(os.path.dirname(__file__), 'model', 'vectorizer.pkl')
    return os.path.exists(model_path) and os.path.exists(vectorizer_path)

def main():
    print("=" * 60)
    print("           FAKE NEWS DETECTION SYSTEM")
    print("=" * 60)
    print()
    
    # Check if model exists
    model_exists = check_model_exists()
    
    if model_exists:
        print("✓ Trained model found!")
    else:
        print("⚠ No trained model found.")
    
    print("\nChoose an option:")
    print("1. Install requirements")
    print("2. Train model (required for first run)")
    print("3. Run web application")
    print("4. Install requirements + Train model + Run app (Full setup)")
    print("5. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                install_requirements()
            elif choice == '2':
                train_model()
            elif choice == '3':
                if not model_exists and not check_model_exists():
                    print("⚠ Warning: No trained model found. Please train the model first (option 2).")
                    continue
                run_app()
                break
            elif choice == '4':
                success = True
                success &= install_requirements()
                success &= train_model()
                if success:
                    run_app()
                break
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1-5.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()