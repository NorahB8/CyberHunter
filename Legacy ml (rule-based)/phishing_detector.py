"""
CyberHunter Unified Phishing Detection System
Automatically detects language and uses the appropriate specialized model
"""

import re
from typing import Dict
from phishing_detector_english import PhishingMLModelEnglish
from phishing_detector_arabic import PhishingMLModelArabic

class PhishingMLModel:
    """
    Unified phishing detector that routes to language-specific models
    """

    def __init__(self):
        self.english_model = PhishingMLModelEnglish()
        self.arabic_model = PhishingMLModelArabic()

    def detect_language(self, text: str) -> str:
        """
        Detect if text is primarily Arabic or English
        Returns 'arabic' or 'english'
        """
        if not text:
            return 'english'

        # Count Arabic characters
        arabic_chars = len(re.findall(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]', text))

        # Count English characters
        english_chars = len(re.findall(r'[a-zA-Z]', text))

        # If more than 20% Arabic characters, consider it Arabic
        total_chars = arabic_chars + english_chars
        if total_chars > 0:
            arabic_ratio = arabic_chars / total_chars
            if arabic_ratio > 0.2:
                return 'arabic'

        return 'english'

    def analyze_email(self, sender_email: str, sender_name: str = '',
                     email_body: str = '', routing_info: str = '',
                     urls_in_email: list = None) -> Dict:
        """
        Analyze email using the appropriate language-specific model

        Args:
            sender_email: Email address of sender
            sender_name: Display name of sender
            email_body: Text content of the email
            routing_info: Email routing/via headers
            urls_in_email: List of URLs found in the email

        Returns:
            Dictionary with analysis results including detected language
        """
        # Detect language from email content
        combined_text = f"{sender_name} {email_body}"
        detected_language = self.detect_language(combined_text)

        # Route to appropriate model
        if detected_language == 'arabic':
            result = self.arabic_model.analyze_email(
                sender_email=sender_email,
                sender_name=sender_name,
                email_body=email_body,
                routing_info=routing_info
            )
            result['detected_language'] = 'arabic'
            result['model_used'] = 'arabic_specialized'
        else:
            result = self.english_model.analyze_email(
                sender_email=sender_email,
                sender_name=sender_name,
                email_body=email_body,
                routing_info=routing_info
            )
            result['detected_language'] = 'english'
            result['model_used'] = 'english_specialized'

        return result

    def get_model_info(self) -> Dict:
        """Get information about available models"""
        return {
            'available_models': ['english', 'arabic'],
            'english_keywords': len(self.english_model.suspicious_keywords),
            'arabic_keywords': len(self.arabic_model.suspicious_keywords),
            'english_brands': len(self.english_model.legitimate_brands),
            'arabic_brands': len(self.arabic_model.legitimate_brands),
            'detection_method': 'automatic_language_detection'
        }


def main():
    """Demo usage"""
    model = PhishingMLModel()

    print("=" * 80)
    print("CyberHunter Unified Phishing Detection System")
    print("=" * 80)

    # Get model info
    info = model.get_model_info()
    print(f"\nSystem Configuration:")
    print(f"  Available Models: {', '.join(info['available_models'])}")
    print(f"  English Keywords: {info['english_keywords']}")
    print(f"  Arabic Keywords: {info['arabic_keywords']}")
    print(f"  English Brands: {info['english_brands']}")
    print(f"  Arabic Brands: {info['arabic_brands']}")
    print(f"  Detection Method: {info['detection_method']}")

    # Test English email
    print("\n" + "=" * 80)
    print("Test 1: English Phishing Email")
    print("=" * 80)

    result_en = model.analyze_email(
        sender_email="label623435@494540.oceanpark.trip.entryway.giantreward.com",
        sender_name="FedEx",
        email_body="Your shipment is ready. Click here to confirm delivery address."
    )

    print(f"Detected Language: {result_en['detected_language'].upper()}")
    print(f"Model Used: {result_en['model_used']}")
    print(f"Risk Score: {result_en['risk_score']:.1f}%")
    print(f"Classification: {result_en['classification'].upper()}")
    print(f"Is Phishing: {result_en['is_phishing']}")

    # Test Arabic email
    print("\n" + "=" * 80)
    print("Test 2: Arabic Phishing Email")
    print("=" * 80)

    result_ar = model.analyze_email(
        sender_email="noreply@suspicious-domain.com",
        sender_name="DHL Express",
        email_body="تم تعليق طردك رقم معلومات مفقودة عاجل أيام عمل انقر تحقق حساب"
    )

    print(f"Detected Language: {result_ar['detected_language'].upper()}")
    print(f"Model Used: {result_ar['model_used']}")
    print(f"Risk Score: {result_ar['risk_score']:.1f}%")
    print(f"Classification: {result_ar['classification'].upper()}")
    print(f"Is Phishing: {result_ar['is_phishing']}")

    print("\n" + "=" * 80)
    print("Unified Detection System Ready")
    print("=" * 80)


if __name__ == "__main__":
    main()
