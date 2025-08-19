# 🌐 Hosting Options for Anuj Nandal's Fake News Detector

## 🚀 1. HEROKU (Recommended - Easy & Free)

### Setup Steps:
1. **Create Heroku Account**: https://heroku.com
2. **Install Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli
3. **Deploy Commands**:
```bash
# Login to Heroku
heroku login

# Create app (choose unique name)
heroku create anuj-fake-news-detector

# Set environment variables
heroku config:set FLASK_ENV=production

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main

# Open your live app
heroku open
```

**Your app will be live at**: `https://anuj-fake-news-detector.herokuapp.com`

---

## ☁️ 2. RENDER.COM (Free Alternative)

### Setup Steps:
1. **Create Account**: https://render.com
2. **Connect GitHub**: Link your repository
3. **Create Web Service**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app/app.py`
   - Environment: `Python 3`

**Features**: Auto-deploy on git push, free HTTPS

---

## 🎯 3. VERCEL (Great for Flask)

### Setup Steps:
1. **Install Vercel CLI**: `npm i -g vercel`
2. **Deploy**:
```bash
vercel --prod
```
3. **Create vercel.json**:
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app/app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app/app.py"
    }
  ]
}
```

---

## 🐍 4. PYTHONANYWHERE (Python-Focused)

### Setup Steps:
1. **Create Account**: https://pythonanywhere.com
2. **Upload Files**: Use file manager or git
3. **Configure Web App**:
   - Python version: 3.8+
   - Source code: `/home/anuj/fake_news_detector/app/app.py`
   - Working directory: `/home/anuj/fake_news_detector`

**Your app**: `https://anuj.pythonanywhere.com`

---

## 🌊 5. RAILWAY (Modern & Fast)

### Setup Steps:
1. **Create Account**: https://railway.app
2. **Connect GitHub**: Link repository
3. **Deploy**: Automatic detection of Flask app
4. **Environment Variables**: Set in dashboard

---

## 📋 Pre-Deployment Checklist:

✅ **Files Created**:
- `Procfile` (for Heroku)
- `requirements.txt` (updated)
- Production-ready `app.py`

✅ **Code Updates**:
- Debug mode disabled
- Port configuration for hosting
- Environment variable support

✅ **Model Files**:
- Ensure `model.pkl` and `vectorizer.pkl` are included
- Check file paths are relative

---

## 🎯 RECOMMENDED: Use Heroku

**Why Heroku?**
- ✅ Free tier available
- ✅ Easy deployment
- ✅ Automatic scaling
- ✅ Good for Flask apps
- ✅ Custom domain support

**Quick Start**:
```bash
git init
git add .
git commit -m "Initial commit"
heroku create your-app-name
git push heroku main
```

Your app will be live in minutes! 🚀
