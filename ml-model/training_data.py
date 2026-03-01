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
        'category': 'shipping_scam'
    },

    # Arabic Bank Phishing
    {
        'sender_email': 'security@alrajhi-verify.com',
        'sender_name': 'الراجحي',
        'subject': 'تحذير أمني',
        'body': 'نشاط غير عادي في حسابك. يرجى تحديث معلوماتك الشخصية فوراً. آخر فرصة.',
        'label': 1,
        'category': 'bank_phishing'
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
        'category': 'telecom_scam'
    },

    # Google Phishing - Security alert
    {
        'sender_email': 'security-alert@google-verify.tk',
        'sender_name': 'Google Security',
        'subject': 'Security Alert',
        'body': 'Suspicious activity detected on your Google account. Verify your password immediately.',
        'label': 1,
        'category': 'security_alert'
    },

    # === LEGITIMATE EMAILS (label=0) ===

    # PSU domain
    {
        'sender_email': 'noreply@psu.edu.sa',
        'sender_name': 'PSU',
        'subject': 'CS316: Announcement',
        'body': 'assignment has been posted',
        'label': 0,
        'category': 'legitimate'
    },

    # Real FedEx
    {
        'sender_email': 'support@fedex.com',
        'sender_name': 'FedEx',
        'subject': 'Delivery Notification',
        'body': 'Your package will be delivered tomorrow. Track your shipment using the tracking number.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real Google
    {
        'sender_email': 'no-reply@google.com',
        'sender_name': 'Google',
        'subject': 'Security Alert',
        'body': 'We noticed a new sign-in to your Google Account. If this was you, you don\'t need to do anything.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real Amazon
    {
        'sender_email': 'auto-confirm@amazon.com',
        'sender_name': 'Amazon.com',
        'subject': 'Your order has shipped',
        'body': 'Your order has been shipped and will arrive in 2 business days.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real Microsoft
    {
        'sender_email': 'no-reply@microsoft.com',
        'sender_name': 'Microsoft Account Team',
        'subject': 'Microsoft account activity',
        'body': 'Recent activity on your Microsoft account. Review your recent sign-in activity.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real PayPal
    {
        'sender_email': 'service@paypal.com',
        'sender_name': 'PayPal',
        'subject': 'Receipt for your payment',
        'body': 'You sent a payment. Thank you for using PayPal.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real DHL
    {
        'sender_email': 'noreply@dhl.com',
        'sender_name': 'DHL',
        'subject': 'Shipment notification',
        'body': 'Your shipment is on the way. Estimated delivery date.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real Apple
    {
        'sender_email': 'no_reply@email.apple.com',
        'sender_name': 'Apple',
        'subject': 'Your receipt from Apple',
        'body': 'Thank you for your purchase from the App Store.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real Netflix
    {
        'sender_email': 'info@mailer.netflix.com',
        'sender_name': 'Netflix',
        'subject': 'What to watch this weekend',
        'body': 'Check out these new releases on Netflix.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real Arabic Bank - Al Rajhi
    {
        'sender_email': 'noreply@alrajhibank.com.sa',
        'sender_name': 'مصرف الراجحي',
        'subject': 'كشف حساب شهري',
        'body': 'كشف الحساب الشهري متاح الآن. يمكنك مراجعته من خلال تطبيق الراجحي.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real STC
    {
        'sender_email': 'noreply@stc.com.sa',
        'sender_name': 'STC',
        'subject': 'فاتورة STC',
        'body': 'فاتورتك الشهرية جاهزة. يمكنك عرضها من خلال تطبيق mystc.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real GitHub
    {
        'sender_email': 'noreply@github.com',
        'sender_name': 'GitHub',
        'subject': 'Your pull request was merged',
        'body': 'Your pull request has been successfully merged into the main branch.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real LinkedIn
    {
        'sender_email': 'messages-noreply@linkedin.com',
        'sender_name': 'LinkedIn',
        'subject': 'You have a new message',
        'body': 'You have received a new message from your connection.',
        'label': 0,
        'category': 'legitimate'
    },

    # Real Bank - Chase
    {
        'sender_email': 'no.reply.alerts@chase.com',
        'sender_name': 'Chase',
        'subject': 'Your Chase statement is ready',
        'body': 'Your monthly statement is now available. View it online or in the Chase mobile app.',
        'label': 0,
        'category': 'legitimate'
    },

    # Sephora marketing email
    {
        'sender_email': 'info@communication.sephora-info-me.com',
        'sender_name': 'SEPHORA',
        'subject': 'Discover Mongoliese now at Sephora',
        'body': 'A complete set for face and lips with a natural glow.',
        'label': 0,
        'category': 'legitimate'
    },

    # L'Occitane marketing email
    {
        'sender_email': 'newsletters@email-loccitane.com',
        'sender_name': "L'Occitane En Provence",
        'subject': 'New arrivals just for you',
        'body': 'Discover our latest skincare collection.',
        'label': 0,
        'category': 'legitimate'
    },

    # Phishing - Western name from Japanese ISP domain (generic)
    {
        'sender_email': 'nenkin.hyogo@ruby.plala.or.jp',
        'sender_name': 'Charles Koch',
        'subject': 'Important business proposal',
        'body': 'I have a business proposal for you regarding an investment opportunity.',
        'label': 1,
        'category': 'name_domain_mismatch'
    },

    # Phishing - Donation/inheritance scam from Japanese ISP
    {
        'sender_email': 'nenkin.hyogo@ruby.plala.or.jp',
        'sender_name': 'Charles Koch',
        'subject': 'DONATION NOTICE.REF:MDD9926',
        'body': 'This is to inform you that my late brother strongly believed in giving while living and decided to give USD2,000,000.00 Million Dollars to randomly selected individuals worldwide. On receipt of this email you should count yourself as the lucky individual.',
        'label': 1,
        'category': 'donation_scam'
    },
]


# === URL DATASET ===
URL_TRAINING_DATA = [
    # === PHISHING URLS (label=1) ===

    # Cloud Storage Abuse - Phishing page on Google Cloud Storage
    {
        'url': 'https://storage.googleapis.com/jawdlock2/hreflyjaw.html#?Z289MSZzMT0yMjM2OTE2JnMyPTUxMjA2NDYzOCZzMz1HTEI=',
        'label': 1,
        'category': 'cloud_hosted_phishing'
    },

    # Typosquatting - PayPal
    {
        'url': 'http://paypa1-security-verify.tk/login',
        'label': 1,
        'category': 'typosquatting'
    },

    # Typosquatting - eBay (a→4)
    {
        'url': 'http://eb4y.com',
        'label': 1,
        'category': 'typosquatting'
    },

    # Typosquatting - eBay (a→ai)
    {
        'url': 'http://ebai.com',
        'label': 1,
        'category': 'typosquatting'
    },

    # Typosquatting - eBay (e→3)
    {
        'url': 'http://3bay.com',
        'label': 1,
        'category': 'typosquatting'
    },

    # Typosquatting - Sephora 
    {
        'url': 'http://seph0ra.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://sephura.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://sephoora.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://sephu0ra.com',
        'label': 1,
        'category': 'typosquatting'
    },

    {
        'url': 'http://seph1ra.com',
        'label': 1,
        'category': 'typosquatting'
    },

    {
        'url': 'http://seph6ra.com',
        'label': 1,
        'category': 'typosquatting'
    },

    # Typosquatting - Netflix 
    {
        'url': 'http://netfl1x.com',
        'label': 1,
        'category': 'typosquatting'
    },

    {
        'url': 'http://netf1ix.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://neetf1ix.com',
        'label': 1,
        'category': 'typosquatting'
    },
{
        'url': 'http://ne1f1ix.com',
        'label': 1,
        'category': 'typosquatting'
    },
    # Typosquatting - Apple 
    {
        'url': 'http://appl3.com',
        'label': 1,
        'category': 'typosquatting'
    },

    {
        'url': 'http://app1e.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://appl1e.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://4pple.com',
        'label': 1,
        'category': 'typosquatting'
    },

    # Typosquatting - Amazon 
    {
        'url': 'http://4mazon.com',
        'label': 1,
        'category': 'typosquatting'
    },

    {
        'url': 'http://amaz0n.com',
        'label': 1,
        'category': 'typosquatting'
    },
{
        'url': 'http://4maz0n.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://amaz0on.com',
        'label': 1,
        'category': 'typosquatting'
    },
    # Typosquatting - DHL 
    {
        'url': 'http://dh1.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://dhi.com',
        'label': 1,
        'category': 'typosquatting'
    },
    {
        'url': 'http://dh1l.com',
        'label': 1,
        'category': 'typosquatting'
    },

    # Typosquatting - FedEx 
    {
        'url': 'http://f3dex.com',
        'label': 1,
        'category': 'typosquatting'
    },

    {
        'url': 'http://f3d3x.com',
        'label': 1,
        'category': 'typosquatting'
    },
     

    # IP address URL
    {
        'url': 'http://192.168.1.100/paypal/verify',
        'label': 1,
        'category': 'ip_address'
    },

    # Credential attack URL (@ in URL)
    {
        'url': 'http://google.com@evil-site.com/login',
        'label': 1,
        'category': 'credential_attack'
    },

    # Suspicious TLD URL
    {
        'url': 'http://account-verify-secure.xyz/update',
        'label': 1,
        'category': 'suspicious_tld'
    },

    # Long suspicious URL with many hyphens
    {
        'url': 'http://secure-login-verify-account-update-confirm.tk/auth',
        'label': 1,
        'category': 'long_suspicious'
    },

    # PayPal Phishing URLs 
    {
        'url': 'http://paypa1-login-security.com/verify',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://paypal.account-update-secure.xyz/login',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://secure-paypal.evil-domain.ru/auth',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://login-paypal-confirm.netlify.app',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://paypal.verify-user-access.tk',
        'label': 1, 'category': 'brand_subdomain'
    },
    {   'url': 'http://paypal.evil-site.xyz/secure/login',
        'label': 1,
        'category': 'brand_subdomain'
    },
    {
        'url': 'http://secure-paypaI-reset-password.xyz/login',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://paypal-warning-user-confirm.top/auth',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://paypal-security-team-alert.help/verify',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://paypa1-account-check.ga/login',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://paypal-login-session-expired.ru/auth',
        'label': 1, 'category': 'suspicious_tld'
    },

    # Amazon Phishing URLs
    {
        'url': 'http://amaz0n-security-check.com/update',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://amazon.login-alert.xyz/confirm',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://secure-amazon-payment.ga/verify',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://amazon.account-locked.help/login',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://amazon.customer.verify-now.top',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://amaz0n-order-problem-confirm.xyz/update',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://amazon-security-team-alert.top/login',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://amazon-user-verification.help/auth',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://secure-amazon-session-warning.ga/verify',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://amazon-login-unusual-activity.ru/check',
        'label': 1, 'category': 'suspicious_tld'
    },

    #Microsoft Phishing URLs
    {
        'url': 'http://micr0soft-account-security.com/login',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://microsoft.verify-session.xyz/auth',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://secure-microsoft-alert.ga/reset',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://office365-login-confirm.ru/secure',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://microsoft-authentication-warning.top',
        'label': 1, 'category': 'suspicious_tld'
    },{
        'url': 'http://micros0ft-account-warning.xyz/reset',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://microsoft-session-expired.top/login',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://secure-office365-confirm.help/auth',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://office-login-security-alert.ga/reset',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://microsoft-user-verification.ru/login',
        'label': 1, 'category': 'suspicious_tld'
    },


    # Google Phishing URLs 
    {
        'url': 'http://goog1e-account-recovery.com/signin',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://google.security-check-alert.xyz/login',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://accounts-google.verify-user.net/auth',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://google-auth-reset-password.help',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://drive-google-secure-access.top',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://goog1e-login-suspicious-activity.xyz/auth',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://google-account-warning.top/verify',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://secure-google-confirm-session.help/reset',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://google-user-authentication.ga/login',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://google-password-reset-alert.ru/auth',
        'label': 1, 'category': 'suspicious_tld'
    },


    #Facebook Phishing URLs
    {
        'url': 'http://faceb00k-security-alert.com/login',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://faceb00k',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://faceb0ok',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://f4ceb0ok',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://facebook.verify-session.xyz/auth',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://secure-facebook-warning.ga/confirm',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://facebook-login-check.help/reset',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://fb-account-protection.top',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://faceb00k-login-confirm.xyz/security',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://facebook-session-warning.top/reset',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://secure-facebook-user-check.help/login',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://facebook-authentication-required.ga/verify',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://facebook-password-alert.ru/reset',
        'label': 1, 'category': 'suspicious_tld'
    },

    # Banking Phishing URLs 
    {
        'url': 'http://bank-secure-login-update.xyz/auth',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://chase.verify-account-alert.ru/login',
        'label': 1, 'category': 'brand_subdomain'
    },
    {
        'url': 'http://secure-bank-authentication.ga/verify',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://account-warning-bank.top/update',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://bank-login-confirm.help',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://bank-account-security-warning.xyz/login',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://secure-onlinebank-confirm.top/auth',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://bank-session-expired.help/verify',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://bank-login-alert.ga/reset',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://bank-user-check-required.ru/auth',
        'label': 1, 'category': 'suspicious_tld'
    },

    # Shipping/Courier Phishing URLs
    {
        'url': 'http://dhl-tracking-confirmation.xyz/update',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://fedex-delivery-problem.top/verify',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://ups-shipping-alert.ga/confirm',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://package-delivery-missing-info.help',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://courier-tracking-warning.ru/check',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://dhl-delivery-problem-confirm.xyz/track',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://fedex-address-verification.top/update',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://ups-shipping-session.help/confirm',
        'label': 1, 'category': 'suspicious_keywords'
    },
    {
        'url': 'http://courier-delivery-warning.ga/verify',
        'label': 1, 'category': 'suspicious_tld'
    },
    {
        'url': 'http://parcel-redelivery-alert.ru/check',
        'label': 1, 'category': 'suspicious_tld'
    },

    # IP Address Phishing URLs
    {
        'url': 'http://192.168.0.55/paypal/login',
        'label': 1, 'category': 'ip_address'
    },
    {
        'url': 'http://45.88.120.3/secure-bank/auth',
        'label': 1, 'category': 'ip_address'
    },
    {
        'url': 'http://103.21.244.1/google/verify',
        'label': 1, 'category': 'ip_address'
    },
    {
        'url': 'http://172.16.5.44/bank/login',
        'label': 1, 'category': 'ip_address'
    },
    {
        'url': 'http://88.214.193.17/google/auth',
        'label': 1, 'category': 'ip_address'
    },
    {
        'url': 'http://31.13.77.102/facebook/security',
        'label': 1, 'category': 'ip_address'
    },

    # Credential Attack URLs (@ in URL) 
    {
        'url': 'http://google.com@evil-site.xyz/login',
        'label': 1, 'category': 'credential_attack'
    },
    {
        'url': 'http://paypal.com@phish-domain.ru/auth',
        'label': 1, 'category': 'credential_attack'
    },
    {
        'url': 'http://amazon.com@malicious-site.top/signin',
        'label': 1, 'category': 'credential_attack'
    },
    {
        'url': 'http://paypal.com@secure-authenticate.xyz/login',
        'label': 1, 'category': 'credential_attack'
    },
    {
        'url': 'http://google.com@account-warning.top/auth',
        'label': 1, 'category': 'credential_attack'
    },
    {
        'url': 'http://amazon.com@session-check.help/login',
        'label': 1, 'category': 'credential_attack'
    },
    {
        'url': 'http://microsoft.com@verify-user.ga/auth',
        'label': 1, 'category': 'credential_attack'
    },
    {
        'url': 'http://bank.com@security-alert.ru/login',
        'label': 1, 'category': 'credential_attack'
    },

    #Long Suspicious URLs
    {
        'url': 'http://important-security-notice-login.xyz/secure',
        'label': 1, 'category': 'long_suspicious'
    },
    {
        'url': 'http://user-verification-required-now.top/login',
        'label': 1, 'category': 'long_suspicious'
    },
    {
        'url': 'http://account-suspension-warning.ga/auth',
        'label': 1, 'category': 'long_suspicious'
    },
    {
        'url': 'http://last-chance-account-verify.help/login',
        'label': 1, 'category': 'long_suspicious'
    },
    {
        'url': 'http://secure-login-confirm-user-account-update.xyz/auth',
        'label': 1, 'category': 'long_suspicious'
    },
    {
        'url': 'http://important-account-warning-reset.top/login',
        'label': 1, 'category': 'long_suspicious'
    },
    {
        'url': 'http://last-notice-user-verification.help/auth',
        'label': 1, 'category': 'long_suspicious'
    },
    {
        'url': 'http://urgent-security-confirmation.ga/reset',
        'label': 1, 'category': 'long_suspicious'
    },
    {
        'url': 'http://final-account-check-required.ru/login',
        'label': 1, 'category': 'long_suspicious'
    },

    #Sephora Phishing URL
    {
        'url': 'http://s0ephora1.com',
        'label': 1, 'category': 'typosquatting'
    },
    {
        'url': 'http://sephora.us@advent2025.com',
        'label': 1, 'category': 'special_characters'
    },

    

    # --- Cloud-Hosted Phishing (legitimate services abused) ---
    {
        'url': 'https://storage.googleapis.com/jawdlock2/hreflyjaw.html#?Z289MSZzMT0yMjM2OTE2JnMyPTUxMjA2NDYzOCZzMz1HTEI=',
        'label': 1, 'category': 'cloud_hosted_phishing'
    },

    # REAL URLS (label=0) 

    {
        'url': 'https://www.google.com',
        'label': 0,
        'category': 'legitimate'
    },
    {
        'url': 'https://www.amazon.com/gp/product/B08N5WRWNW',
        'label': 0,
        'category': 'legitimate'
    },
    {
        'url': 'https://github.com/anthropics/claude-code',
        'label': 0,
        'category': 'legitimate'
    },
    {
        'url': 'https://support.apple.com/en-us/HT201222',
        'label': 0,
        'category': 'legitimate'
    },
    {
        'url': 'https://www.paypal.com/myaccount/summary',
        'label': 0,
        'category': 'legitimate'
    },
    {
        'url': 'https://www.microsoft.com/en-us/windows',
        'label': 0,
        'category': 'legitimate'
    },

    # Google
    {
        'url': 'https://mail.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://drive.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://maps.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://accounts.google.com/signin',
        'label': 0, 'category': 'legitimate'
    },

    #Amazon
    {
        'url': 'https://www.amazon.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.amazon.com/orders',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.amazon.com/gp/help/customer/display.html',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://sellercentral.amazon.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://music.amazon.com',
        'label': 0, 'category': 'legitimate'
    },

    #Microsoft
    {
        'url': 'https://www.microsoft.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://account.microsoft.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://login.live.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://support.microsoft.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://portal.office.com',
        'label': 0, 'category': 'legitimate'
    },

    # PayPal
    {
        'url': 'https://www.paypal.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.paypal.com/signin',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://developer.paypal.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.paypal.com/us/webapps/mpp/home',
        'label': 0, 'category': 'legitimate'
    },

    # GitHub 
    {
        'url': 'https://github.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://github.com/login',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://docs.github.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://api.github.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://github.com/features',
        'label': 0, 'category': 'legitimate'
    },

    # Other Tech
    {
        'url': 'https://stackoverflow.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://stackoverflow.com/questions',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://chat.openai.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://openai.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://platform.openai.com/docs',
        'label': 0, 'category': 'legitimate'
    },

    # Apple
    {
        'url': 'https://www.apple.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://developer.apple.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.icloud.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://apps.apple.com',
        'label': 0, 'category': 'legitimate'
    },

    # Entertainment & Social
    {
        'url': 'https://www.netflix.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://help.netflix.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.ebay.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.ebay.com/help/home',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.ebay.com/sh/ovw',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.linkedin.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://twitter.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.youtube.com',
        'label': 0, 'category': 'legitimate'
    },

    # News & Education 
    {
        'url': 'https://www.wikipedia.org',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.bbc.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.nytimes.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.coursera.org',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.udemy.com',
        'label': 0, 'category': 'legitimate'
    },

    # Sephora 
    {
        'url': 'https://sephora.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.sephora.sa',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://t10.communication.sephora-info-fr.com/r/?id=h26a4148c',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://t10.communication.sephora-info-me.com/r/?id=example',
        'label': 0, 'category': 'legitimate'
    },

    # More Google 
    {
        'url': 'https://www.google.com/search?q=machine+learning',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://news.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://calendar.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://translate.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://photos.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://meet.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://contacts.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://fonts.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://earth.google.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://store.google.com',
        'label': 0, 'category': 'legitimate'
    },

    #More Amazon
    {
        'url': 'https://www.amazon.com/gp/cart/view.html',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.amazon.com/gp/your-account/order-history',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.amazon.com/prime',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.amazon.com/music',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.amazon.com/kindle-dbs/storefront',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://advertising.amazon.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://aws.amazon.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://docs.aws.amazon.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://console.aws.amazon.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://status.aws.amazon.com',
        'label': 0, 'category': 'legitimate'
    },

    #More Microsoft 
    {
        'url': 'https://support.microsoft.com/en-us',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://learn.microsoft.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://visualstudio.microsoft.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://azure.microsoft.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://portal.azure.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://dev.azure.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://outlook.live.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://onedrive.live.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://bing.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://microsoftedge.microsoft.com',
        'label': 0, 'category': 'legitimate'
    },

    # More PayPal
    {
        'url': 'https://www.paypal.com/us/signin',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.paypal.com/us/smarthelp/home',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.paypal.com/us/webapps/mpp/send-money-online',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.paypal.com/us/business',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.paypal.com/us/security',
        'label': 0, 'category': 'legitimate'
    },

    # More GitHub
    {
        'url': 'https://github.com/explore',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://github.com/trending',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://github.com/marketplace',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://docs.github.com/en/get-started',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://education.github.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://status.github.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://gist.github.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://pages.github.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://cli.github.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://api.github.com/repos',
        'label': 0, 'category': 'legitimate'
    },

    #StackOverflow & StackExchange
    {
        'url': 'https://stackoverflow.com/tags',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://stackoverflow.com/jobs',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://superuser.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://serverfault.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://stackapps.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://stackexchange.com',
        'label': 0, 'category': 'legitimate'
    },

    #OpenAI
    {
        'url': 'https://openai.com/research',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://openai.com/blog',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://platform.openai.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://platform.openai.com/playground',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://help.openai.com',
        'label': 0, 'category': 'legitimate'
    },

    # Apple
    {
        'url': 'https://www.apple.com/iphone',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.apple.com/mac',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.apple.com/ipad',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.apple.com/watch',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.apple.com/services',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://support.apple.com/iphone',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://support.apple.com/mac',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://developer.apple.com/xcode',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://developer.apple.com/swift',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.icloud.com/mail',
        'label': 0, 'category': 'legitimate'
    },

    #More Netflix
    {
        'url': 'https://www.netflix.com/browse',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.netflix.com/latest',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://help.netflix.com/en/node/412',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://jobs.netflix.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://media.netflix.com',
        'label': 0, 'category': 'legitimate'
    },

    #More LinkedIn
    {
        'url': 'https://www.linkedin.com/feed',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.linkedin.com/jobs',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.linkedin.com/learning',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://business.linkedin.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://engineering.linkedin.com',
        'label': 0, 'category': 'legitimate'
    },

    # Twitter
    {
        'url': 'https://twitter.com/home',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://twitter.com/explore',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://twitter.com/settings/account',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://help.twitter.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://developer.twitter.com',
        'label': 0, 'category': 'legitimate'
    },

    #YouTube
    {
        'url': 'https://www.youtube.com/feed/subscriptions',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.youtube.com/results?search_query=python',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://studio.youtube.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://music.youtube.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://support.google.com/youtube',
        'label': 0, 'category': 'legitimate'
    },

    #  Wikipedia 
    {
        'url': 'https://www.wikipedia.org/wiki/Artificial_intelligence',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://en.wikipedia.org/wiki/Machine_learning',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://en.wikipedia.org/wiki/Phishing',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://commons.wikimedia.org',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://meta.wikimedia.org',
        'label': 0, 'category': 'legitimate'
    },

    # News 
    {
        'url': 'https://www.bbc.com/news',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.bbc.com/sport',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.cnn.com/world',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.reuters.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.aljazeera.com',
        'label': 0, 'category': 'legitimate'
    },

    #Education
    {
        'url': 'https://www.coursera.org/learn/machine-learning',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.coursera.org/professional-certificates',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.edx.org/course',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.udemy.com/course/python-for-beginners',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.udacity.com/course',
        'label': 0, 'category': 'legitimate'
    },

    {
        'url': 'https://www.nytimes.com/section/technology',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.theguardian.com/international',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.forbes.com/technology',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.bloomberg.com/markets',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://techcrunch.com',
        'label': 0, 'category': 'legitimate'
    },

    #Cloud Storage
    {
        'url': 'https://www.dropbox.com/login',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.dropbox.com/home',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.dropbox.com/business',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.box.com/home',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://drive.dropbox.com',
        'label': 0, 'category': 'legitimate'
    },

    #Slack
    {
        'url': 'https://slack.com/signin',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://slack.com/help',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://slack.com/features',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://api.slack.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://status.slack.com',
        'label': 0, 'category': 'legitimate'
    },

    # Project Management
    {
        'url': 'https://trello.com/home',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://trello.com/templates',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://asana.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://clickup.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://notion.so',
        'label': 0, 'category': 'legitimate'
    },

    #Zoom
    {
        'url': 'https://zoom.us/signin',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://zoom.us/download',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://support.zoom.us',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://explore.zoom.us',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://zoom.us/pricing',
        'label': 0, 'category': 'legitimate'
    },

    #Reddit
    {
        'url': 'https://www.reddit.com/r/programming',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.reddit.com/r/machinelearning',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.reddit.com/login',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://old.reddit.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://www.reddithelp.com',
        'label': 0, 'category': 'legitimate'
    },

    #Dev Blogs & Communities
    {
        'url': 'https://medium.com/topic/technology',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://medium.com/topic/programming',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://dev.to',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://hashnode.com',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://freecodecamp.org/news',
        'label': 0, 'category': 'legitimate'
    },

    #Python Ecosystem
    {
        'url': 'https://pypi.org/project/numpy',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://pypi.org/project/pandas',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://pypi.org/project/scikit-learn',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://docs.python.org/3',
        'label': 0, 'category': 'legitimate'
    },
    {
        'url': 'https://realpython.com',
        'label': 0, 'category': 'legitimate'
    },

    #Misk
    {
        'url': 'https://hub.misk.org.sa/',
        'label': 0, 'category': 'legitimate'
    },

    #More Google Docs
    {
        'url': 'https://docs.google.com/document/u/',
        'label': 0, 'category': 'legitimate'
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
