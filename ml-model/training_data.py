"""
CyberHunter Training Data
Separated into URL and Email datasets
"""

# EMAIL DATASET
EMAIL_TRAINING_DATA = [
    # PHISHING EMAILS (label=1)

    # DHL Phishing example Gibberish domain
    {
        'sender_email': 'Noreply-SNGVOTLA@sngvotlasngvotla.ca',
        'sender_name': 'DHL Express',
        'subject': 'Parcel Notification',
        'body': 'Your parcel has been suspended. Missing information. Please verify your address to schedule delivery.',
        'label': 1,
    },

    # FedEx Phishing 
    {
        'sender_email': 'label623435@494540.oceanpark.trip.entryway.giantreward.choresrecords.com',
        'sender_name': 'FedEx',
        'subject': 'Shipment Notification',
        'body': 'Your shipment is ready for delivery. Click here to confirm your address.',
        'label': 1,
    },

    # with Arabic mixed
    {
        'sender_email': 'label657841@540101.oceanpark.trip.entryway.giantreward.choresrecords.com',
        'sender_name': 'FedEx فيدكس',
        'subject': 'Package Delivery',
        'body': 'Your package requires verification. Update your delivery information now.',
        'label': 1,
    },

    {
        'sender_email': 'proof643380@706419.junglerealm.pathway.gatehouse.superwin.antiwalmart.com',
        'sender_name': 'FedEx Delivery',
        'subject': 'Action Required',
        'body': 'Urgent: Your shipment cannot be delivered. Missing address information. Verify now.',
        'label': 1,
    },

    # PayPal Phishing - Free email provider
    {
        'sender_email': 'paypal-security@gmail.com',
        'sender_name': 'PayPal Security',
        'subject': 'Account Suspended',
        'body': 'Your PayPal account has been suspended due to suspicious activity. Verify your identity immediately.',
        'label': 1,
    },

    # Bank Phishing - using urgent keyword
    {
        'sender_email': 'security@bank-verification.xyz',
        'sender_name': 'Chase Bank',
        'subject': 'Urgent: Verify Your Account',
        'body': 'Unauthorized access detected. Confirm your account details within 24 hours or your account will be locked.',
        'label': 1,
    },

# Arabic Bank Phishing
    {
        'sender_email': 'security@alrajhi-verify.com',
        'sender_name': 'الراجحي',
        'subject': 'تحذير أمني',
        'body': 'نشاط غير عادي في حسابك. يرجى تحديث معلوماتك الشخصية فوراً. آخر فرصة.',
        'label': 1,
    },
    # Arabic DHL Phishing
    {
        'sender_email': 'noreply@dhl-ksa-tracking.com',
        'sender_name': 'DHL Express',
        'subject': 'تنبيه شحنة',
        'body': 'تم تعليق طردك. معلومات مفقودة. يرجى التحقق من عنوانك لجدولة التسليم عاجل.',
        'label': 1,
    },

    

    # Microsoft Phishing - Account verification
    {
        'sender_email': 'noreply@microsoft-account-verify.com',
        'sender_name': 'Microsoft Account Team',
        'subject': 'Verify your Microsoft account',
        'body': 'Your Microsoft account requires verification. Click here to confirm your identity and prevent account closure.',
        'label': 1,
    },

    # Amazon Phishing - Prize scam
    {
        'sender_email': 'winner2024@amazon-prizes.top',
        'sender_name': 'Amazon Rewards',
        'subject': 'Congratulations! You won!',
        'body': 'You have been selected as a winner. Claim your free gift card now. Limited time offer.',
        'label': 1,
    },

    # Netflix Phishing - Payment update
    {
        'sender_email': 'billing@netflix-update.club',
        'sender_name': 'Netflix',
        'subject': 'Payment Failed',
        'body': 'Your payment method failed. Update your credit card information to continue your subscription.',
        'label': 1,
    },

    # Apple Phishing - iCloud storage
    {
        'sender_email': 'icloud-storage@apple-support.xyz',
        'sender_name': 'Apple Support',
        'subject': 'iCloud Storage Full',
        'body': 'Your iCloud storage is full. Upgrade now or your data will be deleted. Act immediately.',
        'label': 1,
    },

    # Random spam - Gibberish username
    {
        'sender_email': 'MguTYrJq@wildzone.freezone.xyz',
        'sender_name': 'Special Offer',
        'subject': 'Claim your prize',
        'body': 'You won a prize. Click here to claim your reward today only.',
        'label': 1,
    },

    # Arabic STC Phishing
    {
        'sender_email': 'verify@stc-rewards.com',
        'sender_name': 'STC',
        'subject': 'جائزة مجانية',
        'body': 'مبروك! فزت بجائزة من STC. اضغط هنا للمطالبة بالجائزة الآن.',
        'label': 1,
    },

    # Google Phishing - Security alert
    {
        'sender_email': 'security-alert@google-verify.tk',
        'sender_name': 'Google Security',
        'subject': 'Security Alert',
        'body': 'Suspicious activity detected on your Google account. Verify your password immediately.',
        'label': 1,
    },

    #LEGITIMATE EMAILS (label=0)

    # PSU
    {
        'sender_email': 'noreply@psu.edu.sa',
        'sender_name': 'PSU',
        'subject': 'CS316: Announcement',
        'body': 'assignment has been posted',
        'label': 0,
    },

    #FedEx
    {
        'sender_email': 'support@fedex.com',
        'sender_name': 'FedEx',
        'subject': 'Delivery Notification',
        'body': 'Your package will be delivered tomorrow. Track your shipment using the tracking number.',
        'label': 0,
    },

    #Google
    {
        'sender_email': 'no-reply@google.com',
        'sender_name': 'Google',
        'subject': 'Security Alert',
        'body': 'We noticed a new sign-in to your Google Account. If this was you, you don\'t need to do anything.',
        'label': 0,
    },

    #Amazon
    {
        'sender_email': 'auto-confirm@amazon.com',
        'sender_name': 'Amazon.com',
        'subject': 'Your order has shipped',
        'body': 'Your order has been shipped and will arrive in 2 business days.',
        'label': 0,
    },

    #Microsoft
    {
        'sender_email': 'no-reply@microsoft.com',
        'sender_name': 'Microsoft Account Team',
        'subject': 'Microsoft account activity',
        'body': 'Recent activity on your Microsoft account. Review your recent sign-in activity.',
        'label': 0,
    },

    #PayPal
    {
        'sender_email': 'service@paypal.com',
        'sender_name': 'PayPal',
        'subject': 'Receipt for your payment',
        'body': 'You sent a payment. Thank you for using PayPal.',
        'label': 0,
    },

    #DHL
    {
        'sender_email': 'noreply@dhl.com',
        'sender_name': 'DHL',
        'subject': 'Shipment notification',
        'body': 'Your shipment is on the way. Estimated delivery date.',
        'label': 0,
    },

    #Apple
    {
        'sender_email': 'no_reply@email.apple.com',
        'sender_name': 'Apple',
        'subject': 'Your receipt from Apple',
        'body': 'Thank you for your purchase from the App Store.',
        'label': 0,
    },

    #Netflix
    {
        'sender_email': 'info@mailer.netflix.com',
        'sender_name': 'Netflix',
        'subject': 'What to watch this weekend',
        'body': 'Check out these new releases on Netflix.',
        'label': 0,
    },

    #Arabic Bank - Al Rajhi
    {
        'sender_email': 'noreply@alrajhibank.com.sa',
        'sender_name': 'مصرف الراجحي',
        'subject': 'كشف حساب شهري',
        'body': 'كشف الحساب الشهري متاح الآن. يمكنك مراجعته من خلال تطبيق الراجحي.',
        'label': 0,
    },

    #STC
    {
        'sender_email': 'noreply@stc.com.sa',
        'sender_name': 'STC',
        'subject': 'فاتورة STC',
        'body': 'فاتورتك الشهرية جاهزة. يمكنك عرضها من خلال تطبيق mystc.',
        'label': 0,
    },

    #GitHub
    {
        'sender_email': 'noreply@github.com',
        'sender_name': 'GitHub',
        'subject': 'Your pull request was merged',
        'body': 'Your pull request has been successfully merged into the main branch.',
        'label': 0,
    },

    #LinkedIn
    {
        'sender_email': 'messages-noreply@linkedin.com',
        'sender_name': 'LinkedIn',
        'subject': 'You have a new message',
        'body': 'You have received a new message from your connection.',
        'label': 0,
    },

    # Bank - Chase
    {
        'sender_email': 'no.reply.alerts@chase.com',
        'sender_name': 'Chase',
        'subject': 'Your Chase statement is ready',
        'body': 'Your monthly statement is now available. View it online or in the Chase mobile app.',
        'label': 0,
    },

    # PayPal — legitimate legal agreement update
    {
        'sender_email': 'no_reply@communications.paypal.com',
        'sender_name': 'PayPal Communications',
        'subject': "We're making some changes to our PayPal legal agreements",
        'body': 'We are making changes to our legal agreements. No action needed. Visit PayPal.com for details. PayPal is committed to preventing fraudulent emails.',
        'label': 0,
    },

    # Microsoft — legitimate account security notification
    {
        'sender_email': 'account-security-noreply@accountprotection.microsoft.com',
        'sender_name': 'Microsoft account team',
        'subject': 'Microsoft account security info was added',
        'body': 'Security info was recently added to your Microsoft account. A passkey was added. If this was you, ignore this email. If this was not you, review your recent activity.',
        'label': 0,
    },

    # Move Dance — legitimate order shipping confirmation
    {
        'sender_email': 'system@tn3.netsuite.com',
        'sender_name': 'Move Online Retail Ltd',
        'subject': 'Move Online Retail Ltd: Your order #9923152 has shipped',
        'body': 'Great news, your parcel is on its way. Track my order. Delivery address: Riyadh SA. Sales order 9923152. EVRi shipping.',
        'label': 0,
    },

    # Additional legitimate emails with hyphens in subdomain (help model not penalize hyphens in legit domains)
    {
        'sender_email': 'no-reply@e-mail.hoyoverse.com',
        'sender_name': 'HoYoverse',
        'subject': 'Game update notification',
        'body': 'A new version is now available. Log in to claim your rewards.',
        'label': 0,
    },
    {
        'sender_email': 'noreply@e-comm.apple.com',
        'sender_name': 'Apple',
        'subject': 'Your Apple order',
        'body': 'Thank you for your purchase from Apple.',
        'label': 0,
    },

    # HoYoverse (Genshin Impact) — legitimate game newsletter
    {
        'sender_email': 'noreply.news@e-mail.hoyoverse.com',
        'sender_name': 'P.A.I.M.O.N',
        'subject': 'Thanks for waiting! The temple above Mondstadt is finally open',
        'body': 'Version Luna VI is now live. Congratulations on unlocking Reunion Gifts. Earn Primogems from limited-time exploration rewards. New character Linnea available for a limited time.',
        'label': 0,
    },

    # Ballet with Isabella — legitimate fitness/dance newsletter
    {
        'sender_email': 'isabella@balletwithisabella.com',
        'sender_name': 'Ballet with Isabella Ltd',
        'subject': 'Your ankles have been asking for this',
        'body': 'My Ankle Strength and Mobility class is already inside members accounts. The exercises train your strength at end range. Log in and give yourself this one this week. All levels welcome.',
        'label': 0,
    },

    # Substack newsletter — legitimate author newsletter
    {
        'sender_email': 'emilyhenry@substack.com',
        'sender_name': "Emily's Grocery List",
        'subject': 'Good little pretty paperbacks out soon',
        'body': 'The Great Big Beautiful Life paperback will be available on May 19th. Signed copies available. Thank you for your love and support.',
        'label': 0,
    },

    # Hollister — legitimate order confirmation
    {
        'sender_email': 'customercare@hollisterco.sa',
        'sender_name': 'Customer Services Team',
        'subject': 'Order Confirmation FKSA-ON-13631947',
        'body': 'Thanks for your order. Order number: FKSA-ON-13631947. Estimated delivery 1-3 business days. Order total SAR 298.00.',
        'label': 0,
    },

    # Netflix — legitimate terms update email
    {
        'sender_email': 'info@account.netflix.com',
        'sender_name': 'Netflix',
        'subject': 'Updates to our Terms of Use & Privacy Statement',
        'body': 'We are reaching out with updates to our Terms of Use and Privacy Statement about interactive features, advertising, and data from advertisers.',
        'label': 0,
    },

    # Safwat Al-Jawf — Arabic marketing email (health products, discount offer)
    {
        'sender_email': 'hello@safwat-aljawf.com',
        'sender_name': 'صفوة الجوف',
        'subject': 'دام صحتك ما تتساوم… نقدم لكم خصم ما هو عادي',
        'body': 'اطلب بكود vip20 ولك خصم 15% لمدة 24 ساعة فقط. عروض العودة للمدارس من صفوة الجوف. منتجاتنا الصحية: زيت الزيتون، الزعتر البري، قرانولا. مع كل طلب هدية مميزة.',
        'label': 0,
    },

    # Sephora marketing email
    {
        'sender_email': 'info@communication.sephora-info-me.com',
        'sender_name': 'SEPHORA',
        'subject': 'Discover Mongoliese now at Sephora',
        'body': 'A complete set for face and lips with a natural glow.',
        'label': 0,
    },

    # L'Occitane marketing email
    {
        'sender_email': 'newsletters@email-loccitane.com',
        'sender_name': "L'Occitane En Provence",
        'subject': 'New arrivals just for you',
        'body': 'Discover our latest skincare collection.',
        'label': 0,
    },

    # Amazon.sa — Eid marketing
    {
        'sender_email': 'store-news@amazon.sa',
        'sender_name': 'Amazon.sa',
        'subject': 'عروض العيد على الأحذية بخصم 80%',
        'body': 'تسوق أحذية نسائية ورجالية بخصم يصل إلى 80%. توصيل سريع ومجاني مع برايم.',
        'label': 0,
    },
    # Amazon.sa — order delivery
    {
        'sender_email': 'order-update@amazon.sa',
        'sender_name': 'Amazon.sa',
        'subject': 'Delivered: your Amazon.sa order',
        'body': 'Your package was delivered. It was handed directly to a resident. Track your order in the Amazon app.',
        'label': 0,
    },
    # Amazon.sa — shipping
    {
        'sender_email': 'shipment-tracking@amazon.sa',
        'sender_name': 'Amazon.sa',
        'subject': 'Your order has shipped',
        'body': 'Your Amazon.sa order is on its way. Expected delivery tomorrow.',
        'label': 0,
    },

    # Aura loyalty program (subdomain + hyphen = normal for marketing)
    {
        'sender_email': 'discover@your.aura-mena.com',
        'sender_name': 'Aura',
        'subject': 'We would love to hear your feedback',
        'body': 'Thank you for visiting us at The Cheesecake Factory. Let us know how we did.',
        'label': 0,
    },
    {
        'sender_email': 'rewards@my.aura-mena.com',
        'sender_name': 'Aura Rewards',
        'subject': 'Your points balance',
        'body': 'You have 1713 points in your Aura rewards account. Redeem them at any partner brand.',
        'label': 0,
    },

    # Twitter/X notification
    {
        'sender_email': 'notify@twitter.com',
        'sender_name': 'Twitter',
        'subject': 'Someone liked your Tweet',
        'body': 'Your Tweet got a like. See who liked it on Twitter.',
        'label': 0,
    },

    # Spotify
    {
        'sender_email': 'no-reply@spotify.com',
        'sender_name': 'Spotify',
        'subject': 'Your Spotify receipt',
        'body': 'Thanks for your Spotify Premium subscription. Your next billing date is next month.',
        'label': 0,
    },

    # Uber receipt
    {
        'sender_email': 'noreply@uber.com',
        'sender_name': 'Uber',
        'subject': 'Your Tuesday trip with Uber',
        'body': 'Thanks for riding with Uber. Here is your trip receipt. Total charged: 25.00 SAR.',
        'label': 0,
    },

    # Booking.com confirmation
    {
        'sender_email': 'noreply@booking.com',
        'sender_name': 'Booking.com',
        'subject': 'Booking confirmation — Riyadh Marriott Hotel',
        'body': 'Your booking is confirmed. Check-in: 10 May. Check-out: 12 May. Manage your booking on Booking.com.',
        'label': 0,
    },

    # Airbnb
    {
        'sender_email': 'automated@airbnb.com',
        'sender_name': 'Airbnb',
        'subject': 'Reservation confirmed',
        'body': 'Your reservation is confirmed. Your host is expecting you. Check your itinerary in the Airbnb app.',
        'label': 0,
    },

    # Noon.com (Saudi e-commerce)
    {
        'sender_email': 'noreply@noon.com',
        'sender_name': 'noon',
        'subject': 'Your order has been shipped',
        'body': 'Great news! Your noon order is on its way. Track your shipment in the noon app.',
        'label': 0,
    },

    # SADAD (Saudi payment system)
    {
        'sender_email': 'noreply@sadad.com.sa',
        'sender_name': 'SADAD',
        'subject': 'فاتورة جديدة بانتظارك',
        'body': 'لديك فاتورة جديدة في نظام سداد. يمكنك سدادها من خلال تطبيق البنك أو الصراف الآلي.',
        'label': 0,
    },

    # Careem
    {
        'sender_email': 'receipts@careem.com',
        'sender_name': 'Careem',
        'subject': 'Your Careem ride receipt',
        'body': 'Thank you for riding with Careem. Your trip summary and receipt are attached.',
        'label': 0,
    },

    # YouTube
    {
        'sender_email': 'noreply@youtube.com',
        'sender_name': 'YouTube',
        'subject': 'A new comment on your video',
        'body': 'Someone commented on your YouTube video. Sign in to reply.',
        'label': 0,
    },

    # Instagram
    {
        'sender_email': 'mail@mail.instagram.com',
        'sender_name': 'Instagram',
        'subject': 'You have a new follower',
        'body': 'Someone started following you on Instagram. See their profile in the app.',
        'label': 0,
    },

    # Zoom meeting invite
    {
        'sender_email': 'no-reply@zoom.us',
        'sender_name': 'Zoom',
        'subject': 'You have been invited to a Zoom meeting',
        'body': 'You are invited to join a Zoom meeting. Join from your computer or mobile app using the meeting ID provided.',
        'label': 0,
    },

    # University (Arabic - KAU)
    {
        'sender_email': 'noreply@kau.edu.sa',
        'sender_name': 'جامعة الملك عبدالعزيز',
        'subject': 'إعلان دراسي',
        'body': 'يُعلم الطلاب بأن الجدول الدراسي للفصل القادم متاح الآن على البوابة الإلكترونية.',
        'label': 0,
    },

    # STC Pay
    {
        'sender_email': 'noreply@stcpay.com.sa',
        'sender_name': 'STC Pay',
        'subject': 'تم استلام تحويلك',
        'body': 'تم إيداع مبلغ في محفظة STC Pay الخاصة بك. افتح التطبيق لعرض التفاصيل.',
        'label': 0,
    },

    # Slack workspace
    {
        'sender_email': 'feedback@slack.com',
        'sender_name': 'Slack',
        'subject': 'You have unread messages in Slack',
        'body': 'You have new messages waiting in your Slack workspace. Open Slack to catch up.',
        'label': 0,
    },

    # Coursera certificate
    {
        'sender_email': 'no-reply@coursera.org',
        'sender_name': 'Coursera',
        'subject': 'Congratulations on completing your course',
        'body': 'You have successfully completed Machine Learning on Coursera. Your certificate is ready to download.',
        'label': 0,
    },

    # Austrian Airlines — flight booking confirmation
    {
        'sender_email': 'booking@austrian.com',
        'sender_name': 'Austrian Airlines',
        'subject': 'Your booking confirmation',
        'body': 'Thank you for booking with Austrian Airlines. Your flight details are confirmed. Check in online from 47 hours before departure. Follow us on Instagram, Facebook, and Twitter.',
        'label': 0,
    },
    {
        'sender_email': 'newsletter@austrian.com',
        'sender_name': 'Austrian Airlines',
        'subject': 'Special fares this week',
        'body': 'Book your next trip with Austrian Airlines and enjoy special fares. Visit our website for details. Connect with us on social media.',
        'label': 0,
    },

    # KFC Saudi Arabia — promotional offer
    {
        'sender_email': 'noreply@offers.saudi.kfc.me',
        'sender_name': 'KFC Saudi Arabia',
        'subject': 'Limited time offer just for you',
        'body': 'Enjoy our new menu items at KFC Saudi Arabia. Order now via the app or website. Valid for a limited time only.',
        'label': 0,
    },

    # Schuh — shoe retailer order update
    {
        'sender_email': 'customerservices@email.schuh.co.uk',
        'sender_name': 'schuh',
        'subject': 'Your order has been dispatched',
        'body': 'Your schuh order is on its way. Expected delivery in 1-2 business days. Track your order using the link in this email.',
        'label': 0,
    },

    # Bath & Body Works Saudi Arabia
    {
        'sender_email': 'no-reply@bathandbodyworks.com.sa',
        'sender_name': 'Bath & Body Works',
        'subject': 'New arrivals: candles and body care',
        'body': 'Discover our latest candles, lotions, and shower gels. Shop online or visit your nearest Bath & Body Works store.',
        'label': 0,
    },

    # Warner Music Group — artist newsletter
    {
        'sender_email': 'news@wmg.com',
        'sender_name': 'Warner Music',
        'subject': 'New music from your favorite artists',
        'body': 'Check out the latest releases from Warner Music artists. Stream now on Spotify, Apple Music, and YouTube.',
        'label': 0,
    },

    # Squatwolf — fitness apparel
    {
        'sender_email': 'hello@squatwolf.com',
        'sender_name': 'SQUATWOLF',
        'subject': 'New collection just dropped',
        'body': 'Train hard in our new collection. Free shipping on orders over $100. Shop now on our website.',
        'label': 0,
    },

    # === DELIVERY + URGENCY SCAMS (no explicit brand) ===

    # Cloud storage link delivery scam
    {
        'sender_email': 'delivery-notice@parcel-info.xyz',
        'sender_name': 'Delivery Service',
        'subject': 'Your package is on hold',
        'body': 'You have a delivery. You have to pay now at: https://storage.googleapis.com/localbuckjaw456/hreflyjaw.html',
        'label': 1,
    },
    {
        'sender_email': 'noreply@courier-update.top',
        'sender_name': 'Courier Notification',
        'subject': 'Action required: delivery fee',
        'body': 'Your shipment is awaiting customs clearance. Pay the fee now to release your package.',
        'label': 1,
    },
    {
        'sender_email': 'update@parcel-hold.ga',
        'sender_name': 'Package Tracking',
        'subject': 'Missed delivery — pay to reschedule',
        'body': 'We attempted to deliver your parcel. A customs fee of $2.99 is required. Pay now or your package will be returned.',
        'label': 1,
    },
    {
        'sender_email': 'shipment@delivery-fee-confirm.xyz',
        'sender_name': 'Shipment Team',
        'subject': 'Your parcel requires payment',
        'body': 'Your package is held at customs. You must pay the shipping fee immediately to receive your delivery.',
        'label': 1,
    },

    # Arabic delivery scam
    {
        'sender_email': 'noreply@توصيل-سريع.com',
        'sender_name': 'خدمة التوصيل',
        'subject': 'طردك في انتظار الدفع',
        'body': 'لديك طرد في الانتظار. يجب عليك الدفع الآن لاستلامه. اضغط على الرابط.',
        'label': 1,
    },

    # Payment urgency without brand
    {
        'sender_email': 'billing@payment-required-now.xyz',
        'sender_name': 'Billing Department',
        'subject': 'Invoice overdue — pay now',
        'body': 'Your invoice is overdue. You must pay now to avoid service suspension. Click the link to complete payment.',
        'label': 1,
    },
    {
        'sender_email': 'alert@account-payment-due.top',
        'sender_name': 'Account Team',
        'subject': 'Final notice: payment required',
        'body': 'This is your final notice. Your account will be closed if payment is not received within 24 hours.',
        'label': 1,
    },

    # OTP / verification scam via link
    {
        'sender_email': 'verify@secure-otp-confirm.xyz',
        'sender_name': 'Security Team',
        'subject': 'Your OTP has expired — verify now',
        'body': 'Your one-time password has expired. Click here to verify your account and generate a new OTP.',
        'label': 1,
    },
    {
        'sender_email': 'noreply@account-verify-secure.ga',
        'sender_name': 'Account Verification',
        'subject': 'Confirm your identity',
        'body': 'We detected a login from a new device. Confirm your identity immediately or your account will be suspended.',
        'label': 1,
    },

    # Phishing - Western name from Japanese ISP domain (generic)
    {
        'sender_email': 'nenkin.hyogo@ruby.plala.or.jp',
        'sender_name': 'Charles Koch',
        'subject': 'Important business proposal',
        'body': 'I have a business proposal for you regarding an investment opportunity.',
        'label': 1,
    },

    #  Money scams - lottery/inheritancePhishing 
    {
        'sender_email': 'nenkin.hyogo@ruby.plala.or.jp',
        'sender_name': 'Charles Koch',
        'subject': 'DONATION NOTICE.REF:MDD9926',
        'body': 'This is to inform you that my late brother strongly believed in giving while living and decided to give USD2,000,000.00 Million Dollars to randomly selected individuals worldwide. On receipt of this email you should count yourself as the lucky individual.',
        'label': 1,
    },

    # Money scams - lottery/inheritance
    {
        'sender_email': 'beneficiary@fundrelease-agency.com',
        'sender_name': 'UN Compensation Fund',
        'subject': 'You have an unclaimed inheritance of $4.5 Million',
        'body': 'Dear beneficiary, we are pleased to inform you that you have been selected to receive a sum of $4,500,000.00 USD as compensation. To claim your funds, send a copy of your ID and pay a small processing fee.',
        'label': 1,
    },
    {
        'sender_email': 'mrjohncooper@mailhost.xyz',
        'sender_name': 'Mr. John Cooper',
        'subject': 'Lottery winning notification',
        'body': 'Congratulations! You have won the international lottery jackpot of 1,000,000 GBP. To claim your prize money, provide your bank account details and national ID for wire transfer.',
        'label': 1,
    },
    {
        'sender_email': 'dr.aminu@globalfund-wire.net',
        'sender_name': 'Dr. Aminu Kano',
        'subject': 'Business Partnership - $15 Million Fund Transfer',
        'body': 'I need your assistance to transfer USD15,000,000 from an inactive account. You will receive 30% commission. Send your full name, address, and bank details to proceed.',
        'label': 1,
    },

    # Job offer scam
    {
        'sender_email': 'hr@globalcareers-hiring.net',
        'sender_name': 'Global Careers HR',
        'subject': 'You have been selected for a remote position',
        'body': 'Congratulations! You have been selected for a remote work opportunity paying $5,000/month. No experience needed. Reply with your full name, address, and bank details to receive your starter kit.',
        'label': 1,
    },
    {
        'sender_email': 'recruitment@jobs-online-hiring.xyz',
        'sender_name': 'Online Jobs Team',
        'subject': 'Work from home — $800/day guaranteed',
        'body': 'We are hiring remote workers. Earn $800 per day working from home. Send your ID and bank account number to get started immediately.',
        'label': 1,
    },

    # Crypto scam
    {
        'sender_email': 'support@crypto-wallet-verify.com',
        'sender_name': 'Crypto Wallet Support',
        'subject': 'Your Bitcoin wallet requires verification',
        'body': 'Your cryptocurrency wallet has been flagged for suspicious activity. Verify your wallet now or your funds will be frozen. Enter your seed phrase to confirm your identity.',
        'label': 1,
    },
    {
        'sender_email': 'noreply@bitcoin-reward-claim.top',
        'sender_name': 'Bitcoin Rewards',
        'subject': 'You have unclaimed Bitcoin worth $9,400',
        'body': 'Our system shows you have unclaimed Bitcoin in your account. Click here to claim your cryptocurrency reward before it expires.',
        'label': 1,
    },

    # Tax refund scam
    {
        'sender_email': 'refund@irs-tax-refund.xyz',
        'sender_name': 'IRS Tax Refund',
        'subject': 'Your tax refund of $2,840 is ready',
        'body': 'The IRS has processed your tax return. You are eligible for a refund of $2,840. Confirm your bank account details within 48 hours to receive your payment.',
        'label': 1,
    },

    # Fake invoice scam
    {
        'sender_email': 'billing@invoice-payment-due.net',
        'sender_name': 'Accounts Payable',
        'subject': 'Invoice #INV-2094 payment overdue',
        'body': 'Please find attached invoice #INV-2094 for $3,200. This payment is overdue. Wire the amount to our new bank account immediately to avoid late fees.',
        'label': 1,
    },

    # Attachment phishing
    {
        'sender_email': 'noreply@document-secure-share.xyz',
        'sender_name': 'Secure Document',
        'subject': 'Important document shared with you',
        'body': 'A confidential document has been shared with you. Please open the attached file and enter your credentials to view it. This link expires in 24 hours.',
        'label': 1,
    },

    {
        'sender_email': 'emily.johnson2024@mailhost.xyz',
        'sender_name': 'Emily Johnson',
        'subject': 'I found your profile and would love to connect',
        'body': 'Hello dear, I came across your profile and I am very interested in getting to know you. I am a nurse working abroad. Please reply so we can talk more. I have something important to share with you.',
        'label': 1,
    },

    # Arabic job scam
    {
        'sender_email': 'hr@وظائف-عن-بعد.com',
        'sender_name': 'فرص العمل',
        'subject': 'وظيفة عن بعد براتب 5000 ريال',
        'body': 'تم اختيارك للعمل عن بعد براتب 5000 ريال شهرياً. لا خبرة مطلوبة. أرسل بياناتك الشخصية ورقم حسابك البنكي للتسجيل الآن.',
        'label': 1,
    },
]


