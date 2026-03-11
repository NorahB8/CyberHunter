// CyberHunter Content Script - Real-time Email Scanner with ML
class EmailPhishingDetector {
    constructor() {
        // ML API Configuration
        this.API_URL = 'http://localhost:5000/api/analyze';
        this.USE_ML_API = true; // Set to false to use only rule-based detection
        this.API_TIMEOUT = 5000; // 5 second timeout for API calls

        this.suspiciousPatterns = {
            urgentLanguage: /urgent|immediate|action required|suspended|verify now|confirm identity|update required|asap|act now|today only|confirm immediately|account will be closed|last chance|عاجل|ضروري|فوري|مطلوب|معلق|تعليق|الآن|اليوم|حالاً|ينتهي|تنتهي|تحقق الآن|تصرف الآن|وقت محدود|اليوم فقط|أكد فوراً|سيتم إغلاق الحساب|آخر فرصة|خلال 24 ساعة/i,
            threatLanguage: /unauthorized|suspicious activity|security alert|unusual activity|compromised|blocked|locked|غير مصرح|نشاط مشبوه|تحذير|موقوف|حظر|محظور|مخترق|تنبيه أمني|نشاط غير عادي|مقفل|تم الحظر|إيقاف|تجميد/i,
            rewards: /winner|prize|congratulations|claim|free gift|selected|فائز|جائزة|مبروك|يدعي|مجاني|هدية/i,
            financialTerms: /payment|invoice|refund|transaction|wire transfer|bank account|دفع|فاتورة|استرداد|تحويل|حساب بنكي|مصرفي|حساب مصرفي/i,
            personalInfo: /ssn|social security|password|pin|credit card|account number|cvv|verification code|كلمة المرور|كلمة السر|رقم سري|بطاقة ائتمان|رقم الحساب|رمز التحقق|الرقم السري|بيانات شخصية|معلومات البطاقة|تاريخ الانتهاء/i,
            shippingScam: /parcel|delivery|tracking|warehouse|manufacturer|unable to deliver|missing information|business days|طرد|شحنة|توصيل|تتبع|مستودع|مصنع|غير قادر على التسليم|معلومات مفقودة|أيام عمل|رقم التتبع/i
        };

        this.knownPhishingIndicators = {
            mismatchedUrls: true,
            spoofedSender: true,
            suspiciousAttachments: true,
            urgencyTactics: true
        };

        // Legitimate brand domains
        this.legitimateBrands = {
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
            // Arabic banks
            'الراجحي': ['alrajhibank.com.sa'],
            'راجحي': ['alrajhibank.com.sa'],
            'الأهلي': ['alahli.com'],
            'أهلي': ['alahli.com'],
            'سامبا': ['samba.com'],
            'الرياض': ['riyadbank.com'],
            'رياض': ['riyadbank.com'],
            'البنك العربي': ['arabbank.com'],
            'sephora': ['sephora.com', 'sephora.sa', 'sephora-info-fr.com', 'sephora-info-me.com'],
            'loccitane': ['loccitane.com', 'email-loccitane.com'],
            "l'occitane": ['loccitane.com', 'email-loccitane.com'],
            'stc': ['stc.com.sa'],
            'موبايلي': ['mobily.com.sa'],
            'زين': ['sa.zain.com']
        };

        // Suspicious domain patterns for spam detection
        this.suspiciousDomainPatterns = [
            'wildzone', 'ultraprize', 'entryport', 'megasnap', 'flashvault',
            'quickfire', 'zonejump', 'rapidlink', 'freezone', 'netgrab',
            'instawin', 'prizepool', 'luckyzone', 'winfast', 'grabprize',
            'spam', 'temp', 'fake', 'scam', 'phish', 'suspicious', 'malware',
            'oceanpark', 'trip', 'entryway', 'giantreward', 'choresrecords',
            'junglerealm', 'pathway', 'gatehouse', 'superwin', 'antiwalmart'
        ];

        // Suspicious username patterns
        this.suspiciousUsernamePatterns = [
            /^[a-z]{3,8}\d{4,8}$/,  // word + many digits (e.g., grant612671, label623435)
            /^[A-Za-z]{8,}$/,       // random long char sequence (e.g., MguTYrJq)
            /^[a-z]{2,4}\d{2,4}$/,  // short word + digits
            /^\d+[a-z]+\d+$/,       // digits-letters-digits pattern
            /^[A-Z][a-z]{2,}[A-Z][a-z]{2,}$/  // MixedCaseRandom pattern
        ];

        this.scannedEmails = new Set();
        this.scanResults = new Map(); // Store scan results for re-display
        this.init();
    }

    init() {
        console.log('CyberHunter: Email scanner initialized');
        this.detectEmailClient();
        this.startMonitoring();
    }

    testEmailExtraction() {
        console.log('CyberHunter: Testing email extraction...');
        const emails = document.querySelectorAll(this.emailSelector);
        emails.forEach((email, index) => {
            const data = this.extractEmailData(email);
            console.log(`Email ${index + 1}:`, {
                sender: data.sender,
                senderEmail: data.senderEmail,
                hasSenderEmail: !!data.senderEmail && data.senderEmail.includes('@')
            });
        });
    }

