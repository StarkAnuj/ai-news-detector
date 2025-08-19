"""
Quick Start Script for Fake News Detection System
This script will help you get started quickly with minimal setup.
"""

print("=" * 60)
print("           FAKE NEWS DETECTION SYSTEM")
print("                Quick Start Guide")
print("=" * 60)
print()

print("Step 1: Install Required Packages")
print("Run this command in your terminal:")
print("    pip install flask scikit-learn pandas numpy nltk joblib matplotlib seaborn requests")
print()

print("Step 2: Train the Model")
print("Navigate to the model directory and run:")
print("    cd model")
print("    python train_model.py")
print()

print("Step 3: Start the Web Application")
print("Navigate to the app directory and run:")
print("    cd app")
print("    python app.py")
print()

print("Step 4: Access the Application")
print("Open your web browser and go to:")
print("    http://localhost:5000")
print()

print("=" * 60)
print("Alternative: Use the Interactive Script")
print("Run: python main.py")
print("Then select option 4 for full setup")
print("=" * 60)

# Try to detect if we can import required packages
print("\nChecking if packages are installed...")
missing_packages = []

packages = [
    'flask', 'sklearn', 'pandas', 'numpy', 
    'nltk', 'joblib', 'matplotlib', 'seaborn', 'requests'
]

for package in packages:
    try:
        __import__(package)
        print(f"✓ {package}")
    except ImportError:
        print(f"✗ {package} (not installed)")
        missing_packages.append(package)

if missing_packages:
    print(f"\nMissing packages: {', '.join(missing_packages)}")
    print("Please install them using pip install command above.")
else:
    print("\n✓ All packages are installed!")
    print("You can now run the training script and web application.")
