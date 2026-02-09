"""
Test the trained ML model on real examples
"""

from phishing_detector_ml import PhishingMLDetector

# Test cases
test_cases = [
    {
        'name': 'FedEx Phishing #1 (Sophisticated Spam)',
        'email': 'label623435@494540.oceanpark.trip.entryway.giantreward.choresrecords.com',
        'sender': 'FedEx',
        'body': 'Your shipment is ready for delivery. Click here to confirm.',
        'expected': 'high_risk'
    },
    {
        'name': 'FedEx Phishing #2 (Arabic Mixed)',
        'email': 'label657841@540101.oceanpark.trip.entryway.giantreward.choresrecords.com',
        'sender': 'FedEx فيدكس',
        'body': 'Your package requires verification. Update delivery information now.',
        'expected': 'high_risk'
    },
    {
        'name': 'DHL Phishing (Gibberish Domain)',
        'email': 'Noreply-SNGVOTLA@sngvotlasngvotla.ca',
        'sender': 'DHL Express',
        'body': 'Your parcel has been suspended. Missing information. Verify your address.',
        'expected': 'high_risk'
    },
    {
        'name': 'PayPal Phishing (Free Email)',
        'email': 'paypal-security@gmail.com',
        'sender': 'PayPal Security',
        'body': 'Your PayPal account suspended. Verify identity immediately.',
        'expected': 'high_risk'
    },
    {
        'name': 'Legitimate - FedEx',
        'email': 'support@fedex.com',
        'sender': 'FedEx',
        'body': 'Your package will be delivered tomorrow. Track your shipment.',
        'expected': 'low_risk'
    },
    {
        'name': 'Legitimate - Google',
        'email': 'no-reply@google.com',
        'sender': 'Google',
        'body': 'New sign-in to your account. If this was you, no action needed.',
        'expected': 'low_risk'
    },
    {
        'name': 'Legitimate - Amazon',
        'email': 'auto-confirm@amazon.com',
        'sender': 'Amazon.com',
        'body': 'Your order has shipped and will arrive in 2 days.',
        'expected': 'low_risk'
    },
]

def run_tests():
    print("=" * 90)
    print("CyberHunter ML Model - Test Suite")
    print("=" * 90)

    try:
        detector = PhishingMLDetector()
    except FileNotFoundError:
        print("\nError: Model not trained yet!")
        print("Please run: python train_model.py")
        return

    print("\n" + "=" * 90)
    print("Running Tests")
    print("=" * 90)

    passed = 0
    failed = 0

    for test in test_cases:
        print(f"\n{'-' * 90}")
        print(f"Test: {test['name']}")
        print(f"Email: {test['email']}")
        print(f"Expected: {test['expected'].upper()}")
        print(f"{'-' * 90}")

        result = detector.analyze_email(
            sender_email=test['email'],
            sender_name=test['sender'],
            email_body=test['body']
        )

        print(f"\nResult:")
        print(f"  Risk Score: {result['risk_score']}%")
        print(f"  Classification: {result['classification'].upper()}")
        print(f"  Is Phishing: {result['is_phishing']}")
        print(f"  Confidence: {result['confidence'] * 100:.1f}%")
        print(f"  Model Type: {result['model_type']}")

        print(f"\nAnalysis:")
        for item in result['feature_analysis']:
            print(f"  {item}")

        # Check if prediction matches expected
        if result['classification'] == test['expected']:
            print(f"\n  PASS")
            passed += 1
        else:
            print(f"\n  FAIL - Expected {test['expected']}, got {result['classification']}")
            failed += 1

    # Summary
    print("\n" + "=" * 90)
    print("Test Summary")
    print("=" * 90)
    print(f"Total Tests: {len(test_cases)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Success Rate: {passed / len(test_cases) * 100:.1f}%")

    # Show feature importance
    print("\n" + "=" * 90)
    print("Top 10 Most Important Features (Learned by ML)")
    print("=" * 90)
    top_features = detector.get_feature_importance(10)
    for i, (feature, importance) in enumerate(top_features, 1):
        print(f"  {i:2d}. {feature:30s} {importance:.4f}")

    print("\n" + "=" * 90)


if __name__ == '__main__':
    run_tests()
