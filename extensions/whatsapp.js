// CyberHunter - WhatsApp Web Phishing Detection
class WhatsAppPhishingDetector {
    constructor() {
        this.API_URL = 'http://localhost:5000/api/analyze';
        this.API_TIMEOUT = 5000;
        this.scannedMessages = new Set();

        this.suspiciousPatterns = {
            urgency:     /urgent|immediately|act now|expires|limited time|today only|24 hours|verify now|confirm now|click here now|عاجل|فوري|الآن|اليوم فقط|خلال 24 ساعة/i,
            prizes:      /winner|won|prize|congratulations|claim|free gift|selected|reward|lottery|jackpot|فائز|جائزة|مبروك|مجاني|هدية|يانصيب/i,
            credentials: /password|pin|otp|verification code|credit card|bank account|national id|copy of id|send your id|photo of your id|picture of id|كلمة المرور|رقم سري|بيانات البنك|الهوية/i,
            financial:   /send money|wire transfer|western union|bitcoin|crypto|wallet address|payment required|advance fee|أرسل مبلغ|تحويل|عملة رقمية|رسوم/i,
            socialEngineering: /جربه|جرب الرابط|جالي فعلاً|وصلني فعلاً|try it|try the link|it actually worked|i got paid|i received|share this link|forward this|أنا استلمت|وصلني مبلغ|كسبت فعلاً/i,
            threats:     /suspended|blocked|account will be closed|unauthorized access|security breach|تعليق|محظور|إغلاق الحساب|اختراق/i
        };

        this.shortUrlDomains = [
            'bit.ly', 'tinyurl.com', 't.co', 'goo.gl', 'ow.ly',
            'is.gd', 'buff.ly', 'adf.ly', 'shorte.st', 'clck.ru'
        ];

        // Suspicious TLDs commonly used in scams
        this.suspiciousTLDs = [
            '.buzz', '.xyz', '.tk', '.ml', '.ga', '.cf', '.gq',
            '.top', '.club', '.icu', '.cyou', '.monster', '.rest',
            '.fit', '.uno', '.fun', '.site', '.online', '.space'
        ];

        // Currency amount pattern (e.g. E£19,000 / $5,000 / LE 2000)
        this.moneyPattern = /([E£$€¥₹LE]{1,3}[\s]?\d[\d,\.]+|\d[\d,\.]+\s*(?:dollars?|euros?|pounds?|جنيه|ريال|دولار|يورو))/i;

        console.log('CyberHunter: WhatsApp detector created');
        this.init();
    }

    init() {
        // WhatsApp loads slowly — retry until messages are found
        let attempts = 0;
        const tryStart = () => {
            attempts++;
            const ready = document.querySelector('div[data-id], div[data-testid="msg-container"]');
            if (ready || attempts > 20) {
                console.log('CyberHunter: Starting WhatsApp scan after', attempts, 'attempts');
                this.startMonitoring();
            } else {
                setTimeout(tryStart, 1000);
            }
        };
        setTimeout(tryStart, 2000);
    }

    startMonitoring() {
        this.scanVisibleMessages();
        const observer = new MutationObserver(() => this.scanVisibleMessages());
        observer.observe(document.body, { childList: true, subtree: true });
    }

    scanVisibleMessages() {
        // WhatsApp uses data-id on message rows; incoming start with "false_"
        const allMessages = document.querySelectorAll(
            'div[data-id^="false_"], div[data-testid="msg-container"]'
        );

        console.log('CyberHunter: Found', allMessages.length, 'incoming messages');

        allMessages.forEach(msg => this.processMessage(msg));
    }

    getMessageId(el) {
        return el.getAttribute('data-id') ||
               el.closest('[data-id]')?.getAttribute('data-id') ||
               el.innerText.slice(0, 60);
    }

    extractText(el) {
        // Try multiple selectors WhatsApp uses for message text
        const selectors = [
            'span.selectable-text.copyable-text',
            'span[class*="selectable-text"]',
            'div[class*="copyable-text"] span',
            'span[dir="ltr"]',
            'span[dir="rtl"]'
        ];
        for (const sel of selectors) {
            const found = el.querySelector(sel);
            if (found && found.innerText.trim()) return found.innerText.trim();
        }
        return el.innerText?.trim() || '';
    }

