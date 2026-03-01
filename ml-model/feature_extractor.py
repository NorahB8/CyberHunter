"""
Feature Extractor for CyberHunter ML Model
Extracts features from emails for ML training and prediction
"""

import re
from urllib.parse import urlparse

class FeatureExtractor:
    """Extract features from emails for ML training"""

    def __init__(self):
        # Suspicious keywords (English + Arabic)
        self.suspicious_keywords = [
            # English urgency
            'urgent', 'immediate', 'action required', 'suspended', 'verify now',
            'confirm identity', 'update required', 'asap', 'act now', 'today only',
            'confirm immediately', 'account will be closed', 'last chance',
            # English threats
            'unauthorized', 'suspicious activity', 'security alert', 'unusual activity',
            'compromised', 'blocked', 'locked',
            # English rewards
            'winner', 'prize', 'congratulations', 'claim', 'free gift', 'selected',
            # English financial
            'payment', 'invoice', 'refund', 'transaction', 'wire transfer',
            'bank account', 'credit card', 'cvv', 'pin',
            # English shipping
            'parcel', 'delivery', 'tracking', 'warehouse', 'unable to deliver',
            'missing information', 'business days',
            # Arabic urgency
            'عاجل', 'فوري', 'حالاً', 'ينتهي', 'تنتهي', 'معلق', 'تحقق الآن',
            'تصرف الآن', 'وقت محدود', 'اليوم فقط', 'أكد فوراً',
            # Arabic threats
            'محظور', 'غير مصرح', 'مخترق', 'تنبيه أمني', 'نشاط غير عادي',
            'مقفل', 'تم الحظر', 'إيقاف', 'تجميد',
            # Arabic personal info
            'كلمة المرور', 'كلمة السر', 'بطاقة ائتمان', 'حساب مصرفي',
            'رقم سري', 'رمز التحقق', 'الرقم السري', 'بيانات شخصية',
            # Arabic general
            'تحقق', 'حساب', 'تأكيد', 'تحديث', 'أمان', 'انقر', 'تسجيل الدخول',
            'مصرفي', 'بنك', 'فائز', 'جائزة', 'مجاني', 'يدعي', 'محدود',
            'طرد', 'شحنة', 'توصيل', 'تتبع', 'معلومات مفقودة'
        ]

        # Spam domain keywords
        self.suspicious_domain_patterns = [
            'wildzone', 'ultraprize', 'entryport', 'megasnap', 'flashvault',
            'quickfire', 'zonejump', 'rapidlink', 'freezone', 'netgrab',
            'instawin', 'prizepool', 'luckyzone', 'winfast', 'grabprize',
            'spam', 'temp', 'fake', 'scam', 'phish', 'suspicious', 'malware',
            'oceanpark', 'trip', 'entryway', 'giantreward', 'choresrecords',
            'junglerealm', 'pathway', 'gatehouse', 'superwin', 'antiwalmart',
            'verify', 'account', 'secure', 'update', 'confirm'
        ]

        # Legitimate brands and their domains
        self.legitimate_brands = {
            'dhl': ['dhl.com', 'dhl.de', 'dhl.co.uk'],
            'fedex': ['fedex.com', 'fedex.co.uk'],
            'paypal': ['paypal.com'],
            'amazon': ['amazon.com', 'amazon.sa', 'amazon.co.uk'],
            'microsoft': ['microsoft.com', 'outlook.com', 'live.com'],
            'apple': ['apple.com', 'icloud.com', 'email.apple.com'],
            'google': ['google.com', 'gmail.com'],
            'netflix': ['netflix.com', 'mailer.netflix.com'],
            'ebay': ['ebay.com'],
            'chase': ['chase.com'],
            'الراجحي': ['alrajhibank.com.sa'],
            'راجحي': ['alrajhibank.com.sa'],
            'sephora': ['sephora.com', 'sephora.sa', 'sephora-info-fr.com', 'sephora-info-me.com'],
            'loccitane': ['loccitane.com', 'email-loccitane.com'],
            'stc': ['stc.com.sa'],
            'موبايلي': ['mobily.com.sa']
        }

        # Suspicious username patterns
        self.username_patterns = [
            r'^[a-z]{3,8}\d{4,8}$',  # label623435
            r'^[A-Za-z]{8,}$',       # MguTYrJq
            r'^[a-z]{2,4}\d{2,4}$',
            r'^\d+[a-z]+\d+$'
        ]

    def _parse_input(self, input_string):
        """Parse email or URL into components for feature extraction

        Returns dict with:
        - domain: The domain name
        - username: Username from email or path from URL (NO query params)
        - is_url: Boolean indicating if input is a URL
        - full_path: Full URL path WITHOUT query parameters
        """
        if not input_string:
            return {'domain': '', 'username': '', 'is_url': False, 'full_path': ''}

        input_lower = input_string.lower()

        # Check if it's a URL
        if '://' in input_lower:
            try:
                parsed = urlparse(input_lower)
                # Use hostname (not netloc) to strip out user@info from URLs
                # e.g., http://google.com@evil.com → hostname is "evil.com"
                domain = parsed.hostname or parsed.netloc
                path = parsed.path.lstrip('/')
                # Use path as "username" for feature extraction
                # DO NOT include query parameters - they are legitimate tracking/analytics
                return {
                    'domain': domain,
                    'username': path,
                    'is_url': True,
                    'full_path': path  # Exclude query params from analysis
                }
            except:
                pass

        # Check if it's an email
        if '@' in input_lower:
            parts = input_lower.split('@')
            return {
                'domain': parts[1] if len(parts) > 1 else '',
                'username': parts[0],
                'is_url': False,
                'full_path': ''
            }

        # Fallback: treat as domain only
        return {'domain': input_lower, 'username': '', 'is_url': False, 'full_path': ''}

    def extract_features(self, email_data):
        """Extract feature vector from email or URL entry"""
        features = {}

        # Support both 'sender_email' (email entries) and 'url' (URL entries)
        sender_email = email_data.get('sender_email', email_data.get('url', '')).lower()
        sender_name = email_data.get('sender_name', '').lower()
        subject = email_data.get('subject', '').lower()
        body = email_data.get('body', '').lower()
        full_text = f"{sender_name} {subject} {body}"

        # Feature 1: Suspicious keyword count
        keyword_matches = sum(1 for kw in self.suspicious_keywords if kw in full_text)
        features['suspicious_keyword_count'] = min(keyword_matches, 10)

        # Feature 2: Keyword density
        word_count = len(full_text.split())
        features['keyword_density'] = keyword_matches / max(word_count, 1)

        # Feature 3: Has suspicious username pattern
        features['suspicious_username'] = self._check_username(sender_email)

        # Feature 4: Domain spam keywords
        features['domain_spam_keywords'] = self._check_domain_spam(sender_email)

        # Feature 5: Subdomain count
        features['subdomain_count'] = self._count_subdomains(sender_email)

        # Feature 6: Domain length
        features['domain_length'] = self._get_domain_length(sender_email)

        # Feature 7: Gibberish domain score
        features['gibberish_score'] = self._check_gibberish(sender_email)

        # Feature 8: Brand impersonation
        features['brand_impersonation'] = self._check_brand_impersonation(
            sender_email, sender_name, body
        )

        # Feature 9: Free email provider with company name
        features['free_email_company'] = self._check_free_email(sender_email, sender_name)

        # Feature 10: Suspicious TLD
        features['suspicious_tld'] = self._check_tld(sender_email)

        # Feature 11: Has digits in username
        features['username_digit_count'] = self._count_username_digits(sender_email)

        # Feature 12: Email contains IP address
        features['has_ip_address'] = self._check_ip_address(sender_email)

        # Feature 13: Long digit sequence in domain
        features['long_digit_sequence'] = self._check_long_digits(sender_email)

        # Feature 14: Excessive hyphens
        features['hyphen_count'] = self._count_hyphens(sender_email)

        # Feature 15: Arabic character ratio
        features['arabic_ratio'] = self._arabic_ratio(full_text)

        # Feature 16: Urgency level
        urgency_words = ['urgent', 'immediate', 'now', 'today', 'asap', 'عاجل', 'فوري', 'الآن']
        features['urgency_count'] = sum(1 for word in urgency_words if word in full_text)

        # Feature 17: Personal info request
        personal_info = ['password', 'credit card', 'ssn', 'pin', 'cvv',
                        'كلمة المرور', 'بطاقة ائتمان', 'رقم سري']
        features['personal_info_request'] = sum(1 for word in personal_info if word in full_text)

        # Feature 18: Vowel ratio in domain
        features['domain_vowel_ratio'] = self._domain_vowel_ratio(sender_email)

        # Feature 19: Direct typosquatting detection in domain
        features['typosquatting'] = self._check_typosquatting(sender_email)

        # Feature 20: Legitimate email username pattern (negative = safe signal)
        features['legitimate_username'] = self._check_legitimate_username(sender_email)

        # Feature 21: Sender name vs domain mismatch
        features['name_domain_mismatch'] = self._check_name_domain_mismatch(
            sender_email, sender_name
        )

        # Feature 22: Domain age (new/suspicious domain detection)
        features['domain_age_suspicious'] = self._check_domain_age(sender_email)

        return features

    def _check_username(self, email):
        parsed = self._parse_input(email)
        username = parsed['username']

        if not username:
            return 0

        # For URLs, check if path contains gibberish
        if parsed['is_url']:
            # Split path by /
            path_parts = username.split('/')
            for part in path_parts:
                # Check if path segment is gibberish (random chars)
                if len(part) > 5 and self._is_gibberish_string(part):
                    return 1

        # For emails, check username patterns
        for pattern in self.username_patterns:
            if re.match(pattern, username):
                return 1
        return 0

    def _check_domain_spam(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain']

        if not domain:
            return 0

        # Count spam keywords in domain
        count = sum(1 for keyword in self.suspicious_domain_patterns if keyword in domain)

        # For URLs, also check path for spam patterns
        if parsed['is_url'] and parsed['full_path']:
            path = parsed['full_path'].lower()
            # Increment count if path contains suspicious patterns
            if any(keyword in path for keyword in self.suspicious_domain_patterns):
                count += 1

        return min(count, 5)

    def _count_subdomains(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain']

        if not domain:
            return 0

        return max(0, domain.count('.') - 1)

    def _get_domain_length(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain']
        if not domain:
            return 0
        return min(len(domain), 100)

    def _check_gibberish(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain']
        if not domain:
            return 0
        domain_name = domain.split('.')[0]

        # Check for repeated patterns
        if len(domain_name) > 10:
            half = len(domain_name) // 2
            if domain_name[:half] == domain_name[half:half*2]:
                return 1
        return 0

    def _check_brand_impersonation(self, email, sender_name, body):
        parsed = self._parse_input(email)
        domain = parsed['domain'].lower() if parsed['domain'] else email.lower()
        full_text = f"{sender_name} {body}".lower()

        for brand, legitimate_domains in self.legitimate_brands.items():
            # Check if brand is mentioned in sender name, body, OR the domain/path
            brand_in_text = brand in full_text
            brand_in_domain = brand in domain

            if brand_in_text or brand_in_domain:
                is_legitimate = any(legit in domain for legit in legitimate_domains)
                if not is_legitimate:
                    return 1

        # Check for brand name in subdomain (e.g., paypal.evil-site.com)
        domain_parts = domain.split('.')
        if len(domain_parts) >= 3:
            subdomains = '.'.join(domain_parts[:-2]).lower()
            for brand in self.legitimate_brands:
                if brand in subdomains:
                    # The brand is in a subdomain but the root domain isn't legitimate
                    root_domain = '.'.join(domain_parts[-2:])
                    is_legitimate = any(root_domain in legit for legit in self.legitimate_brands[brand])
                    if not is_legitimate:
                        return 1

        # Check for @ in URL (credential attack: http://google.com@evil.com)
        if parsed['is_url'] and '@' in email:
            return 1

        return 0

    def _check_free_email(self, email, sender_name):
        free_providers = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
        companies = ['paypal', 'amazon', 'bank', 'microsoft', 'apple', 'fedex', 'dhl']

        email_lower = email.lower()
        name_lower = sender_name.lower()

        if any(provider in email_lower for provider in free_providers):
            if any(company in name_lower for company in companies):
                return 1
        return 0

    def _check_tld(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain'].lower() if parsed['domain'] else email.lower()
        suspicious_tlds = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.club']
        return 1 if any(domain.endswith(tld) for tld in suspicious_tlds) else 0

    def _count_username_digits(self, email):
        parsed = self._parse_input(email)
        username = parsed['username']
        if not username:
            return 0
        return min(sum(c.isdigit() for c in username), 10)

    def _check_ip_address(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain']
        if not domain:
            return 0
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        return 1 if re.search(ip_pattern, domain) else 0

    def _check_long_digits(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain']
        if not domain:
            return 0
        return 1 if re.search(r'\d{6,}', domain) else 0

    def _count_hyphens(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain']
        if not domain:
            return 0
        return min(domain.count('-'), 5)

    def _arabic_ratio(self, text):
        arabic_chars = len(re.findall(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]', text))
        total_chars = len(re.findall(r'[a-zA-Z\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]', text))
        return arabic_chars / max(total_chars, 1)

    def _domain_vowel_ratio(self, email):
        parsed = self._parse_input(email)
        domain = parsed['domain']
        if not domain:
            return 0.4
        domain_name = domain.split('.')[0]
        vowels = sum(1 for c in domain_name if c.lower() in 'aeiou')
        letters = sum(1 for c in domain_name if c.isalpha())
        return vowels / max(letters, 1)

    def _check_typosquatting(self, email):
        """Detect typosquatting/homograph attacks in domain name"""
        parsed = self._parse_input(email)
        domain = parsed['domain']
        if not domain:
            return 0
        domain = domain.lower()

        # FIRST: Check if this is a LEGITIMATE brand domain - don't flag if it is!
        legitimate_domains_list = []
        for brand, domains in self.legitimate_brands.items():
            legitimate_domains_list.extend(domains)

        # If the domain IS a legitimate brand domain, it's NOT typosquatting
        if any(legit_domain in domain for legit_domain in legitimate_domains_list):
            return 0

        # Common brand typosquatting patterns
        typosquat_patterns = {
            'paypa1': 'paypal',      # 1 instead of l
            'paypa|': 'paypal',      # | instead of l
            'g00gle': 'google',      # 0 instead of o
            'micr0soft': 'microsoft', # 0 instead of o
            'appl3': 'apple',        # 3 instead of e
            'app1e': 'apple',        # 1 instead of l
            'amaz0n': 'amazon',      # 0 instead of second o
            'ama0zon': 'amazon',     # 0 instead of first o
            '4mazon': 'amazon',      # 4 instead of a
            'faceb00k': 'facebook',  # 0 instead of o
            'fac3book': 'facebook',  # 3 instead of e
            'netf1ix': 'netflix',    # 1 instead of l
            'netfl1x': 'netflix',    # 1 instead of i
            'netf1ix': 'netflix',    # 1 instead of li
            'n3tflix': 'netflix',    # 3 instead of e
            'twitt3r': 'twitter',    # 3 instead of e
            'linkdin': 'linkedin',   # missing e
            'l1nkedin': 'linkedin',  # 1 instead of i
            'dh1': 'dhl',            # 1 instead of l
            'fed3x': 'fedex',        # 3 instead of e
            'f3dex': 'fedex',        # 3 instead of first e
            'f3d3x': 'fedex',        # 3 instead of both e's
            'g0ogle': 'google',      # 0 instead of first o
            'goog1e': 'google',      # 1 instead of l
            'go0gle': 'google',      # 0 instead of second o
            'micosoft': 'microsoft', # missing r
            'microsfot': 'microsoft', # transposed letters
            'paypal1': 'paypal',     # extra 1
            'paypai': 'paypal',      # i instead of l
            'ch4se': 'chase',        # 4 instead of a
            'we11sfargo': 'wellsfargo', # 1 instead of l
            's0ephora': 'sephora',   # 0 instead of e
            'seph0ra': 'sephora',    # 0 instead of o
            'seph1ra': 'sephora',    # 1 instead of o
            'seph6ra': 'sephora',    # 6 instead of o
            'sephura': 'sephora',    # u instead of o (misspelling)
            'sephoora': 'sephora',   # double o
            'sephu0ra': 'sephora',   # u and 0
            'sephora1': 'sephora',   # 1 instead of l (trailing)
            's3phora': 'sephora',    # 3 instead of e
            'eb4y': 'ebay',          # 4 instead of a
            'ebai': 'ebay',          # i instead of y (misspelling)
            '3bay': 'ebay',          # 3 instead of e
        }

        # Check if domain matches any typosquatting pattern
        for typo, original in typosquat_patterns.items():
            if typo in domain:  # Check entire domain, not just first part
                return 1

        # Check for common character substitutions
        # Look for patterns like: o→0, l→1, e→3, i→1, s→5, a→4
        # ONLY flag if the brand appears in normalized version but NOT in the original
        # (i.e., the numbers are actually disguising the brand name)
        if any(char in domain for char in ['0', '1', '3', '4', '5', '6']):
            normalized = domain.replace('0', 'o').replace('1', 'l').replace('3', 'e').replace('5', 's').replace('4', 'a').replace('6', 'b')
            for brand in ['paypal', 'google', 'microsoft', 'apple', 'amazon', 'facebook', 'dhl', 'fedex', 'sephora', 'ebay', 'netflix']:
                if brand in normalized and brand not in domain:
                    return 1

        return 0

    def _check_legitimate_username(self, email):
        """Check if email username matches common legitimate patterns.
        Returns 1 if legitimate (safe signal), 0 otherwise."""
        parsed = self._parse_input(email)
        if parsed['is_url']:
            return 0  # Not applicable for URLs
        username = parsed['username'].lower()
        if not username:
            return 0

        # Common legitimate business email prefixes
        legitimate_prefixes = [
            'info', 'contact', 'support', 'help', 'sales', 'team',
            'hello', 'admin', 'office', 'service', 'billing',
            'noreply', 'no-reply', 'do-not-reply', 'donotreply',
            'newsletters', 'newsletter', 'news', 'updates', 'marketing',
            'notifications', 'notification', 'notify', 'alert', 'alerts',
            'customercare', 'customer-care', 'customerservice',
            'feedback', 'enquiry', 'inquiry', 'press', 'media', 'hr',
            'careers', 'jobs', 'orders', 'shipping', 'returns',
            'welcome', 'community', 'events', 'webmaster', 'postmaster'
        ]

        if username in legitimate_prefixes:
            return 1
        return 0

    def _check_name_domain_mismatch(self, email, sender_name):
        """Detect mismatch between sender display name and email domain.
        E.g., Western name 'Charles Koch' from Japanese domain ruby.plala.or.jp"""
        parsed = self._parse_input(email)
        if parsed['is_url'] or not sender_name:
            return 0

        domain = parsed['domain'].lower() if parsed['domain'] else ''
        name = sender_name.lower().strip()
        if not domain or not name:
            return 0

        # Check for Japanese/Asian ISP domains with Western names
        jp_domains = ['.jp', '.or.jp', '.co.jp', '.ne.jp']
        cn_domains = ['.cn', '.com.cn']
        kr_domains = ['.kr', '.co.kr']

        # Check if name looks Western (ASCII letters, common Western pattern)
        is_western_name = bool(re.match(r'^[a-z\s\-\.\']+$', name)) and len(name.split()) >= 2

        if is_western_name:
            if any(domain.endswith(d) for d in jp_domains + cn_domains + kr_domains):
                return 1

        # Check for Japanese ISP consumer domains with any non-Japanese name
        jp_isps = ['plala.or.jp', 'ocn.ne.jp', 'biglobe.ne.jp', 'nifty.com',
                    'so-net.ne.jp', 'dti.ne.jp', 'infoweb.ne.jp']
        if any(domain.endswith(isp) for isp in jp_isps) and is_western_name:
            return 1

        return 0

    def _check_domain_age(self, email):
        """Check if domain shows signs of being new/temporary.
        Uses heuristic approach (no WHOIS) for speed.
        Returns 1 if domain appears suspicious/temporary, 0 otherwise."""
        parsed = self._parse_input(email)
        domain = parsed['domain']
        if not domain:
            return 0

        domain_lower = domain.lower()

        # Check if it's a legitimate brand domain first
        legitimate_domains_list = []
        for domains in self.legitimate_brands.values():
            legitimate_domains_list.extend(domains)

        if any(legit_domain in domain_lower for legit_domain in legitimate_domains_list):
            return 0  # Known legitimate brand - safe

        # Check for disposable/free TLDs (strong signal of temporary domains)
        disposable_tlds = [
            '.tk', '.ml', '.ga', '.cf', '.gq',  # Freenom free TLDs
            '.xyz', '.top', '.club', '.site', '.online', '.website',  # Cheap TLDs
            '.win', '.bid', '.trade', '.stream', '.download'  # Suspicious TLDs
        ]

        for tld in disposable_tlds:
            if domain_lower.endswith(tld):
                return 1  # Likely temporary/new domain

        # Check for patterns common in new phishing domains
        # Long domains with hyphens + suspicious keywords
        if '-' in domain_lower and len(domain_lower) > 25:
            spam_keywords = ['verify', 'secure', 'login', 'account', 'update',
                           'confirm', 'check', 'validation', 'security']
            if any(kw in domain_lower for kw in spam_keywords):
                return 1

        return 0

    def _is_gibberish_string(self, text):
        """Check if a string appears to be randomly generated gibberish

        ONLY detects truly random gibberish, NOT legitimate URL paths
        """
        if not text or len(text) < 8:  # Increased from 5 to 8
            return False

        text_original = text
        text = text.lower()

        # Whitelist common legitimate patterns FIRST
        # Article/documentation IDs and common path segments
        if re.search(r'(answer|article|page|id|kb|ht|view|post|item|product|doc|ref|redirect|track|gp)', text):
            return False

        # Support/help/tracking paths
        if any(word in text for word in ['support', 'help', 'docs', 'legal', 'privacy', 'terms',
                                         'about', 'contact', 'mail', 'account', 'buy', 'purchase',
                                         'itunes', 'store', 'shop', 'product', 'track', 'shipment',
                                         'delivery', 'order', 'customer', 'service']):
            return False

        # Common URL path abbreviations (Amazon uses 'gp', 'dp', etc.)
        if re.search(r'^(gp|dp|ap|ref|exec|obidos|redirect|track|redir|go|r)$', text):
            return False

        # Pure numeric strings (like IDs) are NOT gibberish
        if text.replace('-', '').replace('_', '').isdigit():
            return False

        # Single letter or very short segments are NOT gibberish
        if len(text) <= 2:
            return False

        # Remove file extensions
        text = re.sub(r'\.(html?|php|asp|jsp|txt|pdf|xml|json)$', '', text)

        if len(text) < 8:
            return False

        # Count vowels
        vowels = sum(1 for c in text if c in 'aeiou')
        letters = sum(1 for c in text if c.isalpha())

        # Need substantial letters to evaluate
        if letters < 6:
            return False

        vowel_ratio = vowels / letters

        # ONLY flag EXTREMELY low vowel ratios (< 12%)
        # Most real words have at least 15% vowels
        if vowel_ratio < 0.12:
            # But check if it's just an abbreviation or brand name
            if letters < 10:  # Short strings might be abbreviations
                return False
            return True

        # DISABLED: Consonant cluster check causes too many false positives
        # Many legitimate paths have clusters like "https", "github", etc.

        # ONLY flag if path looks like true random gibberish
        # Check for very specific random patterns: long strings with random digit insertion
        alphanumeric = sum(1 for c in text if c.isalnum())
        digits = sum(1 for c in text if c.isdigit())

        # Only flag if VERY suspicious: >50% digits AND >12 chars AND low vowel ratio
        if alphanumeric > 12 and digits > alphanumeric * 0.5 and vowel_ratio < 0.15:
            return True

        return False
