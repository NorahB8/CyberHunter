"""
CyberHunter English Phishing Detection Model
Specialized for English language phishing emails
"""

import re
import numpy as np
from urllib.parse import urlparse
from typing import Dict, List

class PhishingMLModelEnglish:
    """
    English-focused phishing detection model
    """

    def __init__(self):
        # English-only suspicious keywords
        self.suspicious_keywords = [
            'verify', 'account', 'suspended', 'urgent', 'confirm', 'update',
            'security', 'click', 'login', 'password', 'banking', 'paypal',
            'amazon', 'winner', 'prize', 'free', 'claim', 'limited', 'expire',
            'parcel', 'delivery', 'tracking', 'schedule', 'address', 'warehouse',
            'manufacturer', 'resolve', 'missing information', 'unable to deliver',
            'business days', 'return', 'retrieve', 'unsubscribe',
            'asap', 'immediate', 'act now', 'verify now', 'today only',
            'blocked', 'unauthorized', 'compromised', 'locked', 'unusual activity',
            'ssn', 'social security', 'credit card', 'bank account', 'cvv', 'pin',
            'confirm immediately', 'account will be closed', 'last chance'
        ]

        self.suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.club']
        self.legitimate_tlds = ['.com', '.org', '.edu', '.gov', '.net']

        self.url_shorteners = [
            'bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly', 'is.gd',
            'buff.ly', 'adf.ly', 'shorte.st', 'bc.vc'
        ]

        # Suspicious domain patterns for spam detection
        self.suspicious_domain_patterns = [
            'wildzone', 'ultraprize', 'entryport', 'megasnap', 'flashvault',
            'quickfire', 'zonejump', 'rapidlink', 'freezone', 'netgrab',
            'instawin', 'prizepool', 'luckyzone', 'winfast', 'grabprize',
            'spam', 'temp', 'fake', 'scam', 'phish', 'suspicious', 'malware',
            'oceanpark', 'trip', 'entryway', 'giantreward', 'choresrecords',
            'junglerealm', 'pathway', 'gatehouse', 'superwin', 'antiwalmart'
        ]

        # Suspicious username patterns
        self.suspicious_username_patterns = [
            r'^[a-z]{3,8}\d{4,8}$',  # word + many digits
            r'^[A-Za-z]{8,}$',       # random long char sequence
            r'^[a-z]{2,4}\d{2,4}$',  # short word + digits
            r'^\d+[a-z]+\d+$',       # digits-letters-digits
            r'^[A-Z][a-z]{2,}[A-Z][a-z]{2,}$'  # MixedCase
        ]

        # English brand names and domains
        self.legitimate_brands = {
            'dhl': ['dhl.com', 'dhl.de', 'dhl.co.uk'],
            'fedex': ['fedex.com', 'fedex.co.uk'],
            'ups': ['ups.com'],
            'usps': ['usps.com', 'usps.gov'],
            'paypal': ['paypal.com'],
            'amazon': ['amazon.com', 'amazon.co.uk'],
            'ebay': ['ebay.com'],
            'microsoft': ['microsoft.com', 'outlook.com', 'live.com'],
            'apple': ['apple.com', 'icloud.com'],
            'google': ['google.com', 'gmail.com'],
            'netflix': ['netflix.com'],
            'facebook': ['facebook.com', 'fb.com'],
            'chase': ['chase.com'],
            'wells fargo': ['wellsfargo.com'],
            'bank of america': ['bankofamerica.com'],
            'citibank': ['citibank.com']
        }

        # Feature weights optimized for English
        self.feature_weights = {
            'url_length': 0.08,
            'domain_age': 0.12,
            'https_enabled': 0.10,
            'suspicious_chars': 0.09,
            'subdomain_count': 0.11,
            'suspicious_keywords': 0.16,  # Higher for English
            'ip_address': 0.13,
            'url_shortener': 0.07,
            'tld_risk': 0.09,
            'homograph_attack': 0.06,
            'gibberish_domain': 0.14,
            'brand_impersonation': 0.17,  # Higher for English brands
            'email_routing_suspicious': 0.12,
            'noreply_mismatch': 0.10,
            'sender_name_mismatch': 0.15,
            'username_suspicious': 0.12,
            'domain_suspicious': 0.14,
            'overall_email_risk': 0.16
        }

    def _feature_suspicious_keywords(self, text: str) -> float:
        """Check for English phishing keywords"""
        text_lower = text.lower()
        matches = sum(1 for kw in self.suspicious_keywords if kw in text_lower)

        if matches > 2:
            return 1.0
        elif matches > 0:
            return matches / 3
        else:
            return 0.0

    def _feature_gibberish_domain(self, domain: str) -> float:
        """Detect gibberish domains"""
        if not domain:
            return 0.0

        domain_without_tld = domain[:domain.rfind('.')]

        # Check for repeated substrings
        length = len(domain_without_tld)
        if length > 10:
            half = length // 2
            first_half = domain_without_tld[:half]
            second_half = domain_without_tld[half:half*2]
            if first_half == second_half:
                return 1.0

        # Check vowel ratio (English has ~40% vowels)
        vowels = 'aeiouAEIOU'
        vowel_count = sum(1 for c in domain_without_tld if c in vowels)
        total_letters = sum(1 for c in domain_without_tld if c.isalpha())

        if total_letters > 0:
            vowel_ratio = vowel_count / total_letters
            if vowel_ratio < 0.2:
                return 1.0
            elif vowel_ratio < 0.3:
                return 0.7

        # Check for excessive consonant clusters
        consonant_clusters = re.findall(r'[^aeiouAEIOU]{4,}', domain_without_tld)
        if consonant_clusters:
            return 0.8

        return 0.0

    def _feature_brand_impersonation(self, domain: str, email_content: str = '') -> float:
        """Detect English brand impersonation"""
        domain_lower = domain.lower()
        content_lower = email_content.lower()

        for brand, legitimate_domains in self.legitimate_brands.items():
            brand_mentioned = brand in content_lower or brand in domain_lower

            if brand_mentioned:
                is_legitimate = any(legit_domain in domain_lower
                                   for legit_domain in legitimate_domains)

                if not is_legitimate:
                    return 1.0

        return 0.0

    def _analyze_username(self, email_address: str) -> float:
        """Analyze email username for suspicious patterns"""
        if not email_address or '@' not in email_address:
            return 0.0

        try:
            username = email_address.split('@')[0].strip()

            if len(username) <= 2:
                return 0.8

            for pattern in self.suspicious_username_patterns:
                if re.match(pattern, username):
                    return 1.0

            if len(username) >= 8:
                vowels = sum(1 for c in username if c.lower() in 'aeiou')
                if vowels == 0:
                    return 1.0
                elif username.isalpha() and vowels / len(username) < 0.2:
                    return 0.9

            digit_count = sum(1 for c in username if c.isdigit())
            if digit_count > 4:
                return 0.7

            return 0.0
        except:
            return 0.0

    def _analyze_domain(self, domain: str) -> float:
        """Analyze domain for spam patterns"""
        if not domain:
            return 0.0

        domain_lower = domain.lower()
        score = 0.0

        # IP address
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        if re.search(ip_pattern, domain):
            return 1.0

        # Long digit sequences
        if re.search(r'\d{8,}', domain):
            score += 0.8

        # Spam keywords
        for keyword in self.suspicious_domain_patterns:
            if keyword in domain_lower:
                score += 0.6
                break

        # Subdomain count
        subdomain_count = domain.count('.') - 1
        if subdomain_count >= 4:
            score += 0.7
        elif subdomain_count >= 3:
            score += 0.5

        # Long domain
        if len(domain) > 50:
            score += 0.4

        # Excessive hyphens
        if domain.count('-') >= 3:
            score += 0.5

        return min(1.0, score)

    def _analyze_email_address(self, email_address: str) -> Dict[str, float]:
        """Comprehensive email address analysis"""
        if not email_address or '@' not in email_address:
            return {
                'username_suspicious': 0.0,
                'domain_suspicious': 0.0,
                'overall_email_risk': 0.0
            }

        try:
            username, domain = email_address.split('@', 1)

            username_score = self._analyze_username(email_address)
            domain_score = self._analyze_domain(domain)

            overall = (username_score * 0.4) + (domain_score * 0.6)

            return {
                'username_suspicious': username_score,
                'domain_suspicious': domain_score,
                'overall_email_risk': overall
            }
        except:
            return {
                'username_suspicious': 0.0,
                'domain_suspicious': 0.0,
                'overall_email_risk': 0.0
            }

    def _feature_sender_name_mismatch(self, sender_email: str, sender_name: str) -> float:
        """Detect sender name mismatches"""
        if not sender_email or not sender_name:
            return 0.0

        sender_email_lower = sender_email.lower()
        sender_name_lower = sender_name.lower()

        try:
            email_domain = sender_email.split('@')[1] if '@' in sender_email else sender_email
        except:
            return 0.5

        free_providers = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
                         'aol.com', 'mail.com', 'protonmail.com', 'yandex.com']

        for brand, legitimate_domains in self.legitimate_brands.items():
            if brand in sender_name_lower:
                if any(provider in sender_email_lower for provider in free_providers):
                    return 1.0

                is_legitimate = any(domain in email_domain.lower()
                                   for domain in legitimate_domains)
                if not is_legitimate:
                    return 1.0

        suspicious_chars_count = sum(sender_name.count(c) for c in ['©', '®', '™'])
        if suspicious_chars_count > 1:
            return 0.7

        return 0.0

    def analyze_email(self, sender_email: str, sender_name: str = '',
                     email_body: str = '', routing_info: str = '') -> Dict:
        """
        Analyze email for phishing (English-focused)
        """
        try:
            if '@' in sender_email:
                sender_domain = sender_email.split('@')[1]
            else:
                sender_domain = sender_email
        except:
            sender_domain = ''

        email_address_analysis = self._analyze_email_address(sender_email)

        email_features = {
            'gibberish_domain': self._feature_gibberish_domain(sender_domain),
            'brand_impersonation': self._feature_brand_impersonation(
                sender_domain, f"{sender_name} {email_body}"),
            'sender_name_mismatch': self._feature_sender_name_mismatch(sender_email, sender_name),
            'suspicious_keywords': self._feature_suspicious_keywords(
                f"{sender_name} {email_body}"),
            'username_suspicious': email_address_analysis['username_suspicious'],
            'domain_suspicious': email_address_analysis['domain_suspicious'],
            'overall_email_risk': email_address_analysis['overall_email_risk']
        }

        # Calculate risk score
        risk_score = 0.0
        for feature_name, feature_value in email_features.items():
            weight = self.feature_weights.get(feature_name, 0.05)
            risk_score += feature_value * weight

        risk_score = min(100, risk_score * 100)

        # Classification
        if risk_score >= 70:
            classification = 'high_risk'
            is_phishing = True
            confidence = risk_score / 100
        elif risk_score >= 40:
            classification = 'medium_risk'
            is_phishing = True
            confidence = 0.5 + (risk_score - 40) / 60 * 0.3
        else:
            classification = 'low_risk'
            is_phishing = False
            confidence = 1.0 - (risk_score / 100)

        # Generate analysis
        analysis = []
        if email_features.get('username_suspicious', 0) > 0.7:
            analysis.append("[WARNING] Suspicious email username pattern detected")
        if email_features.get('domain_suspicious', 0) > 0.6:
            analysis.append("[WARNING] Sender domain contains spam keywords")
        if email_features.get('overall_email_risk', 0) > 0.6:
            analysis.append("[WARNING] Email address shows spam characteristics")
        if email_features.get('gibberish_domain', 0) > 0.6:
            analysis.append("[WARNING] Sender domain appears randomly generated")
        if email_features.get('brand_impersonation', 0) > 0.5:
            analysis.append("[WARNING] Email claims to be from known brand with wrong domain")
        if email_features.get('sender_name_mismatch', 0) > 0.6:
            analysis.append("[WARNING] Sender display name doesn't match email address")
        if email_features.get('suspicious_keywords', 0) > 0.5:
            analysis.append("[WARNING] Contains phishing-related keywords")

        if not analysis:
            analysis.append("[SAFE] No significant phishing indicators detected")

        return {
            'is_phishing': is_phishing,
            'confidence': round(confidence, 3),
            'risk_score': round(risk_score, 2),
            'classification': classification,
            'email_features': {k: round(v, 3) for k, v in email_features.items()},
            'feature_analysis': analysis,
            'sender_domain': sender_domain,
            'language': 'english'
        }