    extractLinks(el) {
        // Get anchor tags
        const anchorLinks = [...el.querySelectorAll('a[href]')].map(a => a.href);
        // Also extract URLs from raw text (WhatsApp doesn't always wrap links in <a>)
        const text = el.innerText || '';
        const urlRegex = /https?:\/\/[^\s\u200B\u00A0]+/gi;
        const textLinks = [...(text.match(urlRegex) || [])];
        return [...new Set([...anchorLinks, ...textLinks])];
    }

    extractSender(el) {
        // Group chats: sender name is in a span before the message body
        const senderEl = el.querySelector('span[aria-label][dir], [data-pre-plain-text]');
        if (!senderEl) return 'Unknown';
        const raw = senderEl.getAttribute('data-pre-plain-text') || senderEl.getAttribute('aria-label') || '';
        const match = raw.match(/\]\s*(.+?):\s*$/);
        return match ? match[1].trim() : raw.trim() || 'Unknown';
    }

    countSuspiciousKeywords(text) {
        let count = 0;
        Object.values(this.suspiciousPatterns).forEach(p => {
            if (p.test(text)) count++;
        });
        return count;
    }

    hasShortUrl(links) {
        return links.some(link => {
            try {
                const host = new URL(link).hostname.replace('www.', '');
                return this.shortUrlDomains.includes(host);
            } catch { return false; }
        });
    }

    hasSuspiciousUrl(links) {
        return links.some(link => {
            try {
                const host = new URL(link).hostname;
                if (/^\d{1,3}(\.\d{1,3}){3}$/.test(host)) return true;  // IP address
                if (host.split('.').length > 4) return true;              // too many subdomains
                if (host.length > 50) return true;                        // very long domain
                if (this.suspiciousTLDs.some(tld => host.endsWith(tld))) return true; // scam TLD
                if (this.isGibberishDomain(host)) return true;            // random chars
                return false;
            } catch { return false; }
        });
    }

    isGibberishDomain(host) {
        const name = host.split('.')[0];
        if (name.length < 4) return false;
        // High consonant ratio = gibberish (xgegg, sngvotla, etc.)
        const vowels = (name.match(/[aeiou]/gi) || []).length;
        const ratio = vowels / name.length;
        if (ratio < 0.3) return true; // less than 30% vowels
        // Repeated characters pattern (xgegg → gg repeated)
        if (/(.)\1{2,}/.test(name)) return true;
        // Starts with rare consonant combos
        if (/^[xzqkvw]{2}/i.test(name)) return true;
        return false;
    }

    async analyzeMessage(msgElement, msgId) {
        const body   = this.extractText(msgElement);
        const links  = this.extractLinks(msgElement);
        const sender = this.extractSender(msgElement);

        if (!body && links.length === 0) return;

        console.log('CyberHunter: Analyzing WhatsApp message:', body.slice(0, 60));

        let riskScore = 0;
        let reasons   = [];

        // Rule-based first (always runs)
        const keywordHits = this.countSuspiciousKeywords(body);
        riskScore += keywordHits * 20;
        if (keywordHits > 0) reasons.push(`Contains ${keywordHits} suspicious keyword(s)`);

        if (this.suspiciousPatterns.credentials.test(body)) {
            riskScore = Math.min(riskScore + 30, 100);
            reasons.push('Asks for personal information or ID');
        }
        if (this.suspiciousPatterns.financial.test(body)) {
            riskScore = Math.min(riskScore + 25, 100);
            reasons.push('Contains financial request or money transfer');
        }
        if (this.hasShortUrl(links)) {
            riskScore = Math.min(riskScore + 20, 100);
            reasons.push('Contains shortened URL — destination hidden');
        }
        if (this.hasSuspiciousUrl(links)) {
            riskScore = Math.min(riskScore + 35, 100);
            reasons.push('Contains suspicious or scam-associated link');
        }
        if (links.length > 0 && this.moneyPattern.test(body)) {
            riskScore = Math.min(riskScore + 25, 100);
            reasons.push('Message contains a link with a money amount — possible scam');
        }
        if (this.suspiciousPatterns.socialEngineering.test(body)) {
            riskScore = Math.min(riskScore + 30, 100);
            reasons.push('Uses social proof ("I got money, try it") — common scam tactic');
        }

        // Try ML API for additional scoring
        try {
            const controller = new AbortController();
            const timer = setTimeout(() => controller.abort(), this.API_TIMEOUT);

            const res = await fetch(this.API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    url: `whatsapp_contact@whatsapp.net`,
                    sender_name: sender,
                    email_body: body + ' ' + links.join(' ')
                }),
                signal: controller.signal
            });
            clearTimeout(timer);

            if (res.ok) {
                const result = await res.json();
                const mlScore = result.risk_score || 0;
                // Blend rule-based and ML
                riskScore = Math.max(riskScore, mlScore * 0.6 + riskScore * 0.4);
                if (result.feature_analysis?.length) {
                    reasons = [...new Set([...reasons, ...result.feature_analysis])];
                }
            }
        } catch (e) {
            console.log('CyberHunter: ML API unavailable, using rule-based only');
        }

        console.log('CyberHunter: Risk score:', riskScore, 'Reasons:', reasons);

        if (riskScore >= 35) {
            this.showWarning(msgElement, riskScore, reasons);
        } else {
            this.showSafeBadge(msgElement, riskScore);
        }
    }

    processMessage(msgElement) {
        const msgId = this.getMessageId(msgElement);
        if (this.scannedMessages.has(msgId)) return;
        this.scannedMessages.add(msgId);
        this.analyzeMessage(msgElement, msgId);
    }

    showSafeBadge(msgElement, riskScore) {
        if (msgElement.querySelector('.ch-wa-badge')) return;

        const badge = document.createElement('div');
        badge.className = 'ch-wa-badge';
        badge.style.cssText = `
            display: inline-flex;
            align-items: center;
            gap: 5px;
            background: rgba(0,200,100,0.12);
            border-left: 3px solid #00c864;
            border-radius: 4px;
            padding: 3px 8px;
            margin: 4px 0 2px 0;
            font-size: 11px;
            font-family: Arial, sans-serif;
            color: #aaa;
        `;
        badge.innerHTML = `<span style="color:#00c864;">✓ CyberHunter</span> Safe — ${Math.round(riskScore)}% risk`;
        this._insertBanner(msgElement, badge);
    }

    showWarning(msgElement, riskScore, reasons) {
        if (msgElement.querySelector('.ch-wa-warning')) return;

        const isHigh  = riskScore >= 70;
        const color   = isHigh ? '#ff3366' : '#ffaa00';
        const label   = isHigh ? '🚨 HIGH RISK MESSAGE' : '⚠ SUSPICIOUS MESSAGE';
        const bgColor = isHigh ? 'rgba(255,51,102,0.15)' : 'rgba(255,170,0,0.15)';

        const banner = document.createElement('div');
        banner.className = 'ch-wa-warning';
        banner.style.cssText = `
            background: ${bgColor};
            border-left: 4px solid ${color};
            border-radius: 6px;
            padding: 8px 12px;
            margin: 6px 0 2px 0;
            font-size: 12px;
            font-family: Arial, sans-serif;
            color: #fff;
            max-width: 420px;
            box-sizing: border-box;
            z-index: 9999;
        `;

        const reasonsHtml = reasons.slice(0, 3)
            .map(r => `<div style="margin-top:3px;color:#555;font-size:11px;">• ${r}</div>`)
            .join('');

        banner.innerHTML = `
            <div style="display:flex;align-items:center;justify-content:space-between;">
                <span style="color:${color};font-weight:bold;">${label}</span>
                <span style="color:#aaa;font-size:11px;">${Math.round(riskScore)}% risk</span>
            </div>
            ${reasonsHtml}
        `;

        this._insertBanner(msgElement, banner);
    }

    _insertBanner(msgElement, el) {
        // Try to find the inner text container to insert before it
        const textContainer =
            msgElement.querySelector('div.copyable-text') ||
            msgElement.querySelector('[data-pre-plain-text]') ||
            msgElement.querySelector('span.selectable-text')?.closest('div') ||
            msgElement.querySelector('div > div > div');

        if (textContainer && textContainer.parentNode) {
            textContainer.parentNode.insertBefore(el, textContainer);
        } else {
            msgElement.prepend(el);
        }
    }
}

// Only run on WhatsApp Web
if (window.location.hostname === 'web.whatsapp.com') {
    console.log('CyberHunter: WhatsApp Web detected, loading scanner...');
    new WhatsAppPhishingDetector();
}
