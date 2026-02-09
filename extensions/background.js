// CyberHunter Background Service Worker

// Initialize extension
chrome.runtime.onInstalled.addListener((details) => {
    if (details.reason === 'install') {
        console.log('CyberHunter installed successfully');
        
        // Initialize storage
        chrome.storage.local.set({
            scanHistory: [],
            settings: {
                enabled: true,
                autoScan: true,
                notificationsEnabled: true
            }
        });

        // Open welcome page
        chrome.tabs.create({
            url: chrome.runtime.getURL('popup.html')
        });
    }
});

// Listen for messages from content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'phishingDetected') {
        handlePhishingDetection(request.data, sender.tab);
        sendResponse({ success: true });
    }
    
    if (request.action === 'getSettings') {
        chrome.storage.local.get(['settings'], (result) => {
            sendResponse(result.settings || {});
        });
        return true; // Keep channel open for async response
    }
    
    return false;
});

async function handlePhishingDetection(data, tab) {
    const { riskLevel, riskScore } = data;

    // Show notification for high-risk emails
    if (riskLevel === 'high') {
        try {
            await chrome.notifications.create({
                type: 'basic',
                iconUrl: 'icons/icon128.png',
                title: '🛑 CyberHunter Alert',
                message: `High-risk phishing email detected (${riskScore}% risk)`,
                priority: 2
            });
        } catch (error) {
            console.error('Error showing notification:', error);
        }
    }

    // Update badge
    updateBadge(tab.id, riskLevel);
}

function updateBadge(tabId, riskLevel) {
    const colors = {
        high: '#ff3366',
        medium: '#ffaa00',
        low: '#00ff88'
    };

    const texts = {
        high: '!',
        medium: '⚠',
        low: '✓'
    };

    chrome.action.setBadgeBackgroundColor({
        color: colors[riskLevel] || '#00ff88',
        tabId: tabId
    });

    chrome.action.setBadgeText({
        text: texts[riskLevel] || '',
        tabId: tabId
    });
}

// Clear badge when tab is closed
chrome.tabs.onRemoved.addListener((tabId) => {
    chrome.action.setBadgeText({ text: '', tabId: tabId });
});

// Monitor navigation to email clients
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete') {
        const emailClients = ['mail.google.com', 'outlook.live.com', 'outlook.office.com'];
        
        if (emailClients.some(client => tab.url?.includes(client))) {
            console.log('CyberHunter: Email client detected, activating protection');
        }
    }
});

console.log('CyberHunter background service worker loaded');
