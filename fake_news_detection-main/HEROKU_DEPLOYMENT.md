# Anuj Nandal's Fake News Detector - Heroku Deployment Guide

## Prerequisites
1. Create a free Heroku account at https://heroku.com
2. Install Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli

## Step 1: Prepare Your Project
1. Create a Procfile in your project root
2. Update requirements.txt
3. Configure Flask for production

## Step 2: Heroku Commands
```bash
# Login to Heroku
heroku login

# Create a new Heroku app
heroku create anuj-fake-news-detector

# Deploy your code
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# Open your app
heroku open
```

## Step 3: Environment Variables
Set any required environment variables:
```bash
heroku config:set FLASK_ENV=production
```

## Your app will be live at:
https://anuj-fake-news-detector.herokuapp.com
