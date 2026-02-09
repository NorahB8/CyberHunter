"""
CyberHunter Training Data
Separated into URL and Email datasets
"""

# === EMAIL DATASET ===
EMAIL_TRAINING_DATA = [
    # === PHISHING EMAILS (label=1) ===

    # DHL Phishing example Gibberish domain
    {
        'sender_email': 'Noreply-SNGVOTLA@sngvotlasngvotla.ca',
        'sender_name': 'DHL Express',
        'subject': 'Parcel Notification',
        'body': 'Your parcel has been suspended. Missing information. Please verify your address to schedule delivery.',
        'label': 1,
        'category': 'shipping_scam'
    },

    # FedEx Phishing #1 - Sophisticated spam domain
    {
        'sender_email': 'label623435@494540.oceanpark.trip.entryway.giantreward.choresrecords.com',
        'sender_name': 'FedEx',
        'subject': 'Shipment Notification',
        'body': 'Your shipment is ready for delivery. Click here to confirm your address.',
        'label': 1,
        'category': 'brand_impersonation'
    },

    # FedEx Phishing #2 - Arabic mixed
    {
        'sender_email': 'label657841@540101.oceanpark.trip.entryway.giantreward.choresrecords.com',
        'sender_name': 'FedEx فيدكس',
        'subject': 'Package Delivery',
        'body': 'Your package requires verification. Update your delivery information now.',
        'label': 1,
        'category': 'brand_impersonation'
    },

    # FedEx Phishing #3 - New spam keywords
    {
        'sender_email': 'proof643380@706419.junglerealm.pathway.gatehouse.superwin.antiwalmart.com',
        'sender_name': 'FedEx Delivery',
        'subject': 'Action Required',
        'body': 'Urgent: Your shipment cannot be delivered. Missing address information. Verify now.',
        'label': 1,
        'category': 'brand_impersonation'
    },

    # PayPal Phishing - Free email provider
    {
        'sender_email': 'paypal-security@gmail.com',
        'sender_name': 'PayPal Security',
        'subject': 'Account Suspended',
        'body': 'Your PayPal account has been suspended due to suspicious activity. Verify your identity immediately.',
        'label': 1,
        'category': 'account_suspended'
    },

    # Bank Phishing - Urgency tactics
    {
        'sender_email': 'security@bank-verification.xyz',
        'sender_name': 'Chase Bank',
        'subject': 'Urgent: Verify Your Account',
        'body': 'Unauthorized access detected. Confirm your account details within 24 hours or your account will be locked.',
        'label': 1,
        'category': 'financial_threat'
    },

    # Arabic DHL Phishing
    {
        'sender_email': 'noreply@dhl-ksa-tracking.com',
        'sender_name': 'DHL Express',
        'subject': 'تنبيه شحنة',
        'body': 'تم تعليق طردك. معلومات مفقودة. يرجى التحقق من عنوانك لجدولة التسليم عاجل.',
        'label': 1,
        'category': 'shipping_scam_arabic'
    },

    # Arabic Bank Phishing
    {
        'sender_email': 'security@alrajhi-verify.com',
        'sender_name': 'الراجحي',
        'subject': 'تحذير أمني',
        'body': 'نشاط غير عادي في حسابك. يرجى تحديث معلوماتك الشخصية فوراً. آخر فرصة.',
        'label': 1,
        'category': 'bank_phishing_arabic'
    },

    # Microsoft Phishing - Account verification
    {
        'sender_email': 'noreply@microsoft-account-verify.com',
        'sender_name': 'Microsoft Account Team',
        'subject': 'Verify your Microsoft account',
        'body': 'Your Microsoft account requires verification. Click here to confirm your identity and prevent account closure.',
        'label': 1,
        'category': 'account_verification'
    },

    # Amazon Phishing - Prize scam
    {
        'sender_email': 'winner2024@amazon-prizes.top',
        'sender_name': 'Amazon Rewards',
        'subject': 'Congratulations! You won!',
        'body': 'You have been selected as a winner. Claim your free gift card now. Limited time offer.',
        'label': 1,
        'category': 'prize_scam'
    },

    # Netflix Phishing - Payment update
    {
        'sender_email': 'billing@netflix-update.club',
        'sender_name': 'Netflix',
        'subject': 'Payment Failed',
        'body': 'Your payment method failed. Update your credit card information to continue your subscription.',
        'label': 1,
        'category': 'payment_scam'
    },

    # Apple Phishing - iCloud storage
    {
        'sender_email': 'icloud-storage@apple-support.xyz',
        'sender_name': 'Apple Support',
        'subject': 'iCloud Storage Full',
        'body': 'Your iCloud storage is full. Upgrade now or your data will be deleted. Act immediately.',
        'label': 1,
        'category': 'storage_scam'
    },

    # Random spam - Gibberish username
    {
        'sender_email': 'MguTYrJq@wildzone.freezone.xyz',
        'sender_name': 'Special Offer',
        'subject': 'Claim your prize',
        'body': 'You won a prize. Click here to claim your reward today only.',
        'label': 1,
        'category': 'random_spam'
    },

    # Arabic STC Phishing
    {
        'sender_email': 'verify@stc-rewards.com',
        'sender_name': 'STC',
        'subject': 'جائزة مجانية',
        'body': 'مبروك! فزت بجائزة من STC. اضغط هنا للمطالبة بالجائزة الآن.',
        'label': 1,
        'category': 'telecom_scam_arabic'
    },

    # Google Phishing - Security alert
    {
        'sender_email': 'security-alert@google-verify.tk',
        'sender_name': 'Google Security',
        'subject': 'Security Alert',
        'body': 'Suspicious activity detected on your Google account. Verify your password immediately.',
        'label': 1,
        'category': 'security_alert_scam'
    },

    # === LEGITIMATE EMAILS (label=0) ===

    # PSU domain
    {
        'sender_email': 'noreply@psu.edu.sa',
        'sender_name': 'PSU',
        'subject': 'CS316: Announcement',
        'body': 'assignment has been posted',
        'label': 0,
        'category': 'legitimate_notification'
    },

    # Real FedEx
    {
        'sender_email': 'support@fedex.com',
        'sender_name': 'FedEx',
        'subject': 'Delivery Notification',
        'body': 'Your package will be delivered tomorrow. Track your shipment using the tracking number.',
        'label': 0,
        'category': 'legitimate_shipping'
    },

    # Real Google
    {
        'sender_email': 'no-reply@google.com',
        'sender_name': 'Google',
        'subject': 'Security Alert',
        'body': 'We noticed a new sign-in to your Google Account. If this was you, you don\'t need to do anything.',
        'label': 0,
        'category': 'legitimate_notification'
    },

    # Real Amazon
    {
        'sender_email': 'auto-confirm@amazon.com',
        'sender_name': 'Amazon.com',
        'subject': 'Your order has shipped',
        'body': 'Your order has been shipped and will arrive in 2 business days.',
        'label': 0,
        'category': 'legitimate_shipping'
    },

    # Real Microsoft
    {
        'sender_email': 'no-reply@microsoft.com',
        'sender_name': 'Microsoft Account Team',
        'subject': 'Microsoft account activity',
        'body': 'Recent activity on your Microsoft account. Review your recent sign-in activity.',
        'label': 0,
        'category': 'legitimate_notification'
    },

    # Real PayPal
    {
        'sender_email': 'service@paypal.com',
        'sender_name': 'PayPal',
        'subject': 'Receipt for your payment',
        'body': 'You sent a payment. Thank you for using PayPal.',
        'label': 0,
        'category': 'legitimate_receipt'
    },

    # Real DHL
    {
        'sender_email': 'noreply@dhl.com',
        'sender_name': 'DHL',
        'subject': 'Shipment notification',
        'body': 'Your shipment is on the way. Estimated delivery date.',
        'label': 0,
        'category': 'legitimate_shipping'
    },

    # Real Apple
    {
        'sender_email': 'no_reply@email.apple.com',
        'sender_name': 'Apple',
        'subject': 'Your receipt from Apple',
        'body': 'Thank you for your purchase from the App Store.',
        'label': 0,
        'category': 'legitimate_receipt'
    },

    # Real Netflix
    {
        'sender_email': 'info@mailer.netflix.com',
        'sender_name': 'Netflix',
        'subject': 'What to watch this weekend',
        'body': 'Check out these new releases on Netflix.',
        'label': 0,
        'category': 'legitimate_marketing'
    },

    # Real Arabic Bank - Al Rajhi
    {
        'sender_email': 'noreply@alrajhibank.com.sa',
        'sender_name': 'مصرف الراجحي',
        'subject': 'كشف حساب شهري',
        'body': 'كشف الحساب الشهري متاح الآن. يمكنك مراجعته من خلال تطبيق الراجحي.',
        'label': 0,
        'category': 'legitimate_bank_arabic'
    },

    # Real STC
    {
        'sender_email': 'noreply@stc.com.sa',
        'sender_name': 'STC',
        'subject': 'فاتورة STC',
        'body': 'فاتورتك الشهرية جاهزة. يمكنك عرضها من خلال تطبيق mystc.',
        'label': 0,
        'category': 'legitimate_telecom_arabic'
    },

    # Real GitHub
    {
        'sender_email': 'noreply@github.com',
        'sender_name': 'GitHub',
        'subject': 'Your pull request was merged',
        'body': 'Your pull request has been successfully merged into the main branch.',
        'label': 0,
        'category': 'legitimate_notification'
    },

    # Real LinkedIn
    {
        'sender_email': 'messages-noreply@linkedin.com',
        'sender_name': 'LinkedIn',
        'subject': 'You have a new message',
        'body': 'You have received a new message from your connection.',
        'label': 0,
        'category': 'legitimate_social'
    },

    # Real Bank - Chase
    {
        'sender_email': 'no.reply.alerts@chase.com',
        'sender_name': 'Chase',
        'subject': 'Your Chase statement is ready',
        'body': 'Your monthly statement is now available. View it online or in the Chase mobile app.',
        'label': 0,
        'category': 'legitimate_bank'
    },
]