    detectEmailClient() {
        const hostname = window.location.hostname;
        
        if (hostname.includes('mail.google.com')) {
            this.emailClient = 'gmail';
            this.emailSelector = 'div[role="main"] div[data-message-id]';
        } else if (hostname.includes('outlook')) {
            this.emailClient = 'outlook';
            this.emailSelector = '[role="region"][aria-label*="message"]';
        }
    }

    startMonitoring() {
        // Monitor for new emails being opened
        const observer = new MutationObserver((mutations) => {
            this.scanVisibleEmails();
        });

        observer.observe(document.body, {
            childList: true,
            subtree: true
        });

        // Initial scan
        setTimeout(() => this.scanVisibleEmails(), 2000);
    }

    scanVisibleEmails() {
        const emails = document.querySelectorAll(this.emailSelector);

        emails.forEach(email => {
            const emailId = this.getEmailId(email);

            // Check if the email element already has a banner
            const hasWarning = email.querySelector('.cyberhunter-warning');
            const hasSafe = email.querySelector('.cyberhunter-safe');

            if (hasWarning || hasSafe) {
                // Banner already exists, skip
                return;
            }

            // If we've scanned this email before, re-display the result
            if (this.scanResults.has(emailId)) {
                const cachedResult = this.scanResults.get(emailId);
                if (cachedResult.riskLevel === 'high' || cachedResult.riskLevel === 'medium') {
                    this.displayWarning(email, cachedResult, emailId);
                    // Re-highlight phishing links (DOM was re-rendered by Gmail)
                    if (cachedResult.phishingLinks && cachedResult.phishingLinks.length > 0) {
                        this.highlightPhishingLinks(email, cachedResult.phishingLinks);
                    }
                } else {
                    this.displaySafeIndicator(email, emailId);
                }
                return;
            }

            // New email, analyze it
            if (!this.scannedEmails.has(emailId)) {
                this.scannedEmails.add(emailId);
                this.analyzeEmail(email, emailId);
            }
        });
    }

    getEmailId(emailElement) {
        if (this.emailClient === 'gmail') {
            return emailElement.getAttribute('data-message-id') || 
                   emailElement.getAttribute('data-legacy-message-id') ||
                   Math.random().toString(36);
        }
        return Math.random().toString(36);
    }

    async analyzeEmail(emailElement, emailId) {
        try {
            const emailData = this.extractEmailData(emailElement);

            // DEBUG: Log extraction result
            console.log('CyberHunter: Extracted email data:', {
                sender: emailData.sender,
                senderEmail: emailData.senderEmail,
                hasEmail: !!emailData.senderEmail
            });

            // If email extraction failed, try alternative method
            if (!emailData.senderEmail || !emailData.senderEmail.includes('@')) {
                console.warn('CyberHunter: Email extraction failed, using fallback');
                if (emailData.sender && emailData.sender.includes('@')) {
                    emailData.senderEmail = emailData.sender;
                } else {
                    console.error('CyberHunter: Cannot extract sender email, marking as suspicious');
                    emailData.senderEmail = 'unknown@suspicious.invalid';
                }
            }

            // Try ML API first, fallback to rule-based
            let analysis;
            let phishingLinks = [];

            if (this.USE_ML_API) {
                console.log('CyberHunter: Attempting ML API analysis...');

                // Scan links in parallel with email analysis
                const [emailAnalysis, scannedLinks] = await Promise.all([
                    this.analyzeWithMLAPI(emailData),
                    this.scanLinksWithML(emailData.links)
                ]);

                analysis = emailAnalysis;
                phishingLinks = scannedLinks;

                if (!analysis) {
                    console.warn('CyberHunter: ML API unavailable, falling back to rule-based detection');
                    analysis = this.performMLAnalysis(emailData);
                    analysis.detectionMethod = 'rule-based (API unavailable)';
                }
            } else {
                console.log('CyberHunter: Using rule-based detection (API disabled)');
                analysis = this.performMLAnalysis(emailData);
                analysis.detectionMethod = 'rule-based';
            }

            // If phishing links detected, upgrade risk level
            if (phishingLinks.length > 0) {
                analysis.phishingLinks = phishingLinks;
                analysis.riskScore = Math.max(analysis.riskScore, 85); // Upgrade to high risk
                analysis.riskLevel = 'high';

                // Initialize riskReasons if it doesn't exist
                if (!analysis.riskReasons) {
                    analysis.riskReasons = [];
                }
                analysis.riskReasons.push(`${phishingLinks.length} phishing link(s) detected in email`);
                console.log(`CyberHunter: Email flagged as high risk due to ${phishingLinks.length} phishing links`);
            }

            // Store the result for re-display later
            this.scanResults.set(emailId, analysis);

            if (analysis.riskLevel === 'high' || analysis.riskLevel === 'medium') {
                this.displayWarning(emailElement, analysis, emailId);

                // Highlight phishing links in the email body
                if (analysis.phishingLinks && analysis.phishingLinks.length > 0) {
                    this.highlightPhishingLinks(emailElement, analysis.phishingLinks);
                }
            } else {
                this.displaySafeIndicator(emailElement, emailId);
            }

            // Log to storage
            this.logScan(emailId, analysis);
        } catch (error) {
            console.error('CyberHunter: Error analyzing email', error);
        }
    }

