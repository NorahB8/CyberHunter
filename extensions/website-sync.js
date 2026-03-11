// Syncs website login session → extension storage
const SESSION_KEY = 'cyberhunter_session';

function syncToExtension(user) {
    try {
        chrome.runtime.sendMessage({ action: 'syncSession', user });
    } catch (e) {
        // Extension context may be inactive, ignore
    }
}

// On page load: only sync TO extension if website has an active session
// (never clear extension session just because the website tab isn't logged in)
const stored = localStorage.getItem(SESSION_KEY);
if (stored) {
    syncToExtension(JSON.parse(stored));
}

// Sync on explicit login/logout action from the website (same-tab)
window.addEventListener('message', (e) => {
    if (e.source === window && e.data && e.data.type === 'cyberhunter_auth') {
        syncToExtension(e.data.user); // null = explicit logout
    }
});

// Sync when localStorage changes from another tab
window.addEventListener('storage', (e) => {
    if (e.key === SESSION_KEY) {
        syncToExtension(e.newValue ? JSON.parse(e.newValue) : null);
    }
});
