# CyberHunter - Quick Start Guide

Get started in 5 minutes.

## Quick Setup

### 1. Train the ML Model (Required First)

The ML model must be trained before the API or website can use it.

```bash
cd ml-model

# Install dependencies
pip install flask flask-cors numpy scikit-learn

# Train the Random Forest model
python train_model.py
```

This creates `cyberhunter_ml_model.pkl` using the training data from `training_data.py`, which contains two separate datasets:
- **EMAIL_TRAINING_DATA** - phishing and legitimate email samples
- **URL_TRAINING_DATA** - phishing and legitimate URL samples

Both are combined into `TRAINING_DATA` for model training.

### 2. Start the API Server

```bash
cd ml-model
python api_server.py
```

The API runs at `http://localhost:5000` with these endpoints:
- `POST /api/analyze` - Analyze a URL or email
- `POST /api/batch-analyze` - Analyze multiple items
- `GET /api/health` - Health check
- `GET /api/stats` - Usage statistics
- `GET /api/features` - Model feature info

### 3. Open the Web Dashboard

Open `index.html` in your browser, or serve it locally:

```bash
python -m http.server 8000
# Visit http://localhost:8000
```

The dashboard works in two modes:
- **With API running** - Uses the Random Forest ML model for full analysis
- **Without API** - Falls back to client-side detection (limited but functional)

### 4. Install the Browser Extension

**Chrome/Edge:**
1. Open `chrome://extensions/`
2. Turn ON "Developer mode" (top-right)
3. Click "Load unpacked"
4. Select the `extensions` folder
5. Open Gmail - the extension scans emails automatically

The extension does two things per email:
- Analyzes the **sender email address** for phishing patterns
- Scans all **links in the email body** for malicious URLs
- If any link scores 70%+, the email is flagged high risk and links are highlighted/blocked

## What Each Component Does

### Web Dashboard (`index.html`)
- Visual URL scanner with feature-by-feature breakdown
- 10 detection features: URL length, domain age, special characters, HTTPS, subdomains, keywords, domain type, URL type, TLD risk, homograph check
- Detects typosquatting, brand-in-subdomain, `@` credential attacks, brand-in-path

### Browser Extension (`extensions/`)
- Real-time email scanning in Gmail/Outlook
- Dual analysis: sender email + all embedded links
- Phishing links are visually highlighted and click-blocked
- Results are cached so re-opening an email re-applies protection
- Works with or without the ML API (falls back to rule-based detection)

### ML Model (`ml-model/`)
- `training_data.py` - Separated email and URL training datasets
- `feature_extractor.py` - Extracts 19 features from emails and URLs
- `train_model.py` - Trains Random Forest classifier
- `phishing_detector_ml.py` - ML prediction with critical security overrides
- `api_server.py` - Flask REST API serving the model
- `phishing_detector.py` - Unified detector with Arabic/English language routing

## What to Test

### Safe URLs (should show low risk)
- `https://google.com`
- `https://www.amazon.com/gp/product/B08N5WRWNW`
- `https://support.apple.com/en-us/HT201222`
- `https://www.paypal.com/myaccount/summary`

### Phishing URLs (should show high risk)
- `http://paypa1-security-verify.tk/login` - typosquatting
- `http://paypal.evil-site.xyz/secure/login` - brand in subdomain
- `http://192.168.1.100/paypal/verify` - IP address as domain
- `http://google.com@evil-site.com/login` - credential attack
- `http://account-verify-secure.xyz/update` - suspicious TLD + keywords
- `http://secure-login-verify-account-update-confirm.tk/auth` - many hyphens + suspicious TLD

### Test via API
```bash
# Safe URL
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"https://google.com\"}"

# Phishing URL
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"http://paypa1-security-verify.tk/login\"}"
```

### Test via Python
```python
import requests

result = requests.post('http://localhost:5000/api/analyze',
    json={'url': 'http://paypa1-security-verify.tk/login'}).json()

print(f"Risk: {result['risk_score']}%")
print(f"Phishing: {result['is_phishing']}")
for msg in result['feature_analysis']:
    print(f"  {msg}")
```

## Adding Training Data

Edit `ml-model/training_data.py`:

```python
# Add to EMAIL_TRAINING_DATA for email samples
EMAIL_TRAINING_DATA = [
    {
        'sender_email': 'phisher@fake-bank.com',
        'sender_name': 'Your Bank',
        'subject': 'Urgent',
        'body': 'Verify your account now',
        'label': 1,  # 1 = phishing, 0 = legitimate
        'category': 'bank_phishing'
    },
    ...
]

# Add to URL_TRAINING_DATA for URL samples
URL_TRAINING_DATA = [
    {
        'sender_email': 'http://evil-site.tk/login',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 1,
        'category': 'phishing_url'
    },
    ...
]
```

After adding data, retrain the model:
```bash
cd ml-model
python train_model.py
```

## Troubleshooting

**"ML model not loaded" error:**
Run `python train_model.py` first to create `cyberhunter_ml_model.pkl`.

**Extension not scanning emails:**
- Refresh Gmail after installing the extension
- Check the browser console (F12) for errors
- Ensure the extension has permission to run on `mail.google.com`

**API not starting:**
- Install dependencies: `pip install -r requirements.txt`
- Check port 5000 isn't in use: try `python api_server.py` on a different port

**Links not highlighted on second view:**
Fixed - the extension now re-applies link highlighting from cache when Gmail re-renders the email DOM.

**Dashboard shows "ML API server is not running":**
Start the API with `python ml-model/api_server.py`. The dashboard will fall back to client-side detection without it, but ML detection is more accurate.
