# 🚀 CyberHunter - Quick Start Guide

Welcome to CyberHunter! Get started in 5 minutes.

## ⚡ Quick Setup

### 1. Test the Web Dashboard (Instant!)

No installation needed - just open the file:

```bash
# Navigate to the website folder
cd phishing-detector/website

# Open index.html in your browser
# Double-click the file OR run:
python -m http.server 8000
# Then visit: http://localhost:8000
```

**Try it now:**
- Enter a URL like `https://google.com` (should be safe)
- Try `http://paypa1-verify.tk` (should be flagged as phishing)

### 2. Install the Browser Extension (2 minutes)

**Chrome/Edge:**
1. Open `chrome://extensions/`
2. Turn ON "Developer mode" (top-right)
3. Click "Load unpacked"
4. Select the `phishing-detector/extension` folder
5. Done! 🎉

**Test it:**
1. Open Gmail
2. The extension will show scanning indicators on emails
3. Click the extension icon to see stats

### 3. Run the ML Model & API (Optional)

For the full system with API:

```bash
# Navigate to ml-model folder
cd phishing-detector/ml-model

# Install dependencies
pip install flask flask-cors numpy

# Run the API server
python api_server.py

# API will be available at http://localhost:5000
```

**Test the API:**
```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"url": "https://google.com"}'
```

### 4. Run Tests (See it in action!)

```bash
cd phishing-detector/ml-model
python test_suite.py
```

This will show you the ML model analyzing various URLs with colored output!

## 📱 What Each Component Does

### Web Dashboard (website/)
- **File:** `index.html`
- **Purpose:** Visual URL scanner with real-time analysis
- **Use:** Manually check suspicious URLs
- **No server needed:** Pure HTML/CSS/JavaScript

### Browser Extension (extension/)
- **Files:** `manifest.json`, `content.js`, `popup.html`, etc.
- **Purpose:** Automatic email protection
- **Use:** Scans emails in Gmail/Outlook automatically
- **Works:** Chrome, Edge, Firefox

### ML Model (ml-model/)
- **Files:** `phishing_detector.py`, `api_server.py`
- **Purpose:** Machine learning detection engine
- **Use:** Power the web dashboard and extension (or integrate into your apps)
- **API:** RESTful endpoints for integration

## 🎯 Common Use Cases

### As a Regular User
1. Install the browser extension → Automatic protection ✅
2. Bookmark the web dashboard → Manual URL checking ✅

### As a Developer
1. Run the API server
2. Integrate with your application:
```python
import requests

response = requests.post('http://localhost:5000/api/analyze', 
    json={'url': 'https://example.com'})
result = response.json()

if result['is_phishing']:
    print("⚠️ Warning: This URL is suspicious!")
```

### For Testing/Demo
1. Run `python test_suite.py` to see the ML model in action
2. Open `index.html` to try the visual interface
3. Test URLs in the browser extension

## 🔍 What to Test

### Safe URLs (Should be GREEN/Low Risk)
- https://google.com
- https://github.com
- https://microsoft.com

### Phishing URLs (Should be RED/High Risk)
- http://paypa1-security.tk
- http://amazon-prize-winner.xyz
- https://192.168.1.1/login

### Suspicious URLs (Should be YELLOW/Medium Risk)
- http://bit.ly/abc123 (URL shortener)
- http://verify-account-now.ml
- https://many.sub.domains.example.com

## 💡 Pro Tips

1. **Test Safely**: All analysis happens locally - no URLs are sent to external servers
2. **Browser Extension**: Click the extension icon to see your scan history
3. **API Integration**: The REST API makes it easy to integrate into any application
4. **Feature Analysis**: Look at individual features to understand WHY something is flagged

## 🆘 Troubleshooting

**Extension not working?**
- Make sure you're on Gmail or Outlook
- Refresh the page after installation
- Check browser console for errors (F12)

**API not starting?**
- Install dependencies: `pip install -r requirements.txt`
- Check port 5000 isn't already in use
- Try a different port: `app.run(port=5001)`

**Dashboard not loading?**
- Try using a local server: `python -m http.server 8000`
- Check browser console (F12) for errors
- Make sure JavaScript is enabled

## 📚 Next Steps

1. Read the full README.md for detailed documentation
2. Check out the API documentation
3. Explore the ML model code
4. Customize the features and thresholds
5. Contribute improvements!

## 🎉 You're All Set!

CyberHunter is now protecting you from phishing attacks. Stay safe! 🛡️

---

**Need Help?** Check the README.md or open an issue on GitHub
