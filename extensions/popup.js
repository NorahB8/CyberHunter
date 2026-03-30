// CyberHunter Popup Script
document.addEventListener('DOMContentLoaded', async () => {
    loadStats();
    loadRecentScans();
    initAuth();

    document.getElementById('websiteLink').addEventListener('click', (e) => {
        e.preventDefault();
        chrome.runtime.sendMessage({ action: 'openFullDashboard' });
    });
});

async function loadStats() {
    try {
        const result = await chrome.storage.local.get(['scanHistory']);
        const history = result.scanHistory || [];
        
        const totalScans = history.length;
        const threatsBlocked = history.filter(scan => 
            scan.riskLevel === 'high' || scan.riskLevel === 'medium'
        ).length;

        document.getElementById('totalScans').textContent = totalScans;
        document.getElementById('threatsBlocked').textContent = threatsBlocked;
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

async function loadRecentScans() {
    try {
        const result = await chrome.storage.local.get(['scanHistory']);
        const history = result.scanHistory || [];
        const scanList = document.getElementById('scanList');

        if (history.length === 0) {
            scanList.innerHTML = '<div class="no-scans">No scans yet. Open an email to see protection in action!</div>';
            return;
        }

        scanList.innerHTML = '';
        const recentScans = history.slice(0, 5);

        recentScans.forEach(scan => {
            const scanItem = document.createElement('div');
            scanItem.className = 'scan-item';
            
            const icon = scan.riskLevel === 'high' ? '🛑' : 
                        scan.riskLevel === 'medium' ? '⚠️' : '✓';
            
            const timeAgo = getTimeAgo(new Date(scan.timestamp));
            
            scanItem.innerHTML = `
                <div class="scan-icon">${icon}</div>
                <div class="scan-details">
                    <div class="scan-time">${timeAgo}</div>
                </div>
                <div class="scan-risk risk-${scan.riskLevel}">${scan.riskLevel}</div>
            `;
            
            scanList.appendChild(scanItem);
        });
    } catch (error) {
        console.error('Error loading recent scans:', error);
    }
}

function getTimeAgo(date) {
    const seconds = Math.floor((new Date() - date) / 1000);
    
    if (seconds < 60) return 'Just now';
    if (seconds < 3600) return Math.floor(seconds / 60) + ' min ago';
    if (seconds < 86400) return Math.floor(seconds / 3600) + ' hr ago';
    return Math.floor(seconds / 86400) + ' days ago';
}

// ── Auth (server-backed, shared with website) ─────────────────────────
const AUTH_API = 'http://localhost:5000/api/auth';
const EXT_SESSION_KEY = 'ext_cyberhunter_session';

async function getExtSession() {
    const r = await chrome.storage.local.get([EXT_SESSION_KEY]);
    return r[EXT_SESSION_KEY] || null;
}

async function saveExtSession(user) {
    await chrome.storage.local.set({ [EXT_SESSION_KEY]: user });
}

async function clearExtSession() {
    await chrome.storage.local.remove(EXT_SESSION_KEY);
}

async function renderExtAuth() {
    const user = await getExtSession();
    const loggedInEl = document.getElementById('extLoggedIn');
    const formsEl = document.getElementById('extAuthForms');
    if (user) {
        loggedInEl.classList.add('show');
        formsEl.style.display = 'none';
        document.getElementById('extAvatar').textContent = user.name.charAt(0).toUpperCase();
        document.getElementById('extUserName').textContent = user.name;
        document.getElementById('extUserEmail').textContent = user.email;
    } else {
        loggedInEl.classList.remove('show');
        formsEl.style.display = '';
    }
}

function initAuth() {
    renderExtAuth();

    // Tab switching
    document.getElementById('extTabLogin').addEventListener('click', () => {
        document.getElementById('extTabLogin').classList.add('active');
        document.getElementById('extTabSignup').classList.remove('active');
        document.getElementById('extLoginForm').classList.add('active');
        document.getElementById('extSignupForm').classList.remove('active');
    });
    document.getElementById('extTabSignup').addEventListener('click', () => {
        document.getElementById('extTabSignup').classList.add('active');
        document.getElementById('extTabLogin').classList.remove('active');
        document.getElementById('extSignupForm').classList.add('active');
        document.getElementById('extLoginForm').classList.remove('active');
    });

    // Login
    document.getElementById('extLoginForm').addEventListener('submit', async e => {
        e.preventDefault();
        const email = document.getElementById('extLoginEmail').value.trim().toLowerCase();
        const password = document.getElementById('extLoginPassword').value;
        const msg = document.getElementById('extLoginMsg');
        try {
            const res = await fetch(`${AUTH_API}/login`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            const data = await res.json();
            if (!data.success) {
                msg.textContent = data.error;
                msg.className = 'auth-msg error';
                return;
            }
            await saveExtSession(data.user);
            msg.textContent = '';
            renderExtAuth();
        } catch {
            msg.textContent = 'Server unavailable. Start the API server first.';
            msg.className = 'auth-msg error';
        }
    });

    // Sign up
    document.getElementById('extSignupForm').addEventListener('submit', async e => {
        e.preventDefault();
        const name = document.getElementById('extSignupName').value.trim();
        const email = document.getElementById('extSignupEmail').value.trim().toLowerCase();
        const password = document.getElementById('extSignupPassword').value;
        const msg = document.getElementById('extSignupMsg');
        try {
            const res = await fetch(`${AUTH_API}/register`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ name, email, password })
            });
            const data = await res.json();
            if (!data.success) {
                msg.textContent = data.error;
                msg.className = 'auth-msg error';
                return;
            }
            await saveExtSession(data.user);
            msg.textContent = '';
            renderExtAuth();
        } catch {
            msg.textContent = 'Server unavailable. Start the API server first.';
            msg.className = 'auth-msg error';
        }
    });

    // Sign out
    document.getElementById('extSignOut').addEventListener('click', async () => {
        await clearExtSession();
        renderExtAuth();
    });
}
