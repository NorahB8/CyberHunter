"""
CyberHunter ML-Based Phishing Detector
Uses trained Random Forest model for predictions
"""

import pickle
import os
from typing import Dict
from feature_extractor import FeatureExtractor

class PhishingMLDetector:
    """ML-based phishing detector using trained Random Forest model"""

    def __init__(self, model_path='cyberhunter_ml_model.pkl'):
        """Load trained model"""
        self.model_path = model_path

        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Trained model not found at {model_path}\n"
                f"Please run 'python train_model.py' first to train the model."
            )

        print(f"Loading ML model from {model_path}...")
        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)

        self.model = model_data['model']
        # Always use fresh FeatureExtractor so code changes take effect immediately
        self.feature_extractor = FeatureExtractor()
        self.feature_names = model_data['feature_names']
        self.model_accuracy = model_data['accuracy']
        self.cv_score = model_data['cv_score']

        print(f"Model loaded successfully!")
        print(f"  Training accuracy: {self.model_accuracy * 100:.2f}%")
        print(f"  Cross-validation score: {self.cv_score * 100:.2f}%")

    def analyze_email(self, sender_email: str, sender_name: str = '',
                     email_body: str = '', routing_info: str = '') -> Dict:
        """
        Analyze email using trained ML model

        Args:
            sender_email: Email address of sender
            sender_name: Display name of sender
            email_body: Email body text
            routing_info: Email routing info (optional)

        Returns:
            Dictionary with prediction results
        """

        # Prepare email data
        email_data = {
            'sender_email': sender_email,
            'sender_name': sender_name,
            'subject': '',  # Not used in current features
            'body': email_body
        }

        # Extract features
        features_dict = self.feature_extractor.extract_features(email_data)
        feature_vector = [features_dict[name] for name in self.feature_names]

        # CRITICAL SECURITY OVERRIDES - Flag high-risk patterns immediately
        critical_override = False
        override_score = 0

        # 1. Typosquatting/Homograph Attack - CRITICAL
        if features_dict.get('typosquatting', 0) == 1:
            critical_override = True
            override_score = 90  # Very high risk - brand impersonation attempt

        # 2. IP Address as domain - CRITICAL
        elif features_dict.get('has_ip_address', 0) == 1:
            critical_override = True
            override_score = 85  # Very high risk - hiding true domain

        # 3. Brand impersonation with wrong domain - CRITICAL
        elif features_dict.get('brand_impersonation', 0) == 1:
            critical_override = True
            override_score = 88  # Very high risk - pretending to be legitimate company

        # 4. Multiple high-risk indicators - CRITICAL
        elif (features_dict.get('suspicious_keyword_count', 0) >= 5 and
              features_dict.get('domain_spam_keywords', 0) >= 3):
            critical_override = True
            override_score = 80  # High risk - multiple spam indicators

        # 5. Cloud storage abuse - suspicious path on legitimate cloud service - CRITICAL
        # BUT: Exclude legitimate support/help domains
        elif ('storage.googleapis.com' in sender_email or 'amazonaws.com' in sender_email or 's3.' in sender_email):
            # Whitelist legitimate Google/Apple/Microsoft domains
            legitimate_domains = ['support.google.com', 'support.apple.com', 'support.microsoft.com',
                                'buy.itunes.apple.com', 'www.apple.com', 'www.microsoft.com']
            is_legitimate = any(domain in sender_email.lower() for domain in legitimate_domains)

            if not is_legitimate:  # Only flag if NOT a whitelisted domain
                # Flag any HTML file hosted on cloud storage — legitimate sites don't do this
                url_no_frag = sender_email.lower().split('#')[0].split('?')[0]
                if any(url_no_frag.endswith(ext) for ext in ['.html', '.htm', '.php', '.aspx']):
                    critical_override = True
                    override_score = 92
                elif features_dict.get('suspicious_username', 0) == 1 or features_dict.get('gibberish_score', 0) == 1:
                    critical_override = True
                    override_score = 88

        if critical_override:
            # Override ML prediction with critical security score
            risk_score = override_score
            prob_phishing = risk_score / 100
            prob_legitimate = 1 - prob_phishing
        else:
            # Make prediction using ML model
            prediction = self.model.predict([feature_vector])[0]
            prediction_proba = self.model.predict_proba([feature_vector])[0]

            # Get probabilities
            prob_legitimate = prediction_proba[0]
            prob_phishing = prediction_proba[1]

            # Convert to risk score (0-100)
            risk_score = prob_phishing * 100

        # Protocol-based risk adjustment for URLs:
        # HTTP (no SSL) is a strong phishing signal — legitimate sites use HTTPS.
        # HTTPS does NOT guarantee safety (cloud-hosted phishing abuses HTTPS).
        if '://' in sender_email.lower():
            if features_dict.get('uses_https', 0) == 0:
                risk_score = min(100, risk_score + 15)
            else:
                risk_score = max(0, risk_score - 5)

        # Feature-based score boosts — each flagged feature adds to the risk score
        # so every card that shows danger actually moves the number.
        boost = 0
        if features_dict.get('suspicious_tld', 0) == 1:
            boost += 15
        if features_dict.get('gibberish_score', 0) == 1:
            boost += 15
        if features_dict.get('free_email_company', 0) == 1:
            boost += 15
        if features_dict.get('suspicious_keyword_count', 0) >= 3:
            boost += 10
        if features_dict.get('domain_spam_keywords', 0) >= 2:
            boost += 10
        if features_dict.get('subdomain_count', 0) >= 3:
            boost += 10
        if features_dict.get('personal_info_request', 0) > 0:
            boost += 10
        if features_dict.get('urgency_count', 0) >= 2:
            boost += 8
        if features_dict.get('suspicious_username', 0) == 1:
            boost += 8
        if features_dict.get('name_domain_mismatch', 0) == 1:
            boost += 8
        risk_score = min(100, risk_score + boost)

        prob_phishing = risk_score / 100
        prob_legitimate = 1 - prob_phishing

        # Classification
        if risk_score >= 70:
            classification = 'high_risk'
            is_phishing = True
        elif risk_score >= 60:
            classification = 'medium_risk'
            is_phishing = True
        else:
            classification = 'low_risk'
            is_phishing = False

        # Generate feature analysis
        analysis = self._generate_analysis(features_dict, risk_score, sender_email, email_body)

        # Get sender domain
        try:
            sender_domain = sender_email.split('@')[1] if '@' in sender_email else ''
        except:
            sender_domain = ''

        return {
            'is_phishing': is_phishing,
            'confidence': round(max(prob_legitimate, prob_phishing), 3),
            'risk_score': round(risk_score, 2),
            'classification': classification,
            'prediction_probabilities': {
                'legitimate': round(prob_legitimate, 3),
                'phishing': round(prob_phishing, 3)
            },
            'email_features': features_dict,
            'feature_analysis': analysis,
            'sender_domain': sender_domain,
            'model_type': 'random_forest_ml',
            'model_accuracy': round(self.model_accuracy * 100, 2)
        }

    def _generate_analysis(self, features: Dict, risk_score: float, sender_email: str = '', email_body: str = '') -> list:
        """Generate human-readable analysis from features"""
        analysis = []
        body_lower = (email_body or '').lower()

        # CRITICAL WARNINGS FIRST
        if features.get('typosquatting', 0) == 1:
            analysis.append("[CRITICAL] Typosquatting attack detected - impersonating legitimate brand")

        # Cloud storage abuse detection
        url_lower = sender_email.lower()
        if 'storage.googleapis.com' in url_lower:
            url_no_frag = url_lower.split('#')[0].split('?')[0]
            if any(url_no_frag.endswith(ext) for ext in ['.html', '.htm', '.php', '.aspx']):
                analysis.append("[CRITICAL] Phishing page hosted on Google Cloud Storage — scammers upload fake login pages to legitimate cloud services to bypass spam filters. The random bucket name and HTML file are strong indicators this is not a real website.")
            else:
                analysis.append("[WARNING] URL points to Google Cloud Storage — verify this is an expected file download before proceeding.")
        elif 'amazonaws.com' in url_lower or 's3.' in url_lower:
            if any(url_lower.endswith(ext) for ext in ['.html', '.htm', '.php']):
                analysis.append("[CRITICAL] Phishing page hosted on Amazon S3 — scammers use legitimate cloud storage to host fake pages and evade detection.")

        if features.get('brand_impersonation', 0) == 1:
            analysis.append("[CRITICAL] Brand impersonation - sender claims to be known company but uses wrong domain")

        if features.get('has_ip_address', 0) == 1:
            analysis.append("[CRITICAL] Using IP address instead of domain name - highly suspicious")

        # Protocol check
        if '://' in sender_email.lower():
            if features.get('uses_https', 0) == 0:
                analysis.append("[WARNING] URL uses HTTP instead of HTTPS — no encryption, connection can be intercepted")
            else:
                analysis.append("[INFO] URL uses HTTPS — encrypted connection (does not guarantee legitimacy)")

        # Check each feature for suspicious values
        if features.get('suspicious_username', 0) == 1:
            analysis.append("[WARNING] Username matches spam pattern (word+digits)")

        if features.get('domain_spam_keywords', 0) > 0:
            count = int(features['domain_spam_keywords'])
            analysis.append(f"[WARNING] Domain contains {count} spam keyword(s)")

        if features.get('free_email_company', 0) == 1:
            analysis.append("[WARNING] Company name using free email provider (e.g., PayPal from @gmail.com)")

        if features.get('gibberish_score', 0) == 1:
            analysis.append("[WARNING] Domain appears randomly generated")

        if features.get('subdomain_count', 0) >= 3:
            count = int(features['subdomain_count'])
            analysis.append(f"[WARNING] Excessive subdomains ({count} levels)")

        if features.get('suspicious_keyword_count', 0) >= 3:
            count = int(features['suspicious_keyword_count'])
            analysis.append(f"[WARNING] Contains {count} phishing-related keywords")

        # Money/donation/lottery scam detection — only specific terms unlikely in real transactional emails
        money_keywords = [
            'million', 'billion', 'donation', 'donate', 'lottery', 'jackpot',
            'prize', 'award', 'inheritance', 'beneficiary', 'wire transfer',
            'compensation', 'winning', 'you have won', 'claim your'
        ]
        if any(kw in body_lower for kw in money_keywords):
            analysis.append("[CRITICAL] Email mentions large sums of money or financial rewards — common advance-fee fraud tactic")

        # ID / personal document request detection
        id_keywords = [
            'copy of your id', 'copy of passport', 'picture of your id', 'photo of your id',
            'scan of your id', 'scan of your passport', 'send your id', 'send your passport',
            'attach your id', 'national id', 'id or passport', 'id card', 'passport copy',
            'government id', 'identification document', 'proof of identity'
        ]
        if any(kw in body_lower for kw in id_keywords):
            analysis.append("[CRITICAL] Email asks for a photo or copy of your ID/passport — never send this to unknown senders")

        if features.get('urgency_count', 0) >= 2:
            analysis.append("[WARNING] Uses urgency tactics to pressure action")

        if features.get('personal_info_request', 0) > 0:
            analysis.append("[WARNING] Requests personal/financial information")

        if features.get('suspicious_tld', 0) == 1:
            analysis.append("[WARNING] Uses suspicious top-level domain")

        # If no specific warnings but high risk, add general warning
        if not analysis and risk_score >= 70:
            analysis.append("[WARNING] ML model detected high-risk patterns")

        # Add safe message if low risk
        if risk_score < 40 and not analysis:
            analysis.append("[SAFE] No significant phishing indicators detected")

        return analysis

    def get_feature_importance(self, top_n=10):
        """Get top N most important features"""
        feature_importance = sorted(
            zip(self.feature_names, self.model.feature_importances_),
            key=lambda x: x[1],
            reverse=True
        )
        return feature_importance[:top_n]


