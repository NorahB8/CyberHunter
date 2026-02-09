# CyberHunter ML API Server - Quick Start

## 🚀 Start the API Server

### Step 1: Install Flask Dependencies

```bash
pip install flask flask-cors
```

### Step 2: Start the API Server

```bash
cd ml-model
python api_server.py
```

**Expected Output:**
```
Loading Random Forest ML model...
Model loaded successfully!
  Training accuracy: 85.71%
  Cross-validation score: 93.33%
Starting CyberHunter API Server...
ML Model initialized successfully
Available endpoints:
  - GET  /api/health
  - POST /api/analyze
  - POST /api/batch-analyze
  - GET  /api/stats
  - GET  /api/features
 * Running on http://0.0.0.0:5000
```

### Step 3: Open the Website

Open `index.html` in your browser and test with these URLs:

**Test URLs:**
- ✅ Safe: `https://google.com`
- ⚠️ Phishing: `http://paypa1.com` (typosquatting)
- ⚠️ Phishing: `label623435@494540.oceanpark.trip.com` (spam pattern)

---

## 📡 API Endpoints

### 1. Health Check
```bash
curl http://localhost:5000/api/health
```

### 2. Analyze URL/Email
```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"url":"paypa1.com"}'
```

**Response:**
```json
{
  "is_phishing": true,
  "risk_score": 90.0,
  "classification": "high_risk",
  "confidence": 0.9,
  "model_type": "random_forest_ml",
  "feature_analysis": [
    "[WARNING] Impersonating known brand with wrong domain",
    "[WARNING] Username matches spam pattern"
  ]
}
```

### 3. Get Model Features
```bash
curl http://localhost:5000/api/features
```

### 4. Get Statistics
```bash
curl http://localhost:5000/api/stats
```

---

## 🌐 Using the Web Interface

1. **Start API Server** (see Step 2 above)
2. **Open index.html** in browser
3. **Enter URL** to analyze
4. **Click "Scan URL"**

The website will:
- ✅ Send URL to ML API
- ✅ Get prediction from Random Forest model
- ✅ Display results with confidence score

**If API is not running:**
- Website falls back to client-side rule-based detection
- Shows alert: "ML API server is not running"

---

## 🔧 Troubleshooting

### Error: "ML model not loaded"

**Solution:** Train the model first:
```bash
cd ml-model
python train_model.py
```

This creates `cyberhunter_ml_model.pkl`

### Error: "Port 5000 already in use"

**Solution:** Change port in `api_server.py`:
```python
app.run(host='0.0.0.0', port=5001, debug=True)
```

And update `index.html`:
```javascript
const API_URL = 'http://localhost:5001/api/analyze';
```

### Error: "CORS policy blocked"

**Solution:** Flask-CORS is already enabled in api_server.py. Make sure:
1. API server is running
2. Using `http://localhost:5000` not `http://127.0.0.1:5000`

---

## 📊 What's Using ML?

| Component | ML Model | Detection Method |
|-----------|----------|------------------|
| **Website** (`index.html`) | ✅ **YES** | Calls API → Random Forest |
| **Browser Extension** | ❌ **NO** | Rule-based (can be updated) |
| **API Server** | ✅ **YES** | Random Forest classifier |
| **Python Scripts** | ✅ **YES** | `phishing_detector_ml.py` |

---

## 🎯 Next Steps

### Option 1: Test Current Setup
1. Start API server
2. Test website with phishing URLs
3. Check API stats: `curl http://localhost:5000/api/stats`

### Option 2: Update Browser Extension
- Connect extension to API (like website does)
- Real-time ML detection in Gmail/Outlook

### Option 3: Deploy API
- Deploy to Heroku/AWS/Azure
- Update API_URL in index.html to production URL
- Enable HTTPS for production

---

**Ready to test!** 🛡️