#URL DATASET
URL_TRAINING_DATA = [
    #PHISHING URLS (label=1)

    # Typosquatting - eBay
    {
        'url': 'http://eb4y.com',
        'label': 1,
    },

    {
        'url': 'http://ebai.com',
        'label': 1,
    },

    {
        'url': 'http://3bay.com',
        'label': 1,
    },

    # Typosquatting - Sephora
    {
        'url': 'http://seph0ra.com',
        'label': 1,
    },

    {
        'url': 'http://sephura.com',
        'label': 1,
    },

    {
        'url': 'http://sephoora.com',
        'label': 1,
    },

    {
        'url': 'http://sephu0ra.com',
        'label': 1,
    },

    {
        'url': 'http://seph1ra.com',
        'label': 1,
    },

    {
        'url': 'http://seph6ra.com',
        'label': 1,
    },



    # Typosquatting - Netflix 
    {
        'url': 'http://netf1ix.com',
        'label': 1,
    },

    # Typosquatting - Apple
    {
        'url': 'http://appl3.com',
        'label': 1,
    },

    {
        'url': 'http://app1e.com',
        'label': 1,
    },

    # Typosquatting - Amazon 
    {
        'url': 'http://4mazon.com',
        'label': 1,
    },

    # Typosquatting - Amazon
    {
        'url': 'http://amaz0n.com',
        'label': 1,
    },

    # Typosquatting - DHL
    {
        'url': 'http://dh1.com',
        'label': 1,
    },

    # Typosquatting - FedEx 
    {
        'url': 'http://f3dex.com',
        'label': 1,
    },

    {
        'url': 'http://f3d3x.com',
        'label': 1,
    },

    # Brand in subdomain
    {
        'url': 'http://paypal.evil-site.xyz/secure/login',
        'label': 1,
    },

    # IP address URL
    {
        'url': 'http://192.168.1.100/paypal/verify',
        'label': 1,
    },

    # Credential attack URL (@ in URL)
    {
        'url': 'http://google.com@evil-site.com/login',
        'label': 1,
    },

    # Suspicious TLD URL
    {
        'url': 'http://account-verify-secure.xyz/update',
        'label': 1,
    },

    # Long suspicious URL with many hyphens
    {
        'url': 'http://secure-login-verify-account-update-confirm.tk/auth',
        'label': 1,
    },

    #PayPal Phishing URLs
    {
        'url': 'http://paypa1-security-verify.tk/login',
        'label': 1,
    },
    {
        'url': 'http://paypa1-login-security.com/verify',
        'label': 1,    },
    {
        'url': 'http://paypal.account-update-secure.xyz/login',
        'label': 1,    },
    {
        'url': 'http://secure-paypal.evil-domain.ru/auth',
        'label': 1,    },
    {
        'url': 'http://login-paypal-confirm.netlify.app',
        'label': 1,    },
    {
        'url': 'http://paypal.verify-user-access.tk',
        'label': 1,    },
{
        'url': 'http://secure-paypaI-reset-password.xyz/login',
        'label': 1,    },
    {
        'url': 'http://paypal-warning-user-confirm.top/auth',
        'label': 1,    },
    {
        'url': 'http://paypal-security-team-alert.help/verify',
        'label': 1,    },
    {
        'url': 'http://paypa1-account-check.ga/login',
        'label': 1,    },
    {
        'url': 'http://paypal-login-session-expired.ru/auth',
        'label': 1,    },

    # --- Amazon Phishing URLs ---
    {
        'url': 'http://amaz0n-security-check.com/update',
        'label': 1,    },
    {
        'url': 'http://amazon.login-alert.xyz/confirm',
        'label': 1,    },
    {
        'url': 'http://secure-amazon-payment.ga/verify',
        'label': 1,    },
    {
        'url': 'http://amazon.account-locked.help/login',
        'label': 1,    },
    {
        'url': 'http://amazon.customer.verify-now.top',
        'label': 1,    },

    # --- Microsoft Phishing URLs ---
    {
        'url': 'http://micr0soft-account-security.com/login',
        'label': 1,    },
    {
        'url': 'http://microsoft.verify-session.xyz/auth',
        'label': 1,    },
    {
        'url': 'http://secure-microsoft-alert.ga/reset',
        'label': 1,    },
    {
        'url': 'http://office365-login-confirm.ru/secure',
        'label': 1,    },
    {
        'url': 'http://microsoft-authentication-warning.top',
        'label': 1,    },

    # --- Google Phishing URLs ---
    {
        'url': 'http://goog1e-account-recovery.com/signin',
        'label': 1,    },
    {
        'url': 'http://google.security-check-alert.xyz/login',
        'label': 1,    },
    {
        'url': 'http://accounts-google.verify-user.net/auth',
        'label': 1,    },
    {
        'url': 'http://google-auth-reset-password.help',
        'label': 1,    },
    {
        'url': 'http://drive-google-secure-access.top',
        'label': 1,    },

    # --- Facebook Phishing URLs ---
    {
        'url': 'http://faceb00k-security-alert.com/login',
        'label': 1,    },
    {
        'url': 'http://faceb00k',
        'label': 1,    },
    {
        'url': 'http://faceb0ok',
        'label': 1,    },
    {
        'url': 'http://f4ceb0ok',
        'label': 1,    },
    {
        'url': 'http://facebook.verify-session.xyz/auth',
        'label': 1,    },
    {
        'url': 'http://secure-facebook-warning.ga/confirm',
        'label': 1,    },
    {
        'url': 'http://facebook-login-check.help/reset',
        'label': 1,    },
    {
        'url': 'http://fb-account-protection.top',
        'label': 1,    },

    # --- Banking Phishing URLs ---
    {
        'url': 'http://bank-secure-login-update.xyz/auth',
        'label': 1,    },
    {
        'url': 'http://chase.verify-account-alert.ru/login',
        'label': 1,    },
    {
        'url': 'http://secure-bank-authentication.ga/verify',
        'label': 1,    },
    {
        'url': 'http://account-warning-bank.top/update',
        'label': 1,    },
    {
        'url': 'http://bank-login-confirm.help',
        'label': 1,    },

    # --- Shipping/Courier Phishing URLs ---
    {
        'url': 'http://dhl-tracking-confirmation.xyz/update',
        'label': 1,    },
    {
        'url': 'http://fedex-delivery-problem.top/verify',
        'label': 1,    },
    {
        'url': 'http://ups-shipping-alert.ga/confirm',
        'label': 1,    },
    {
        'url': 'http://package-delivery-missing-info.help',
        'label': 1,    },
    {
        'url': 'http://courier-tracking-warning.ru/check',
        'label': 1,    },

    # --- IP Address Phishing URLs ---
    {
        'url': 'http://192.168.0.55/paypal/login',
        'label': 1,    },
    {
        'url': 'http://45.88.120.3/secure-bank/auth',
        'label': 1,    },
    {
        'url': 'http://103.21.244.1/google/verify',
        'label': 1,    },

    # --- Credential Attack URLs (@ in URL) ---
    {
        'url': 'http://google.com@evil-site.xyz/login',
        'label': 1,    },
    {
        'url': 'http://paypal.com@phish-domain.ru/auth',
        'label': 1,    },
    {
        'url': 'http://amazon.com@malicious-site.top/signin',
        'label': 1,    },

    # --- Long Suspicious URLs ---
    {
        'url': 'http://important-security-notice-login.xyz/secure',
        'label': 1,    },
    {
        'url': 'http://user-verification-required-now.top/login',
        'label': 1,    },
    {
        'url': 'http://account-suspension-warning.ga/auth',
        'label': 1,    },
    {
        'url': 'http://last-chance-account-verify.help/login',
        'label': 1,    },
# Typosquatting - Netflix 
    {
        'url': 'http://netfl1x.com',
        'label': 1,
    },
    # --- Sephora Phishing URL ---
    {
        'url': 'http://s0ephora1.com',
        'label': 1,    },

    
    # --- More Amazon Phishing ---
    {
        'url': 'http://amaz0n-order-problem-confirm.xyz/update',
        'label': 1,    },
    {
        'url': 'http://amazon-security-team-alert.top/login',
        'label': 1,    },
    {
        'url': 'http://amazon-user-verification.help/auth',
        'label': 1,    },
    {
        'url': 'http://secure-amazon-session-warning.ga/verify',
        'label': 1,    },
    {
        'url': 'http://amazon-login-unusual-activity.ru/check',
        'label': 1,    },

    # --- More Microsoft Phishing ---
    {
        'url': 'http://micros0ft-account-warning.xyz/reset',
        'label': 1,    },
    {
        'url': 'http://microsoft-session-expired.top/login',
        'label': 1,    },
    {
        'url': 'http://secure-office365-confirm.help/auth',
        'label': 1,    },
    {
        'url': 'http://office-login-security-alert.ga/reset',
        'label': 1,    },
    {
        'url': 'http://microsoft-user-verification.ru/login',
        'label': 1,    },

    # --- More Google Phishing ---
    {
        'url': 'http://goog1e-login-suspicious-activity.xyz/auth',
        'label': 1,    },
    {
        'url': 'http://google-account-warning.top/verify',
        'label': 1,    },
    {
        'url': 'http://secure-google-confirm-session.help/reset',
        'label': 1,    },
    {
        'url': 'http://google-user-authentication.ga/login',
        'label': 1,    },
    {
        'url': 'http://google-password-reset-alert.ru/auth',
        'label': 1,    },

    # --- More Facebook Phishing ---
    {
        'url': 'http://faceb00k-login-confirm.xyz/security',
        'label': 1,    },
    {
        'url': 'http://facebook-session-warning.top/reset',
        'label': 1,    },
    {
        'url': 'http://secure-facebook-user-check.help/login',
        'label': 1,    },
    {
        'url': 'http://facebook-authentication-required.ga/verify',
        'label': 1,    },
    {
        'url': 'http://facebook-password-alert.ru/reset',
        'label': 1,    },

    # --- More Banking Phishing ---
    {
        'url': 'http://bank-account-security-warning.xyz/login',
        'label': 1,    },
    {
        'url': 'http://secure-onlinebank-confirm.top/auth',
        'label': 1,    },
    {
        'url': 'http://bank-session-expired.help/verify',
        'label': 1,    },
    {
        'url': 'http://bank-login-alert.ga/reset',
        'label': 1,    },
    {
        'url': 'http://bank-user-check-required.ru/auth',
        'label': 1,    },

    # --- More Shipping Phishing ---
    {
        'url': 'http://dhl-delivery-problem-confirm.xyz/track',
        'label': 1,    },
    {
        'url': 'http://fedex-address-verification.top/update',
        'label': 1,    },
    {
        'url': 'http://ups-shipping-session.help/confirm',
        'label': 1,    },
    {
        'url': 'http://courier-delivery-warning.ga/verify',
        'label': 1,    },
    {
        'url': 'http://parcel-redelivery-alert.ru/check',
        'label': 1,    },

    # --- More Long Suspicious ---
    {
        'url': 'http://secure-login-confirm-user-account-update.xyz/auth',
        'label': 1,    },
    {
        'url': 'http://important-account-warning-reset.top/login',
        'label': 1,    },
    {
        'url': 'http://last-notice-user-verification.help/auth',
        'label': 1,    },
    {
        'url': 'http://urgent-security-confirmation.ga/reset',
        'label': 1,    },
    {
        'url': 'http://final-account-check-required.ru/login',
        'label': 1,    },

    # --- More IP Address Phishing ---
    {
        'url': 'http://172.16.5.44/bank/login',
        'label': 1,    },
    {
        'url': 'http://88.214.193.17/google/auth',
        'label': 1,    },
    {
        'url': 'http://31.13.77.102/facebook/security',
        'label': 1,    },

    # --- More Credential Attacks ---
    {
        'url': 'http://paypal.com@secure-authenticate.xyz/login',
        'label': 1,    },
    {
        'url': 'http://google.com@account-warning.top/auth',
        'label': 1,    },
    {
        'url': 'http://amazon.com@session-check.help/login',
        'label': 1,    },
    {
        'url': 'http://microsoft.com@verify-user.ga/auth',
        'label': 1,    },
    {
        'url': 'http://bank.com@security-alert.ru/login',
        'label': 1,    },

    # LEGITIMATE URLS (label=0) 

    {
        'url': 'https://www.google.com',
        'label': 0,
    },
    {
        'url': 'https://www.amazon.com/gp/product/B08N5WRWNW',
        'label': 0,
    },
    {
        'url': 'https://github.com/anthropics/claude-code',
        'label': 0,
    },
    {
        'url': 'https://support.apple.com/en-us/HT201222',
        'label': 0,
    },
    {
        'url': 'https://www.paypal.com/myaccount/summary',
        'label': 0,
    },
    {
        'url': 'https://www.microsoft.com/en-us/windows',
        'label': 0,
    },

    # --- Google ---
    {
        'url': 'https://mail.google.com',
        'label': 0,    },
    {
        'url': 'https://drive.google.com',
        'label': 0,    },
    {
        'url': 'https://maps.google.com',
        'label': 0,    },
    {
        'url': 'https://accounts.google.com/signin',
        'label': 0,    },

    # --- Amazon ---
    {
        'url': 'https://www.amazon.com',
        'label': 0,    },
    {
        'url': 'https://www.amazon.com/orders',
        'label': 0,    },
    {
        'url': 'https://www.amazon.com/gp/help/customer/display.html',
        'label': 0,    },
    {
        'url': 'https://sellercentral.amazon.com',
        'label': 0,    },
    {
        'url': 'https://music.amazon.com',
        'label': 0,    },

    # --- Microsoft ---
    {
        'url': 'https://www.microsoft.com',
        'label': 0,    },
    {
        'url': 'https://account.microsoft.com',
        'label': 0,    },
    {
        'url': 'https://login.live.com',
        'label': 0,    },
    {
        'url': 'https://support.microsoft.com',
        'label': 0,    },
    {
        'url': 'https://portal.office.com',
        'label': 0,    },

    # --- PayPal ---
    {
        'url': 'https://www.paypal.com',
        'label': 0,    },
    {
        'url': 'https://www.paypal.com/signin',
        'label': 0,    },
    {
        'url': 'https://developer.paypal.com',
        'label': 0,    },
    {
        'url': 'https://www.paypal.com/us/webapps/mpp/home',
        'label': 0,    },

    # --- GitHub ---
    {
        'url': 'https://github.com',
        'label': 0,    },
    {
        'url': 'https://github.com/login',
        'label': 0,    },
    {
        'url': 'https://docs.github.com',
        'label': 0,    },
    {
        'url': 'https://api.github.com',
        'label': 0,    },
    {
        'url': 'https://github.com/features',
        'label': 0,    },

    # --- Other Tech ---
    {
        'url': 'https://stackoverflow.com',
        'label': 0,    },
    {
        'url': 'https://stackoverflow.com/questions',
        'label': 0,    },
    {
        'url': 'https://chat.openai.com',
        'label': 0,    },
    {
        'url': 'https://openai.com',
        'label': 0,    },
    {
        'url': 'https://platform.openai.com/docs',
        'label': 0,    },

    # --- Apple ---
    {
        'url': 'https://www.apple.com',
        'label': 0,    },
    {
        'url': 'https://developer.apple.com',
        'label': 0,    },
    {
        'url': 'https://www.icloud.com',
        'label': 0,    },
    {
        'url': 'https://apps.apple.com',
        'label': 0,    },

    # --- Entertainment & Social ---
    {
        'url': 'https://www.netflix.com',
        'label': 0,    },
    {
        'url': 'https://help.netflix.com',
        'label': 0,    },
    {
        'url': 'https://www.ebay.com',
        'label': 0,    },
    {
        'url': 'https://www.ebay.com/help/home',
        'label': 0,    },
    {
        'url': 'https://www.ebay.com/sh/ovw',
        'label': 0,    },
    {
        'url': 'https://www.linkedin.com',
        'label': 0,    },
    {
        'url': 'https://twitter.com',
        'label': 0,    },
    {
        'url': 'https://www.youtube.com',
        'label': 0,    },

    # --- News & Education ---
    {
        'url': 'https://www.wikipedia.org',
        'label': 0,    },
    {
        'url': 'https://www.bbc.com',
        'label': 0,    },
    {
        'url': 'https://www.nytimes.com',
        'label': 0,    },
    {
        'url': 'https://www.coursera.org',
        'label': 0,    },
    {
        'url': 'https://www.udemy.com',
        'label': 0,    },

    # --- Sephora ---
    {
        'url': 'https://sephora.com',
        'label': 0,    },
    {
        'url': 'https://www.sephora.sa',
        'label': 0,    },
    {
        'url': 'https://t10.communication.sephora-info-fr.com/r/?id=h26a4148c',
        'label': 0,    },
    {
        'url': 'https://t10.communication.sephora-info-me.com/r/?id=example',
        'label': 0,    },

    # --- More Google ---
    {
        'url': 'https://www.google.com/search?q=machine+learning',
        'label': 0,    },
    {
        'url': 'https://news.google.com',
        'label': 0,    },
    {
        'url': 'https://calendar.google.com',
        'label': 0,    },
    {
        'url': 'https://translate.google.com',
        'label': 0,    },
    {
        'url': 'https://photos.google.com',
        'label': 0,    },
    {
        'url': 'https://meet.google.com',
        'label': 0,    },
    {
        'url': 'https://contacts.google.com',
        'label': 0,    },
    {
        'url': 'https://fonts.google.com',
        'label': 0,    },
    {
        'url': 'https://earth.google.com',
        'label': 0,    },
    {
        'url': 'https://store.google.com',
        'label': 0,    },

    # --- More Amazon ---
    {
        'url': 'https://www.amazon.com/gp/cart/view.html',
        'label': 0,    },
    {
        'url': 'https://www.amazon.com/gp/your-account/order-history',
        'label': 0,    },
    {
        'url': 'https://www.amazon.com/prime',
        'label': 0,    },
    {
        'url': 'https://www.amazon.com/music',
        'label': 0,    },
    {
        'url': 'https://www.amazon.com/kindle-dbs/storefront',
        'label': 0,    },
    {
        'url': 'https://advertising.amazon.com',
        'label': 0,    },
    {
        'url': 'https://aws.amazon.com',
        'label': 0,    },
    {
        'url': 'https://docs.aws.amazon.com',
        'label': 0,    },
    {
        'url': 'https://console.aws.amazon.com',
        'label': 0,    },
    {
        'url': 'https://status.aws.amazon.com',
        'label': 0,    },

    # --- More Microsoft ---
    {
        'url': 'https://support.microsoft.com/en-us',
        'label': 0,    },
    {
        'url': 'https://learn.microsoft.com',
        'label': 0,    },
    {
        'url': 'https://visualstudio.microsoft.com',
        'label': 0,    },
    {
        'url': 'https://azure.microsoft.com',
        'label': 0,    },
    {
        'url': 'https://portal.azure.com',
        'label': 0,    },
    {
        'url': 'https://dev.azure.com',
        'label': 0,    },
    {
        'url': 'https://outlook.live.com',
        'label': 0,    },
    {
        'url': 'https://onedrive.live.com',
        'label': 0,    },
    {
        'url': 'https://bing.com',
        'label': 0,    },
    {
        'url': 'https://microsoftedge.microsoft.com',
        'label': 0,    },

    # --- More PayPal ---
    {
        'url': 'https://www.paypal.com/us/signin',
        'label': 0,    },
    {
        'url': 'https://www.paypal.com/us/smarthelp/home',
        'label': 0,    },
    {
        'url': 'https://www.paypal.com/us/webapps/mpp/send-money-online',
        'label': 0,    },
    {
        'url': 'https://www.paypal.com/us/business',
        'label': 0,    },
    {
        'url': 'https://www.paypal.com/us/security',
        'label': 0,    },

    # --- More GitHub ---
    {
        'url': 'https://github.com/explore',
        'label': 0,    },
    {
        'url': 'https://github.com/trending',
        'label': 0,    },
    {
        'url': 'https://github.com/marketplace',
        'label': 0,    },
    {
        'url': 'https://docs.github.com/en/get-started',
        'label': 0,    },
    {
        'url': 'https://education.github.com',
        'label': 0,    },
    {
        'url': 'https://status.github.com',
        'label': 0,    },
    {
        'url': 'https://gist.github.com',
        'label': 0,    },
    {
        'url': 'https://pages.github.com',
        'label': 0,    },
    {
        'url': 'https://cli.github.com',
        'label': 0,    },
    {
        'url': 'https://api.github.com/repos',
        'label': 0,    },

    # --- StackOverflow & StackExchange ---
    {
        'url': 'https://stackoverflow.com/tags',
        'label': 0,    },
    {
        'url': 'https://stackoverflow.com/jobs',
        'label': 0,    },
    {
        'url': 'https://superuser.com',
        'label': 0,    },
    {
        'url': 'https://serverfault.com',
        'label': 0,    },
    {
        'url': 'https://stackapps.com',
        'label': 0,    },
    {
        'url': 'https://stackexchange.com',
        'label': 0,    },

    # --- More OpenAI ---
    {
        'url': 'https://openai.com/research',
        'label': 0,    },
    {
        'url': 'https://openai.com/blog',
        'label': 0,    },
    {
        'url': 'https://platform.openai.com',
        'label': 0,    },
    {
        'url': 'https://platform.openai.com/playground',
        'label': 0,    },
    {
        'url': 'https://help.openai.com',
        'label': 0,    },

    # --- More Apple ---
    {
        'url': 'https://www.apple.com/iphone',
        'label': 0,    },
    {
        'url': 'https://www.apple.com/mac',
        'label': 0,    },
    {
        'url': 'https://www.apple.com/ipad',
        'label': 0,    },
    {
        'url': 'https://www.apple.com/watch',
        'label': 0,    },
    {
        'url': 'https://www.apple.com/services',
        'label': 0,    },
    {
        'url': 'https://support.apple.com/iphone',
        'label': 0,    },
    {
        'url': 'https://support.apple.com/mac',
        'label': 0,    },
    {
        'url': 'https://developer.apple.com/xcode',
        'label': 0,    },
    {
        'url': 'https://developer.apple.com/swift',
        'label': 0,    },
    {
        'url': 'https://www.icloud.com/mail',
        'label': 0,    },

    # --- More Netflix ---
    {
        'url': 'https://www.netflix.com/browse',
        'label': 0,    },
    {
        'url': 'https://www.netflix.com/latest',
        'label': 0,    },
    {
        'url': 'https://help.netflix.com/en/node/412',
        'label': 0,    },
    {
        'url': 'https://jobs.netflix.com',
        'label': 0,    },
    {
        'url': 'https://media.netflix.com',
        'label': 0,    },

    # --- More LinkedIn ---
    {
        'url': 'https://www.linkedin.com/feed',
        'label': 0,    },
    {
        'url': 'https://www.linkedin.com/jobs',
        'label': 0,    },
    {
        'url': 'https://www.linkedin.com/learning',
        'label': 0,    },
    {
        'url': 'https://business.linkedin.com',
        'label': 0,    },
    {
        'url': 'https://engineering.linkedin.com',
        'label': 0,    },

    # --- More Twitter ---
    {
        'url': 'https://twitter.com/home',
        'label': 0,    },
    {
        'url': 'https://twitter.com/explore',
        'label': 0,    },
    {
        'url': 'https://twitter.com/settings/account',
        'label': 0,    },
    {
        'url': 'https://help.twitter.com',
        'label': 0,    },
    {
        'url': 'https://developer.twitter.com',
        'label': 0,    },

    # --- More YouTube ---
    {
        'url': 'https://www.youtube.com/feed/subscriptions',
        'label': 0,    },
    {
        'url': 'https://www.youtube.com/results?search_query=python',
        'label': 0,    },
    {
        'url': 'https://studio.youtube.com',
        'label': 0,    },
    {
        'url': 'https://music.youtube.com',
        'label': 0,    },
    {
        'url': 'https://support.google.com/youtube',
        'label': 0,    },

    # --- More Wikipedia ---
    {
        'url': 'https://www.wikipedia.org/wiki/Artificial_intelligence',
        'label': 0,    },
    {
        'url': 'https://en.wikipedia.org/wiki/Machine_learning',
        'label': 0,    },
    {
        'url': 'https://en.wikipedia.org/wiki/Phishing',
        'label': 0,    },
    {
        'url': 'https://commons.wikimedia.org',
        'label': 0,    },
    {
        'url': 'https://meta.wikimedia.org',
        'label': 0,    },

    # --- More News ---
    {
        'url': 'https://www.bbc.com/news',
        'label': 0,    },
    {
        'url': 'https://www.bbc.com/sport',
        'label': 0,    },
    {
        'url': 'https://www.cnn.com/world',
        'label': 0,    },
    {
        'url': 'https://www.reuters.com',
        'label': 0,    },
    {
        'url': 'https://www.aljazeera.com',
        'label': 0,    },

    # --- More Education ---
    {
        'url': 'https://www.coursera.org/learn/machine-learning',
        'label': 0,    },
    {
        'url': 'https://www.coursera.org/professional-certificates',
        'label': 0,    },
    {
        'url': 'https://www.edx.org/course',
        'label': 0,    },
    {
        'url': 'https://www.udemy.com/course/python-for-beginners',
        'label': 0,    },
    {
        'url': 'https://www.udacity.com/course',
        'label': 0,    },

    # --- More NYT & Business News ---
    {
        'url': 'https://www.nytimes.com/section/technology',
        'label': 0,    },
    {
        'url': 'https://www.theguardian.com/international',
        'label': 0,    },
    {
        'url': 'https://www.forbes.com/technology',
        'label': 0,    },
    {
        'url': 'https://www.bloomberg.com/markets',
        'label': 0,    },
    {
        'url': 'https://techcrunch.com',
        'label': 0,    },

    # --- Cloud Storage ---
    {
        'url': 'https://www.dropbox.com/login',
        'label': 0,    },
    {
        'url': 'https://www.dropbox.com/home',
        'label': 0,    },
    {
        'url': 'https://www.dropbox.com/business',
        'label': 0,    },
    {
        'url': 'https://www.box.com/home',
        'label': 0,    },
    {
        'url': 'https://drive.dropbox.com',
        'label': 0,    },

    # --- Slack ---
    {
        'url': 'https://slack.com/signin',
        'label': 0,    },
    {
        'url': 'https://slack.com/help',
        'label': 0,    },
    {
        'url': 'https://slack.com/features',
        'label': 0,    },
    {
        'url': 'https://api.slack.com',
        'label': 0,    },
    {
        'url': 'https://status.slack.com',
        'label': 0,    },

    # --- Project Management ---
    {
        'url': 'https://trello.com/home',
        'label': 0,    },
    {
        'url': 'https://trello.com/templates',
        'label': 0,    },
    {
        'url': 'https://asana.com',
        'label': 0,    },
    {
        'url': 'https://clickup.com',
        'label': 0,    },
    {
        'url': 'https://notion.so',
        'label': 0,    },

    # --- Zoom ---
    {
        'url': 'https://zoom.us/signin',
        'label': 0,    },
    {
        'url': 'https://zoom.us/download',
        'label': 0,    },
    {
        'url': 'https://support.zoom.us',
        'label': 0,    },
    {
        'url': 'https://explore.zoom.us',
        'label': 0,    },
    {
        'url': 'https://zoom.us/pricing',
        'label': 0,    },

    # --- Reddit ---
    {
        'url': 'https://www.reddit.com/r/programming',
        'label': 0,    },
    {
        'url': 'https://www.reddit.com/r/machinelearning',
        'label': 0,    },
    {
        'url': 'https://www.reddit.com/login',
        'label': 0,    },
    {
        'url': 'https://old.reddit.com',
        'label': 0,    },
    {
        'url': 'https://www.reddithelp.com',
        'label': 0,    },

    # --- Dev Blogs & Communities ---
    {
        'url': 'https://medium.com/topic/technology',
        'label': 0,    },
    {
        'url': 'https://medium.com/topic/programming',
        'label': 0,    },
    {
        'url': 'https://dev.to',
        'label': 0,    },
    {
        'url': 'https://hashnode.com',
        'label': 0,    },
    {
        'url': 'https://freecodecamp.org/news',
        'label': 0,    },

    # --- Python Ecosystem ---
    {
        'url': 'https://pypi.org/project/numpy',
        'label': 0,    },
    {
        'url': 'https://pypi.org/project/pandas',
        'label': 0,    },
    {
        'url': 'https://pypi.org/project/scikit-learn',
        'label': 0,    },
    {
        'url': 'https://docs.python.org/3',
        'label': 0,    },
    {
        'url': 'https://realpython.com',
        'label': 0,    },

    # --- Misk ---
    {
        'url': 'https://hub.misk.org.sa/',
        'label': 0,    },

    # --- More Google Docs ---
    {
        'url': 'https://docs.google.com/document/u/',
        'label': 0,    },

    # === CLOUD STORAGE ABUSE - PHISHING (label=1) ===

    # Google Cloud Storage hosting phishing HTML pages
    {
        'url': 'https://storage.googleapis.com/localbuckjaw456/hreflyjaw.html#?Z289MSZzMT0yMjUwNDAwJnMyPTUxMjA2NDYzOCZzMz1HTEI=',
        'label': 1,    },
    {
        'url': 'https://storage.googleapis.com/bucket-xkq92/pay-now.html',
        'label': 1,    },
    {
        'url': 'https://storage.googleapis.com/delivery-fee-43x/customs.html',
        'label': 1,    },
    {
        'url': 'https://storage.googleapis.com/pklzbucket/login.html',
        'label': 1,    },
    {
        'url': 'https://storage.googleapis.com/rndm-bkt-7742/verify.html',
        'label': 1,    },
    {
        'url': 'https://firebasestorage.googleapis.com/v0/b/phish-app-x/o/index.html',
        'label': 1,    },
    {
        'url': 'https://firebasestorage.googleapis.com/v0/b/delivery-scam99/o/pay.html',
        'label': 1,    },

    # AWS S3 hosting phishing pages
    {
        'url': 'https://s3.amazonaws.com/bucket-phish-44/paypal-login.html',
        'label': 1,    },
    {
        'url': 'https://s3.amazonaws.com/random-bucket-77x/verify-account.html',
        'label': 1,    },
    {
        'url': 'https://s3.amazonaws.com/delivery-fee-confirm/payment.html',
        'label': 1,    },

    # Azure Blob Storage phishing
    {
        'url': 'https://scambucket.blob.core.windows.net/pages/login.html',
        'label': 1,    },
    {
        'url': 'https://phishstore99.blob.core.windows.net/public/verify.html',
        'label': 1,    },

    # === MALFORMED URLs (label=1) ===
    {
        'url': 'http:/paypal.com/login',
        'label': 1,    },
    {
        'url': 'http:/google.com@evil.xyz',
        'label': 1,    },
    {
        'url': 'http:/secure-bank.com/auth',
        'label': 1,    },
    {
        'url': 'https://account-verify.xyz',
        'label': 1,    },

    # === DELIVERY SCAM URLs (label=1) ===
    {
        'url': 'http://delivery-fee-payment.xyz/confirm',
        'label': 1,    },
    {
        'url': 'http://parcel-customs-fee.top/pay',
        'label': 1,    },
    {
        'url': 'http://shipment-hold-payment.ga/release',
        'label': 1,    },
    {
        'url': 'http://missed-delivery-reschedule.xyz/update',
        'label': 1,    },
    {
        'url': 'http://track-package-verify-address.top/confirm',
        'label': 1,    },

    # HTTP phishing (no SSL = higher risk)
    {'url': 'http://paypa1-secure-login.com/verify', 'label': 1},
    {'url': 'http://amazon-account-suspended.net/restore', 'label': 1},
    {'url': 'http://apple-id-verify.com/signin', 'label': 1},
    {'url': 'http://bankofamerica-secure.net/login', 'label': 1},
    {'url': 'http://microsoft-account-alert.com/confirm', 'label': 1},
    {'url': 'http://netflix-billing-update.com/payment', 'label': 1},
    {'url': 'http://google-security-alert.net/verify', 'label': 1},
    {'url': 'http://ebay-seller-suspended.com/appeal', 'label': 1},
    {'url': 'http://fedex-delivery-failed.net/reschedule', 'label': 1},
    {'url': 'http://irs-tax-refund-claim.com/submit', 'label': 1},

    # HTTPS legitimate URLs (secure = lower risk)
    {'url': 'https://appleid.apple.com/sign-in', 'label': 0},
    {'url': 'https://account.microsoft.com/security', 'label': 0},
    {'url': 'https://www.netflix.com/login', 'label': 0},
    {'url': 'https://www.ebay.com/mye/myebay/summary', 'label': 0},
    {'url': 'https://www.fedex.com/en-us/tracking.html', 'label': 0},
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