# Convenience function for quick testing
def test_email(sender_email, sender_name='', email_body=''):
    """Quick test function"""
    try:
        detector = PhishingMLDetector()
        result = detector.analyze_email(sender_email, sender_name, email_body)

        print(f"\nEmail: {sender_email}")
        print(f"Risk Score: {result['risk_score']}%")
        print(f"Classification: {result['classification'].upper()}")
        print(f"Is Phishing: {result['is_phishing']}")
        print(f"Confidence: {result['confidence'] * 100:.1f}%")
        print(f"\nAnalysis:")
        for item in result['feature_analysis']:
            print(f"  {item}")

        return result
    except FileNotFoundError as e:
        print(f"\nError: {e}")
        print("\nPlease run training first:")
        print("  python train_model.py")
        return None


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        email = sys.argv[1]
        name = sys.argv[2] if len(sys.argv) > 2 else ''
        body = sys.argv[3] if len(sys.argv) > 3 else ''
        test_email(email, name, body)
    else:
        print("Usage: python phishing_detector_ml.py <email> [name] [body]")
        print("\nExample:")
        print("  python phishing_detector_ml.py label623435@494540.oceanpark.trip.com FedEx 'Your shipment'")
        print("\nOr import and use:")
        print("  from phishing_detector_ml import PhishingMLDetector")
        print("  detector = PhishingMLDetector()")
        print("  result = detector.analyze_email('test@example.com', 'Test', 'Body')")