# === URL DATASET ===
URL_TRAINING_DATA = [
    # === PHISHING URLS (label=1) ===

    # Cloud Storage Abuse - Phishing page on Google Cloud Storage
    {
        'sender_email': 'https://storage.googleapis.com/jawdlock2/hreflyjaw.html#?Z289MSZzMT0yMjM2OTE2JnMyPTUxMjA2NDYzOCZzMz1HTEI=',
        'sender_name': 'Account Verification',
        'subject': 'Verify Your Account',
        'body': 'Click here to verify your account information. This link expires in 24 hours.',
        'label': 1,
        'category': 'cloud_storage_abuse'
    },

    # Typosquatting URL
    {
        'sender_email': 'http://paypa1-security-verify.tk/login',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 1,
        'category': 'typosquatting_url'
    },

    # Brand in subdomain
    {
        'sender_email': 'http://paypal.evil-site.xyz/secure/login',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 1,
        'category': 'brand_subdomain_phishing'
    },

    # IP address URL
    {
        'sender_email': 'http://192.168.1.100/paypal/verify',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 1,
        'category': 'ip_address_phishing'
    },

    # Credential attack URL (@ in URL)
    {
        'sender_email': 'http://google.com@evil-site.com/login',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 1,
        'category': 'credential_attack_url'
    },

    # Suspicious TLD URL
    {
        'sender_email': 'http://account-verify-secure.xyz/update',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 1,
        'category': 'suspicious_tld_url'
    },

    # Long suspicious URL with many hyphens
    {
        'sender_email': 'http://secure-login-verify-account-update-confirm.tk/auth',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 1,
        'category': 'long_suspicious_url'
    },

    # === LEGITIMATE URLS (label=0) ===

    {
        'sender_email': 'https://www.google.com',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 0,
        'category': 'legitimate_url'
    },
    {
        'sender_email': 'https://www.amazon.com/gp/product/B08N5WRWNW',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 0,
        'category': 'legitimate_url'
    },
    {
        'sender_email': 'https://github.com/anthropics/claude-code',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 0,
        'category': 'legitimate_url'
    },
    {
        'sender_email': 'https://support.apple.com/en-us/HT201222',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 0,
        'category': 'legitimate_url'
    },
    {
        'sender_email': 'https://www.paypal.com/myaccount/summary',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 0,
        'category': 'legitimate_url'
    },
    {
        'sender_email': 'https://www.microsoft.com/en-us/windows',
        'sender_name': '',
        'subject': '',
        'body': '',
        'label': 0,
        'category': 'legitimate_url'
    },
]


