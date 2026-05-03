"""
CyberHunter Arabic Phishing Detection Model
Specialized for Arabic language phishing emails
"""

import re
import numpy as np
from urllib.parse import urlparse
from typing import Dict, List

class PhishingMLModelArabic:
    """
    Arabic-focused phishing detection model
    """

    def __init__(self):
        # Arabic-only suspicious keywords
        self.suspicious_keywords = [
            # Arabic urgency words
            'عاجل', 'فوري', 'حالاً', 'ينتهي', 'تنتهي', 'معلق', 'تحقق الآن',
            'تصرف الآن', 'وقت محدود', 'اليوم فقط', 'أكد فوراً',
            'سيتم إغلاق الحساب', 'آخر فرصة', 'خلال 24 ساعة',
            # Arabic threat words
            'محظور', 'غير مصرح', 'مخترق', 'تنبيه أمني', 'نشاط غير عادي',
            'مقفل', 'تم الحظر', 'إيقاف', 'تجميد',
            # Arabic personal info words
            'كلمة المرور', 'كلمة السر', 'بطاقة ائتمان', 'حساب مصرفي',
            'رقم سري', 'رمز التحقق', 'الرقم السري', 'بيانات شخصية',
            'معلومات البطاقة', 'تاريخ الانتهاء', 'رقم الحساب',
            # Arabic general phishing terms
            'تحقق', 'حساب', 'تأكيد', 'تحديث', 'أمان', 'انقر',
            'تسجيل الدخول', 'مصرفي', 'بنك', 'فائز', 'جائزة',
            'مجاني', 'يدعي', 'محدود', 'طرد', 'شحنة', 'توصيل',
            'تتبع', 'جدولة', 'عنوان', 'مستودع', 'مصنع', 'حل',
            'معلومات مفقودة', 'غير قادر على التسليم', 'أيام عمل',
            'إرجاع', 'استرجاع', 'إلغاء الاشتراك', 'تعليق', 'موقوف',
            'حظر', 'إغلاق', 'تفعيل', 'ضروري', 'مطلوب', 'الآن',
            'اليوم', 'رقم التتبع', 'رسالة', 'إشعار', 'تحذير'
        ]

        self.suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.club']
        self.legitimate_tlds = ['.com', '.org', '.edu', '.gov', '.net', '.sa']

        # Suspicious domain patterns
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
            r'^[a-z]{3,8}\d{4,8}$',
            r'^[A-Za-z]{8,}$',
            r'^[a-z]{2,4}\d{2,4}$',
            r'^\d+[a-z]+\d+$',
            r'^[A-Z][a-z]{2,}[A-Z][a-z]{2,}$'
        ]

        # Arabic brand names and domains
        self.legitimate_brands = {
            # International brands (Arabic names)
            'دي اتش ال': ['dhl.com', 'dhl.de', 'dhl.co.uk'],
            'فيدكس': ['fedex.com', 'fedex.co.uk'],
            'فيديكس': ['fedex.com', 'fedex.co.uk'],
            'أمازون': ['amazon.com', 'amazon.sa'],
            'مايكروسوفت': ['microsoft.com', 'outlook.com'],
            'آبل': ['apple.com', 'icloud.com'],
            'جوجل': ['google.com', 'gmail.com'],
            'نتفليكس': ['netflix.com'],
            'فيسبوك': ['facebook.com'],
            # Arabic banks
            'الراجحي': ['alrajhibank.com.sa'],
            'راجحي': ['alrajhibank.com.sa'],
            'الأهلي': ['alahli.com'],
            'أهلي': ['alahli.com'],
            'سامبا': ['samba.com'],
            'الرياض': ['riyadbank.com'],
            'رياض': ['riyadbank.com'],
            'البنك العربي': ['arabbank.com'],
            'الإنماء': ['alinma.com'],
            'إنماء': ['alinma.com'],
            'البلاد': ['bankalbilad.com'],
            'بلاد': ['bankalbilad.com'],
            # Telecom companies
            'stc': ['stc.com.sa'],
            'إس تي سي': ['stc.com.sa'],
            'موبايلي': ['mobily.com.sa'],
            'زين': ['sa.zain.com'],
            # English names also
            'dhl': ['dhl.com'],
            'fedex': ['fedex.com'],
            'paypal': ['paypal.com'],
            'amazon': ['amazon.com', 'amazon.sa']
        }

        # Feature weights optimized for Arabic
        self.feature_weights = {
            'url_length': 0.08,
            'domain_age': 0.12,
            'https_enabled': 0.10,
            'suspicious_chars': 0.09,
            'subdomain_count': 0.11,
            'suspicious_keywords': 0.18,  # Higher for Arabic keywords
            'ip_address': 0.13,
            'url_shortener': 0.07,
            'tld_risk': 0.09,
            'homograph_attack': 0.08,  # Higher for Arabic script mixing
            'gibberish_domain': 0.14,
            'brand_impersonation': 0.18,  # Higher for Arabic brands
            'email_routing_suspicious': 0.12,
            'noreply_mismatch': 0.10,
            'sender_name_mismatch': 0.16,  # Higher for Arabic names
            'username_suspicious': 0.12,
            'domain_suspicious': 0.14,
            'overall_email_risk': 0.16
        }

    def _feature_suspicious_keywords(self, text: str) -> float:
        """Check for Arabic phishing keywords"""
        matches = sum(1 for kw in self.suspicious_keywords if kw in text)

        if matches > 3:  # Arabic text may have more keywords
            return 1.0
        elif matches > 1:
            return matches / 4
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

        # Check vowel ratio
        vowels = 'aeiouAEIOU'
        vowel_count = sum(1 for c in domain_without_tld if c in vowels)
        total_letters = sum(1 for c in domain_without_tld if c.isalpha())

        if total_letters > 0:
            vowel_ratio = vowel_count / total_letters
            if vowel_ratio < 0.2:
                return 1.0
            elif vowel_ratio < 0.3:
                return 0.7

        # Consonant clusters
        consonant_clusters = re.findall(r'[^aeiouAEIOU]{4,}', domain_without_tld)
        if consonant_clusters:
            return 0.8

        return 0.0

    def _feature_brand_impersonation(self, domain: str, email_content: str = '') -> float:
        """Detect Arabic brand impersonation"""
        domain_lower = domain.lower()

        for brand, legitimate_domains in self.legitimate_brands.items():
            brand_mentioned = brand in email_content or brand in domain_lower

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

        try:
            email_domain = sender_email.split('@')[1] if '@' in sender_email else sender_email
        except:
            return 0.5

        free_providers = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
                         'aol.com', 'mail.com', 'protonmail.com', 'yandex.com']

        for brand, legitimate_domains in self.legitimate_brands.items():
            if brand in sender_name:
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
        Analyze email for phishing (Arabic-focused)
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

        # Generate analysis (Arabic-focused warnings)
        analysis = []
        if email_features.get('username_suspicious', 0) > 0.7:
            analysis.append("[تحذير] نمط اسم مستخدم مشبوه في البريد الإلكتروني")
        if email_features.get('domain_suspicious', 0) > 0.6:
            analysis.append("[تحذير] نطاق المرسل يحتوي على كلمات بريد مزعج")
        if email_features.get('overall_email_risk', 0) > 0.6:
            analysis.append("[تحذير] عنوان البريد يظهر خصائص البريد المزعج")
        if email_features.get('gibberish_domain', 0) > 0.6:
            analysis.append("[تحذير] نطاق المرسل يبدو عشوائياً")
        if email_features.get('brand_impersonation', 0) > 0.5:
            analysis.append("[تحذير] البريد يدعي أنه من علامة تجارية معروفة بنطاق خاطئ")
        if email_features.get('sender_name_mismatch', 0) > 0.6:
            analysis.append("[تحذير] اسم المرسل لا يطابق عنوان البريد الإلكتروني")
        if email_features.get('suspicious_keywords', 0) > 0.5:
            analysis.append("[تحذير] يحتوي على كلمات مفتاحية مرتبطة بالاحتيال")

        if not analysis:
            analysis.append("[آمن] لم يتم اكتشاف مؤشرات احتيال كبيرة")

        return {
            'is_phishing': is_phishing,
            'confidence': round(confidence, 3),
            'risk_score': round(risk_score, 2),
            'classification': classification,
            'email_features': {k: round(v, 3) for k, v in email_features.items()},
            'feature_analysis': analysis,
            'sender_domain': sender_domain,
            'language': 'arabic'
        }
