"""Test Google storage URL feature detection"""
from feature_extractor import FeatureExtractor

extractor = FeatureExtractor()

url = 'https://storage.googleapis.com/jawdlock2/hreflyjaw.html#?Z289MSZzMT0yMjM2OTE2JnMyPTUxMjA2NDYzOCZzMz1HTEI='

email_data = {
    'sender_email': url,
    'sender_name': '',
    'subject': '',
    'body': ''
}

print("Testing Google Storage URL")
print("="*70)
print(f"URL: {url}")
print("\nExtracted Features:")

features = extractor.extract_features(email_data)

# Show only non-zero features
for feature, value in features.items():
    if value > 0 and value != 0.4:  # Exclude default vowel ratio
        print(f"  {feature:30} = {value}")

print("\nKey Findings:")
print(f"  Domain length: {features['domain_length']}")
print(f"  Typosquatting: {features['typosquatting']}")
print(f"  Gibberish score: {features['gibberish_score']}")
print(f"  Domain spam keywords: {features['domain_spam_keywords']}")