    async analyzeWithMLAPI(emailData) {
        try {
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), this.API_TIMEOUT);

            const response = await fetch(this.API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    url: emailData.senderEmail,
                    sender_name: emailData.sender,
                    email_body: emailData.body
                }),
                signal: controller.signal
            });

            clearTimeout(timeoutId);

            if (!response.ok) {
                console.error(`CyberHunter: ML API returned error ${response.status}`);
                return null;
            }

            const mlResult = await response.json();

            // Convert ML result to extension format
            console.log('CyberHunter: ML API Result:', {
                risk: mlResult.risk_score,
                classification: mlResult.classification,
                is_phishing: mlResult.is_phishing
            });

            return {
                riskScore: mlResult.risk_score,
                riskLevel: mlResult.classification === 'high_risk' ? 'high' :
                          mlResult.classification === 'medium_risk' ? 'medium' : 'low',
                features: this.convertMLFeatures(mlResult),
                recommendations: mlResult.feature_analysis || [],
                detectionMethod: 'machine-learning (Random Forest)',
                modelAccuracy: mlResult.model_accuracy
            };

        } catch (error) {
            if (error.name === 'AbortError') {
                console.warn('CyberHunter: ML API request timeout');
            } else {
                console.warn('CyberHunter: ML API request failed:', error.message);
            }
            return null;
        }
    }

    async scanLinksWithML(links) {
        // Scan all links in email using ML API
        const phishingLinks = [];

        if (!this.USE_ML_API || links.length === 0) {
            return phishingLinks;
        }

        console.log(`CyberHunter: Scanning ${links.length} links with ML API...`);

        for (const link of links) {
            try {
                // Skip non-http links
                if (!link.href || (!link.href.startsWith('http://') && !link.href.startsWith('https://'))) {
                    continue;
                }

                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), this.API_TIMEOUT);

                const response = await fetch(this.API_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        url: link.href,
                        sender_name: '',
                        email_body: ''
                    }),
                    signal: controller.signal
                });

                clearTimeout(timeoutId);

                if (response.ok) {
                    const mlResult = await response.json();

                    // If ML detects high risk (70%+), flag this link as phishing
                    if (mlResult.risk_score >= 70) {
                        phishingLinks.push({
                            url: link.href,
                            text: link.text,
                            riskScore: mlResult.risk_score,
                            classification: mlResult.classification,
                            analysis: mlResult.feature_analysis || []
                        });
                        console.log(`CyberHunter: Phishing link detected: ${link.href} (${mlResult.risk_score}%)`);
                    }
                }
            } catch (error) {
                // Silently continue if link scan fails
                console.warn(`CyberHunter: Failed to scan link ${link.href}:`, error.message);
            }
        }

        return phishingLinks;
    }

    convertMLFeatures(mlResult) {
        // Convert ML model features to extension feature format
        const features = mlResult.email_features || {};

        return {
            suspiciousLanguage: {
                score: features.suspicious_keyword_count > 0 ? features.suspicious_keyword_count * 10 : 0,
                matches: []
            },
            urlMismatch: {
                score: 0,
                count: 0,
                examples: []
            },
            senderAuthenticity: {
                score: features.free_email_company ? 50 : 0,
                issues: []
            },
            urgencyLevel: {
                score: features.urgency_count * 15,
                level: features.urgency_count > 3 ? 'high' :
                       features.urgency_count > 1 ? 'medium' : 'low'
            },
            linkCount: {
                score: 0,
                count: 0
            },
            personalInfoRequest: {
                score: features.personal_info_request > 0 ? 50 : 0,
                requests: []
            },
            domainReputation: {
                score: 0,
                reputation: 'unknown'
            },
            gibberishDomain: {
                score: features.gibberish_score ? 100 : 0,
                isGibberish: features.gibberish_score === 1,
                reason: features.gibberish_score ? 'ML detected gibberish domain' : ''
            },
            brandImpersonation: {
                score: features.brand_impersonation ? 100 : 0,
                issues: features.brand_impersonation ? ['Brand impersonation detected by ML'] : []
            },
            senderNameMismatch: {
                score: features.free_email_company ? 100 : 0,
                issues: features.free_email_company ? ['Company using free email (ML detected)'] : []
            },
            emailAddressAnalysis: {
                score: (features.suspicious_username ? 100 : 0) +
                       (features.domain_spam_keywords * 20),
                issues: [],
                username: { score: features.suspicious_username ? 100 : 0 },
                domain: { score: features.domain_spam_keywords * 20 }
            }
        };
    }

    extractEmailData(emailElement) {
        let subject = '';
        let sender = '';
        let body = '';
        let links = [];
        let senderEmail = '';

        if (this.emailClient === 'gmail') {
            // Extract subject
            const subjectElement = emailElement.querySelector('h2, [data-subject]');
            subject = subjectElement ? subjectElement.textContent : '';

            // Strategy 1: Try email attribute
            const senderElement = emailElement.querySelector('[email]');
            if (senderElement && senderElement.getAttribute('email')) {
                senderEmail = senderElement.getAttribute('email');
                sender = senderElement.textContent || senderElement.getAttribute('name') || '';
            }

            // Strategy 2: Parse from textContent if email attribute failed
            if (!senderEmail) {
                const senderText = emailElement.querySelector('[data-hovercard-id]')?.textContent || '';
                // Look for email pattern in text: "Name <email@domain.com>"
                const emailMatch = senderText.match(/<([^>]+@[^>]+)>/);
                if (emailMatch) {
                    senderEmail = emailMatch[1].trim();
                    sender = senderText.split('<')[0].trim();
                } else if (senderText.includes('@')) {
                    // Plain email without brackets
                    senderEmail = senderText.trim();
                    sender = senderText.trim();
                }
            }

            // Strategy 3: Look for span with email class
            if (!senderEmail) {
                const emailSpan = emailElement.querySelector('span.go, span.gD');
                if (emailSpan) {
                    senderEmail = emailSpan.getAttribute('email') || emailSpan.textContent;
                }
            }

            // Extract body
            const bodyElement = emailElement.querySelector('[data-message-id] div[dir="ltr"]');
            body = bodyElement ? bodyElement.textContent : '';

            // Extract links
            const linkElements = emailElement.querySelectorAll('a[href]');
            links = Array.from(linkElements).map(a => ({
                text: a.textContent,
                href: a.href,
                display: a.getAttribute('href')
            }));
        }

        return { subject, sender, senderEmail, body, links };
    }

    performMLAnalysis(emailData) {
        const features = {
            suspiciousLanguage: this.detectSuspiciousLanguage(emailData),
            urlMismatch: this.detectURLMismatch(emailData.links),
            senderAuthenticity: this.checkSenderAuthenticity(emailData),
            urgencyLevel: this.assessUrgency(emailData),
            linkCount: this.analyzeLinkCount(emailData.links),
            personalInfoRequest: this.detectPersonalInfoRequest(emailData),
            domainReputation: this.checkDomainReputation(emailData),
            gibberishDomain: this.detectGibberishDomain(emailData.senderEmail),
            brandImpersonation: this.detectBrandImpersonation(
                emailData.senderEmail,
                emailData.sender,
                emailData.body
            ),
            senderNameMismatch: this.detectSenderNameMismatch(
                emailData.senderEmail,
                emailData.sender
            ),
            emailAddressAnalysis: this.analyzeEmailAddress(emailData.senderEmail)
        };

        const riskScore = this.calculateRiskScore(features);
        const riskLevel = this.classifyRisk(riskScore);

        return {
            riskScore,
            riskLevel,
            features,
            recommendations: this.generateRecommendations(features, riskLevel)
        };
    }

    detectSuspiciousLanguage(emailData) {
        const text = `${emailData.subject} ${emailData.body}`.toLowerCase();
        let score = 0;
        const matches = [];

        Object.entries(this.suspiciousPatterns).forEach(([category, pattern]) => {
            if (pattern.test(text)) {
                score += 20;
                matches.push(category);
            }
        });

        return { score: Math.min(score, 100), matches };
    }

    detectURLMismatch(links) {
        let mismatchCount = 0;
        const suspicious = [];

        links.forEach(link => {
            try {
                const displayedUrl = link.text.trim();
                const actualUrl = new URL(link.href);

                // Check if text looks like a URL but doesn't match actual URL
                if (displayedUrl.includes('.com') || displayedUrl.includes('http')) {
                    if (!link.href.includes(displayedUrl)) {
                        mismatchCount++;
                        suspicious.push({
                            displayed: displayedUrl,
                            actual: actualUrl.hostname
                        });
                    }
                }

                // Check for suspicious domains
                const suspiciousTLDs = ['.tk', '.ml', '.ga', '.cf', '.gq', '.xyz'];
                if (suspiciousTLDs.some(tld => actualUrl.hostname.endsWith(tld))) {
                    mismatchCount++;
                    suspicious.push({
                        url: actualUrl.hostname,
                        reason: 'Suspicious TLD'
                    });
                }
            } catch (e) {
                // Invalid URL
            }
        });

        return {
            score: Math.min(mismatchCount * 30, 100),
            count: mismatchCount,
            examples: suspicious.slice(0, 3)
        };
    }

    checkSenderAuthenticity(emailData) {
        let score = 0;
        const issues = [];

        // Check for display name vs email mismatch
        const sender = emailData.sender.toLowerCase();
        const email = emailData.senderEmail.toLowerCase();

        // Common spoofing patterns
        const trustedBrands = ['paypal', 'amazon', 'microsoft', 'apple', 'google', 'bank', 'sephora', 'loccitane'];
        
        trustedBrands.forEach(brand => {
            if (sender.includes(brand) && !email.includes(brand)) {
                score += 40;
                issues.push(`Display name mentions ${brand} but email domain doesn't match`);
            }
        });

        // Check for suspicious domains
        if (email.includes('secure') || email.includes('verify') || email.includes('account')) {
            score += 20;
            issues.push('Email contains suspicious keywords');
        }

        return { score: Math.min(score, 100), issues };
    }

    assessUrgency(emailData) {
        const urgencyWords = [
            'immediately', 'urgent', 'asap', 'now', 'today',
            'expires', 'limited time', 'act now', 'don\'t wait'
        ];

        const text = `${emailData.subject} ${emailData.body}`.toLowerCase();
        let count = 0;

        urgencyWords.forEach(word => {
            if (text.includes(word)) count++;
        });

        return {
            score: Math.min(count * 15, 100),
            level: count > 3 ? 'high' : count > 1 ? 'medium' : 'low'
        };
    }

    analyzeLinkCount(links) {
        const count = links.length;
        let score = 0;

        if (count > 10) score = 60;
        else if (count > 5) score = 30;
        else if (count === 0) score = 10;

        return { score, count };
    }

    detectPersonalInfoRequest(emailData) {
        const text = `${emailData.subject} ${emailData.body}`.toLowerCase();
        let score = 0;
        const requests = [];

        const personalInfoTerms = {
            'password': 40,
            'credit card': 50,
            'social security': 50,
            'ssn': 50,
            'account number': 40,
            'pin': 40,
            'verification code': 30
        };

        Object.entries(personalInfoTerms).forEach(([term, points]) => {
            if (text.includes(term)) {
                score += points;
                requests.push(term);
            }
        });

        return { score: Math.min(score, 100), requests };
    }

    checkDomainReputation(emailData) {
        // Simulate domain reputation check
        const commonFreeEmail = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com'];
        const email = emailData.senderEmail.toLowerCase();

        let score = 0;
        let reputation = 'unknown';

        // Business email from free provider claiming to be from company
        if (commonFreeEmail.some(domain => email.includes(domain))) {
            const sender = emailData.sender.toLowerCase();
            if (sender.includes('paypal') || sender.includes('amazon') ||
                sender.includes('bank') || sender.includes('microsoft')) {
                score = 70;
                reputation = 'suspicious - free email claiming to be business';
            }
        }

        return { score, reputation };
    }

    detectGibberishDomain(senderEmail) {
        try {
            const domain = senderEmail.split('@')[1];
            if (!domain) return { score: 0, isGibberish: false };

            // Remove TLD
            const domainWithoutTLD = domain.substring(0, domain.lastIndexOf('.'));

            // Check for repeated patterns (like "sngvotlasngvotla")
            if (domainWithoutTLD.length > 10) {
                const half = Math.floor(domainWithoutTLD.length / 2);
                const firstHalf = domainWithoutTLD.substring(0, half);
                const secondHalf = domainWithoutTLD.substring(half, half * 2);

                if (firstHalf === secondHalf) {
                    return {
                        score: 100,
                        isGibberish: true,
                        reason: 'Repeated pattern in domain name'
                    };
                }
            }

            // Check vowel ratio (legitimate domains have ~40% vowels)
            const vowels = 'aeiouAEIOU';
            const letters = domainWithoutTLD.replace(/[^a-zA-Z]/g, '');
            const vowelCount = Array.from(letters).filter(c => vowels.includes(c)).length;
            const vowelRatio = letters.length > 0 ? vowelCount / letters.length : 0;

            if (vowelRatio < 0.2) {
                return {
                    score: 100,
                    isGibberish: true,
                    reason: 'Too few vowels, appears randomly generated'
                };
            } else if (vowelRatio < 0.3) {
                return {
                    score: 70,
                    isGibberish: true,
                    reason: 'Low vowel ratio, suspicious domain'
                };
            }

            // Check for excessive consonant clusters
            const consonantClusters = domainWithoutTLD.match(/[^aeiouAEIOU]{4,}/g);
            if (consonantClusters && consonantClusters.length > 0) {
                return {
                    score: 80,
                    isGibberish: true,
                    reason: 'Excessive consonant clusters'
                };
            }

            return { score: 0, isGibberish: false };
        } catch (e) {
            return { score: 0, isGibberish: false };
        }
    }

    detectBrandImpersonation(senderEmail, sender, emailBody) {
        const senderLower = sender.toLowerCase();
        const emailLower = senderEmail.toLowerCase();
        const bodyLower = emailBody.toLowerCase();

        let score = 0;
        let issues = [];

        for (const [brand, legitimateDomains] of Object.entries(this.legitimateBrands)) {
            // Check if brand is mentioned in sender name or email body
            const brandMentioned = senderLower.includes(brand) || bodyLower.includes(brand);

            if (brandMentioned) {
                // Check if email domain is legitimate for this brand
                const isLegitimate = legitimateDomains.some(domain =>
                    emailLower.includes(domain)
                );

                if (!isLegitimate) {
                    score = 100;
                    issues.push(`Claims to be from ${brand.toUpperCase()} but uses unauthorized domain`);
                    break;
                }
            }
        }

        return { score, issues };
    }

    detectSenderNameMismatch(senderEmail, senderName) {
        if (!senderEmail || !senderName) {
            return { score: 0, issues: [] };
        }

        const emailLower = senderEmail.toLowerCase();
        const nameLower = senderName.toLowerCase();
        let score = 0;
        let issues = [];

        try {
            const domain = senderEmail.split('@')[1];

            // Free email providers
            const freeProviders = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
                                   'aol.com', 'mail.com', 'protonmail.com'];

            // Check if sender name mentions a brand
            for (const [brand, legitimateDomains] of Object.entries(this.legitimateBrands)) {
                if (nameLower.includes(brand)) {
                    // Brand in name, check if email is from free provider
                    if (freeProviders.some(provider => emailLower.includes(provider))) {
                        score = 100;
                        issues.push(`Company name "${brand.toUpperCase()}" using free email service`);
                        return { score, issues };
                    }

                    // Check if domain matches brand
                    const isLegitimate = legitimateDomains.some(d => domain.includes(d));
                    if (!isLegitimate) {
                        score = 100;
                        issues.push(`Sender name claims ${brand.toUpperCase()} but domain doesn't match`);
                        return { score, issues };
                    }
                }
            }

            // Check for excessive trademark symbols
            const trademarkCount = (senderName.match(/[©®™]/g) || []).length;
            if (trademarkCount > 1) {
                score += 70;
                issues.push('Excessive trademark symbols in sender name');
            }

        } catch (e) {
            // Error parsing email
        }

        return { score, issues };
    }

    analyzeUsername(emailAddress) {
        if (!emailAddress || !emailAddress.includes('@')) {
            return { score: 0, issues: [] };
        }

        try {
            const username = emailAddress.split('@')[0].trim().toLowerCase();
            let score = 0;
            let issues = [];

            // Check for legitimate business email usernames FIRST (safe signal)
            const legitimateUsernames = [
                'info', 'contact', 'support', 'help', 'sales', 'team',
                'hello', 'admin', 'office', 'service', 'billing',
                'noreply', 'no-reply', 'do-not-reply', 'donotreply',
                'newsletters', 'newsletter', 'news', 'updates', 'marketing',
                'notifications', 'notification', 'notify', 'alert', 'alerts',
                'customercare', 'customer-care', 'customerservice',
                'feedback', 'enquiry', 'inquiry', 'press', 'media', 'hr',
                'careers', 'jobs', 'orders', 'shipping', 'returns',
                'welcome', 'community', 'events', 'webmaster', 'postmaster'
            ];
            if (legitimateUsernames.includes(username)) {
                return { score: 0, issues: [], isLegitimate: true };
            }

            // Very short usernames (1-2 chars) are suspicious
            if (username.length <= 2) {
                return { score: 80, issues: ['Very short username'] };
            }

            // Check against suspicious patterns
            for (const pattern of this.suspiciousUsernamePatterns) {
                if (pattern.test(username)) {
                    return {
                        score: 100,
                        issues: ['Username matches spam pattern (word+digits or random characters)']
                    };
                }
            }

            // Check for random character sequences (low vowel ratio in long usernames)
            if (username.length >= 8) {
                const vowels = (username.match(/[aeiou]/gi) || []).length;
                if (vowels === 0) {
                    return { score: 100, issues: ['Username has no vowels (random characters)'] };
                } else if (username.match(/^[a-zA-Z]+$/) && vowels / username.length < 0.2) {
                    return { score: 90, issues: ['Username has too few vowels (suspicious pattern)'] };
                }
            }

            // Check for excessive digits
            const digitCount = (username.match(/\d/g) || []).length;
            if (digitCount > 4) {
                score = 70;
                issues.push('Username contains many digits');
            }

            return { score, issues };
        } catch (e) {
            return { score: 0, issues: [] };
        }
    }

    analyzeDomain(domain) {
        if (!domain) {
            return { score: 0, issues: [] };
        }

        const domainLower = domain.toLowerCase();
        let score = 0;
        let issues = [];

        // Check for IP address pattern in domain
        if (/\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/.test(domain)) {
            return { score: 100, issues: ['Domain contains IP address'] };
        }

        // Check for long digit sequences (8+ digits in a row)
        if (/\d{8,}/.test(domain)) {
            score += 80;
            issues.push('Domain contains long digit sequence');
        }

        // Check for suspicious domain keywords
        for (const keyword of this.suspiciousDomainPatterns) {
            if (domainLower.includes(keyword)) {
                score += 60;
                issues.push(`Domain contains spam keyword: ${keyword}`);
                break;
            }
        }

        // Count subdomains (excessive = suspicious)
        const subdomainCount = domain.split('.').length - 2; // Subtract 2 for domain.tld
        if (subdomainCount >= 4) {
            score += 70;
            issues.push(`Excessive subdomains (${subdomainCount + 1} levels)`);
        } else if (subdomainCount >= 3) {
            score += 50;
            issues.push(`Many subdomains (${subdomainCount + 1} levels)`);
        }

        // Check for very long domain names (50+ chars)
        if (domain.length > 50) {
            score += 40;
            issues.push('Very long domain name');
        }

        // Check for excessive hyphens (often used in spam domains)
        const hyphenCount = (domain.match(/-/g) || []).length;
        if (hyphenCount >= 3) {
            score += 50;
            issues.push('Excessive hyphens in domain');
        }

        return { score: Math.min(100, score), issues };
    }

    analyzeEmailAddress(emailAddress) {
        if (!emailAddress || !emailAddress.includes('@')) {
            return { score: 0, issues: [] };
        }

        try {
            const [username, domain] = emailAddress.split('@');

            const usernameAnalysis = this.analyzeUsername(emailAddress);
            const domainAnalysis = this.analyzeDomain(domain);

            // Overall risk is weighted average (domain slightly more important)
            const overallScore = (usernameAnalysis.score * 0.4) + (domainAnalysis.score * 0.6);

            return {
                score: Math.round(overallScore),
                issues: [...usernameAnalysis.issues, ...domainAnalysis.issues],
                username: usernameAnalysis,
                domain: domainAnalysis
            };
        } catch (e) {
            return { score: 0, issues: [] };
        }
    }

    calculateRiskScore(features) {
        const weights = {
            suspiciousLanguage: 0.10,
            urlMismatch: 0.15,
            senderAuthenticity: 0.10,
            urgencyLevel: 0.06,
            linkCount: 0.04,
            personalInfoRequest: 0.08,
            domainReputation: 0.04,
            gibberishDomain: 0.12,
            brandImpersonation: 0.16,
            senderNameMismatch: 0.12,
            emailAddressAnalysis: 0.18  // High weight for sophisticated spam detection
        };

        let totalScore = 0;

        Object.entries(features).forEach(([feature, data]) => {
            const featureWeight = weights[feature] || 0.05;
            totalScore += (data.score || 0) * featureWeight;
        });

        return Math.min(Math.round(totalScore), 100);
    }

    classifyRisk(score) {
        if (score >= 70) return 'high';
        if (score >= 40) return 'medium';
        return 'low';
    }

    generateRecommendations(features, riskLevel) {
        const recommendations = [];

        if (riskLevel === 'high') {
            recommendations.push('⚠️ Do not click any links in this email');
            recommendations.push('🚫 Do not provide any personal information');
            recommendations.push('🗑️ Consider deleting this email immediately');
        }

        if (features.emailAddressAnalysis && features.emailAddressAnalysis.score > 60) {
            if (features.emailAddressAnalysis.issues.length > 0) {
                features.emailAddressAnalysis.issues.forEach(issue => {
                    recommendations.push(`🚨 ${issue}`);
                });
            } else {
                recommendations.push('🚨 Sender email address shows spam/phishing characteristics');
            }
        }

        if (features.gibberishDomain && features.gibberishDomain.isGibberish) {
            recommendations.push(`🔤 Sender domain is gibberish: ${features.gibberishDomain.reason}`);
        }

        if (features.brandImpersonation && features.brandImpersonation.issues.length > 0) {
            recommendations.push(`🏢 ${features.brandImpersonation.issues[0]}`);
        }

        if (features.senderNameMismatch && features.senderNameMismatch.issues.length > 0) {
            recommendations.push(`👤 ${features.senderNameMismatch.issues[0]}`);
        }

        if (features.urlMismatch.count > 0) {
            recommendations.push('🔗 Link URLs do not match displayed text');
        }

        if (features.senderAuthenticity.score > 50) {
            recommendations.push('📧 Sender email may be spoofed');
        }

        if (features.personalInfoRequest.requests.length > 0) {
            recommendations.push('🔒 Email requests sensitive information');
        }

        if (features.urgencyLevel.level === 'high') {
            recommendations.push('⏰ Uses urgency tactics to pressure quick action');
        }

        return recommendations;
    }

    displayWarning(emailElement, analysis, emailId) {
        // Remove any existing warning
        const existingWarning = emailElement.querySelector('.cyberhunter-warning');
        if (existingWarning) existingWarning.remove();

        const warning = document.createElement('div');
        warning.className = `cyberhunter-warning cyberhunter-${analysis.riskLevel}`;
        warning.id = `cyberhunter-${emailId}`;
        warning.innerHTML = `
            <div class="cyberhunter-header">
                <span class="cyberhunter-icon">${analysis.riskLevel === 'high' ? '🛑' : '⚠️'}</span>
                <span class="cyberhunter-title">
                    ${analysis.riskLevel === 'high' ? 'HIGH RISK - Likely Phishing' : 'Suspicious Email Detected'}
                </span>
                <span class="cyberhunter-score">${analysis.riskScore}% Risk</span>
            </div>
            <div class="cyberhunter-recommendations">
                ${analysis.recommendations.map(rec => `<div class="cyberhunter-rec">${rec}</div>`).join('')}
            </div>
            ${analysis.phishingLinks && analysis.phishingLinks.length > 0 ? `
                <div class="cyberhunter-phishing-links" style="margin: 10px 0; padding: 10px; background: rgba(255, 0, 0, 0.1); border-left: 3px solid #ff3366; border-radius: 4px;">
                    <div style="font-weight: bold; margin-bottom: 5px;">🚨 ${analysis.phishingLinks.length} Phishing Link(s) Detected:</div>
                    ${analysis.phishingLinks.map((link, index) => `
                        <div style="margin: 5px 0; padding: 5px; background: rgba(0, 0, 0, 0.05); border-radius: 3px; font-size: 0.9em;">
                            <div style="font-weight: bold; color: #ff3366;">${index + 1}. ${link.text || 'Suspicious Link'}</div>
                            <div style="color: #666; word-break: break-all; margin: 2px 0;">${link.url}</div>
                            <div style="color: #ff3366; font-weight: bold;">Risk: ${link.riskScore}%</div>
                            ${link.analysis && link.analysis.length > 0 ? `
                                <div style="margin-top: 3px; font-size: 0.85em;">${link.analysis[0]}</div>
                            ` : ''}
                        </div>
                    `).join('')}
                </div>
            ` : ''}
            <div class="cyberhunter-footer">
                ${analysis.detectionMethod === 'machine-learning (Random Forest)'
                    ? `🤖 ML Detection: ${Math.round(analysis.modelAccuracy)}% accuracy`
                    : '🛡️ Rule-Based Detection'}
            </div>
        `;

        // Insert at the top of the email
        emailElement.insertBefore(warning, emailElement.firstChild);
    }

    displaySafeIndicator(emailElement, emailId) {
        const existingIndicator = emailElement.querySelector('.cyberhunter-safe');
        if (existingIndicator) return;

        const indicator = document.createElement('div');
        indicator.className = 'cyberhunter-safe';
        indicator.id = `cyberhunter-${emailId}`;
        indicator.innerHTML = `
            <span class="cyberhunter-icon">✓</span>
            <span>Scanned by CyberHunter - No threats detected</span>
        `;

        emailElement.insertBefore(indicator, emailElement.firstChild);
    }

    async logScan(emailId, analysis) {
        try {
            const result = await chrome.storage.local.get(['scanHistory']);
            const history = result.scanHistory || [];

            history.unshift({
                id: emailId,
                timestamp: new Date().toISOString(),
                riskLevel: analysis.riskLevel,
                riskScore: analysis.riskScore
            });

            // Keep only last 100 scans
            if (history.length > 100) history.pop();

            await chrome.storage.local.set({ scanHistory: history });
        } catch (error) {
            console.error('CyberHunter: Error logging scan', error);
        }
    }

    highlightPhishingLinks(emailElement, phishingLinks) {
        // Find and visually highlight phishing links in the email body
        try {
            const allLinks = emailElement.querySelectorAll('a[href]');

            allLinks.forEach(linkElement => {
                const href = linkElement.href;

                // Check if this link is in the phishing links list
                const isPhishing = phishingLinks.some(phishingLink =>
                    href === phishingLink.url ||
                    href.includes(phishingLink.url) ||
                    phishingLink.url.includes(href)
                );

                if (isPhishing) {
                    const matchedLink = phishingLinks.find(pl =>
                        href === pl.url || href.includes(pl.url) || pl.url.includes(href)
                    );

                    // Add visual warning styles
                    linkElement.style.cssText = `
                        background: linear-gradient(135deg, #ff3366 0%, #ff6b9d 100%) !important;
                        color: white !important;
                        padding: 2px 6px !important;
                        border-radius: 4px !important;
                        border: 2px solid #ff0044 !important;
                        text-decoration: line-through !important;
                        font-weight: bold !important;
                        box-shadow: 0 0 10px rgba(255, 51, 102, 0.5) !important;
                        cursor: not-allowed !important;
                        position: relative !important;
                        display: inline-block !important;
                    `;

                    // Add warning icon before the link
                    if (!linkElement.querySelector('.cyberhunter-link-warning')) {
                        const warningIcon = document.createElement('span');
                        warningIcon.className = 'cyberhunter-link-warning';
                        warningIcon.textContent = '🚨 ';
                        warningIcon.style.cssText = 'font-size: 1em; margin-right: 2px;';
                        linkElement.insertBefore(warningIcon, linkElement.firstChild);
                    }

                    // Add tooltip with risk score
                    linkElement.title = `⚠️ PHISHING LINK DETECTED!\nRisk Score: ${matchedLink.riskScore}%\nDO NOT CLICK THIS LINK!\n${matchedLink.analysis[0] || 'Detected as malicious by ML model'}`;

                    // Prevent clicking
                    linkElement.addEventListener('click', (e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        alert(`⚠️ PHISHING LINK BLOCKED!\n\nThis link has been identified as phishing (${matchedLink.riskScore}% risk).\n\nDO NOT visit this URL: ${href}\n\nReason: ${matchedLink.analysis[0] || 'Detected as malicious'}`);
                        return false;
                    }, { capture: true });

                    console.log(`CyberHunter: Highlighted phishing link: ${href}`);
                }
            });
        } catch (error) {
            console.error('CyberHunter: Error highlighting phishing links', error);
        }
    }
}

// Initialize detector
const detector = new EmailPhishingDetector();