# Combined dataset for training (used by train_model.py)
TRAINING_DATA = EMAIL_TRAINING_DATA + URL_TRAINING_DATA


# Statistics
def get_stats():
    total = len(TRAINING_DATA)
    phishing = sum(1 for d in TRAINING_DATA if d['label'] == 1)
    legitimate = sum(1 for d in TRAINING_DATA if d['label'] == 0)

    return {
        'total': total,
        'phishing': phishing,
        'legitimate': legitimate,
        'balance': f"{phishing}/{legitimate} ({phishing/total*100:.1f}% phishing)"
    }


def get_email_stats():
    total = len(EMAIL_TRAINING_DATA)
    phishing = sum(1 for d in EMAIL_TRAINING_DATA if d['label'] == 1)
    legitimate = sum(1 for d in EMAIL_TRAINING_DATA if d['label'] == 0)

    return {
        'total': total,
        'phishing': phishing,
        'legitimate': legitimate,
        'balance': f"{phishing}/{legitimate} ({phishing/total*100:.1f}% phishing)"
    }


def get_url_stats():
    total = len(URL_TRAINING_DATA)
    phishing = sum(1 for d in URL_TRAINING_DATA if d['label'] == 1)
    legitimate = sum(1 for d in URL_TRAINING_DATA if d['label'] == 0)

    return {
        'total': total,
        'phishing': phishing,
        'legitimate': legitimate,
        'balance': f"{phishing}/{legitimate} ({phishing/total*100:.1f}% phishing)"
    }


if __name__ == '__main__':
    print("=" * 50)
    print("Training Data Statistics")
    print("=" * 50)

    email_stats = get_email_stats()
    print(f"\nEmail Dataset:")
    print(f"  Total samples: {email_stats['total']}")
    print(f"  Phishing: {email_stats['phishing']}")
    print(f"  Legitimate: {email_stats['legitimate']}")
    print(f"  Balance: {email_stats['balance']}")

    url_stats = get_url_stats()
    print(f"\nURL Dataset:")
    print(f"  Total samples: {url_stats['total']}")
    print(f"  Phishing: {url_stats['phishing']}")
    print(f"  Legitimate: {url_stats['legitimate']}")
    print(f"  Balance: {url_stats['balance']}")

    stats = get_stats()
    print(f"\nCombined (used for training):")
    print(f"  Total samples: {stats['total']}")
    print(f"  Phishing: {stats['phishing']}")
    print(f"  Legitimate: {stats['legitimate']}")
    print(f"  Balance: {stats['balance']}")
