"""
CyberHunter API Server
Flask-based REST API for phishing detection using Random Forest ML
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from phishing_detector_ml import PhishingMLDetector
import logging
from datetime import datetime
import os
import zipfile
import io
app = Flask(__name__)
CORS(app)  # Enable CORS for browser extension and web interface

# Initialize ML model
print("Loading Random Forest ML model...")
try:
    model = PhishingMLDetector()
    print("ML model loaded successfully!")
except FileNotFoundError as e:
    print(f"ERROR: {e}")
    print("Please run 'python train_model.py' first to train the model.")
    model = None

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Statistics tracking
stats = {
    'total_requests': 0,
    'phishing_detected': 0,
    'safe_urls': 0,
    'start_time': datetime.now()
}


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    uptime = (datetime.now() - stats['start_time']).total_seconds()
    
    return jsonify({
        'status': 'healthy',
        'uptime_seconds': uptime,
        'model_loaded': True,
        'version': '1.0.0'
    })


@app.route('/api/analyze', methods=['POST'])
def analyze_url():
    """
    Analyze a URL for phishing using ML model.

    Request body:
    {
        "url": "https://example.com",
        "sender_name": "Optional sender name",
        "email_body": "Optional email body"
    }

    Response:
    {
        "is_phishing": false,
        "confidence": 0.95,
        "risk_score": 5.2,
        "classification": "low_risk",
        "email_features": {...},
        "feature_analysis": [...],
        "model_type": "random_forest_ml"
    }
    """
    try:
        if model is None:
            return jsonify({
                'error': 'ML model not loaded. Run train_model.py first.'
            }), 500

        data = request.get_json()

        if not data or 'url' not in data:
            return jsonify({
                'error': 'Missing URL parameter'
            }), 400

        url = data['url']

        if not url or not isinstance(url, str):
            return jsonify({
                'error': 'Invalid URL format'
            }), 400

        # Extract optional fields
        sender_name = data.get('sender_name', '')
        email_body = data.get('email_body', '')

        # Pass the URL directly to the ML model - the feature extractor
        # now properly handles both URLs and email addresses via _parse_input()
        sender_email = url

        # Perform ML analysis
        result = model.analyze_email(
            sender_email=sender_email,
            sender_name=sender_name,
            email_body=email_body
        )

        # Update statistics
        stats['total_requests'] += 1
        if result['is_phishing']:
            stats['phishing_detected'] += 1
        else:
            stats['safe_urls'] += 1

        # Log request
        logger.info(f"ML Analysis: {sender_email} | Risk: {result['risk_score']}% | Phishing: {result['is_phishing']}")

        return jsonify(result)

    except Exception as e:
        logger.error(f"Error analyzing URL: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500


@app.route('/api/batch-analyze', methods=['POST'])
def batch_analyze():
    """
    Analyze multiple URLs/emails at once using ML model.

    Request body:
    {
        "emails": [
            {"email": "test@example.com", "name": "Test", "body": "Body text"},
            ...
        ]
    }

    Response:
    {
        "results": [...],
        "count": 2
    }
    """
    try:
        if model is None:
            return jsonify({
                'error': 'ML model not loaded. Run train_model.py first.'
            }), 500

        data = request.get_json()

        if not data or 'emails' not in data:
            return jsonify({
                'error': 'Missing emails parameter'
            }), 400

        emails = data['emails']

        if not isinstance(emails, list) or len(emails) == 0:
            return jsonify({
                'error': 'emails must be a non-empty array'
            }), 400

        if len(emails) > 100:
            return jsonify({
                'error': 'Maximum 100 emails per request'
            }), 400

        # Analyze all emails
        results = []
        for email_data in emails:
            sender_email = email_data.get('email', '')
            sender_name = email_data.get('name', '')
            email_body = email_data.get('body', '')

            result = model.analyze_email(
                sender_email=sender_email,
                sender_name=sender_name,
                email_body=email_body
            )
            results.append(result)

        # Update statistics
        stats['total_requests'] += len(emails)
        for result in results:
            if result['is_phishing']:
                stats['phishing_detected'] += 1
            else:
                stats['safe_urls'] += 1

        logger.info(f"Batch analyzed {len(emails)} emails with ML model")

        return jsonify({
            'results': results,
            'count': len(results)
        })

    except Exception as e:
        logger.error(f"Error in batch analysis: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get API statistics"""
    uptime = (datetime.now() - stats['start_time']).total_seconds()
    
    return jsonify({
        'total_requests': stats['total_requests'],
        'phishing_detected': stats['phishing_detected'],
        'safe_urls': stats['safe_urls'],
        'uptime_seconds': uptime,
        'uptime_hours': uptime / 3600,
        'detection_rate': (
            stats['phishing_detected'] / stats['total_requests'] * 100 
            if stats['total_requests'] > 0 else 0
        )
    })


@app.route('/api/features', methods=['GET'])
def get_features():
    """Get information about ML model features"""
    if model is None:
        return jsonify({
            'error': 'ML model not loaded'
        }), 500

    # Get feature importance from ML model
    feature_importance = model.get_feature_importance(18)  # Get all features

    return jsonify({
        'model_type': 'Random Forest ML',
        'feature_count': len(feature_importance),
        'features': [{'name': name, 'importance': float(importance)}
                    for name, importance in feature_importance],
        'model_accuracy': model.model_accuracy,
        'cv_score': model.cv_score,
        'description': 'Features learned by Random Forest classifier from training data'
    })


@app.route('/api/download-extension', methods=['GET'])
def download_extension():
    """Download browser extension as ZIP file"""
    try:
        # Get the extensions folder path (one level up from ml-model)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)
        extensions_dir = os.path.join(project_root, 'extensions')

        if not os.path.exists(extensions_dir):
            return jsonify({
                'error': 'Extensions folder not found'
            }), 404

        # Create ZIP file in memory
        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Walk through the extensions directory
            for root, dirs, files in os.walk(extensions_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Calculate the archive name (relative path from extensions_dir)
                    arcname = os.path.relpath(file_path, extensions_dir)
                    zf.write(file_path, arcname)

        # Seek to the beginning of the BytesIO buffer
        memory_file.seek(0)

        logger.info("Extension ZIP file created successfully")

        return send_file(
            memory_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name='cyberhunter-extension.zip'
        )

    except Exception as e:
        logger.error(f"Error creating extension ZIP: {str(e)}")
        return jsonify({
            'error': 'Failed to create extension ZIP',
            'message': str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'available_endpoints': [
            'GET /api/health',
            'POST /api/analyze',
            'POST /api/batch-analyze',
            'GET /api/stats',
            'GET /api/features'
        ]
    }), 404


@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    logger.info("Starting CyberHunter API Server...")
    logger.info("ML Model initialized successfully")
    logger.info("Available endpoints:")
    logger.info("  - GET  /api/health")
    logger.info("  - POST /api/analyze")
    logger.info("  - POST /api/batch-analyze")
    logger.info("  - GET  /api/stats")
    logger.info("  - GET  /api/features")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
