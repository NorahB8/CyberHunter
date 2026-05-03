// CyberHunter Popup Script
document.addEventListener('DOMContentLoaded', async () => {
    loadStats();
    loadRecentScans();
    initAuth();
    initDetailPanel();

    const isFullPage = new URLSearchParams(window.location.search).get('mode') === 'fullpage';
    const websiteLink = document.getElementById('websiteLink');

    if (isFullPage) {
        websiteLink.textContent = 'Go to Home Page';
        websiteLink.addEventListener('click', (e) => {
            e.preventDefault();
            window.open('http://127.0.0.1:5500/index.html', '_blank');
        });
    } else {
        websiteLink.textContent = 'Open Full Extension';
        websiteLink.addEventListener('click', (e) => {
            e.preventDefault();
            chrome.runtime.sendMessage({ action: 'openFullDashboard' });
        });
    }
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

function escapeHtml(str) {
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
}

async function loadRecentScans() {
    try {
        const result = await chrome.storage.local.get(['scanHistory']);
        const history = result.scanHistory || [];
        const scanList = document.getElementById('scanList');
        const toggleBtn = document.getElementById('historyToggle');
        const wrapper = document.getElementById('scanListWrapper');

        if (history.length === 0) {
            scanList.innerHTML = '<div class="no-scans">No scans yet. Open an email to see protection in action!</div>';
            toggleBtn.style.display = 'none';
            return;
        }

        const PREVIEW = 5;
        let showingAll = false;

        function renderScans(items) {
            scanList.innerHTML = '';
            items.forEach(scan => {
                const scanItem = document.createElement('div');
                scanItem.className = 'scan-item';

                const icon = scan.riskLevel === 'high' ? '🛑' :
                             scan.riskLevel === 'medium' ? '⚠️' : '✓';
                const timeAgo = getTimeAgo(new Date(scan.timestamp));
                const subject = escapeHtml(scan.subject || 'Email scanned');
                const sender  = escapeHtml(scan.sender  || '');
                const score   = scan.riskScore != null ? `${Math.round(scan.riskScore)}%` : '';
                const level   = escapeHtml(scan.riskLevel || 'low');

                scanItem.innerHTML = `
                    <div class="scan-icon">${icon}</div>
                    <div class="scan-details">
                        <div class="scan-subject">${subject}</div>
                        ${sender ? `<div class="scan-sender">${sender}</div>` : ''}
                        <div class="scan-time">${timeAgo}</div>
                    </div>
                    <div class="scan-meta">
                        <div class="scan-risk risk-${level}">${level}</div>
                        ${score ? `<div class="scan-score">${score} risk</div>` : ''}
                    </div>
                `;
                scanItem.style.cursor = 'pointer';
                scanItem.addEventListener('click', () => showScanDetail(scan));
                scanList.appendChild(scanItem);
            });
        }

        renderScans(history.slice(0, PREVIEW));

        if (history.length > PREVIEW) {
            toggleBtn.style.display = 'block';
            toggleBtn.textContent = `Show all ${history.length} scans ▼`;
            wrapper.style.maxHeight = '220px';

            toggleBtn.onclick = () => {
                showingAll = !showingAll;
                if (showingAll) {
                    renderScans(history);
                    wrapper.style.maxHeight = 'none'; // let body scroll handle it
                    toggleBtn.textContent = 'Show less ▲';
                } else {
                    renderScans(history.slice(0, PREVIEW));
                    wrapper.style.maxHeight = '220px';
                    toggleBtn.textContent = `Show all ${history.length} scans ▼`;
                }
            };
        }
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
            const userKey = `scanHistory_${data.user.email}`;
            const saved = await chrome.storage.local.get([userKey]);
            await chrome.storage.local.set({ scanHistory: saved[userKey] || [] });
            msg.textContent = '';
            renderExtAuth();
            loadStats();
            loadRecentScans();
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
            await chrome.storage.local.remove('scanHistory');
            msg.textContent = '';
            renderExtAuth();
            loadStats();
            loadRecentScans();
        } catch {
            msg.textContent = 'Server unavailable. Start the API server first.';
            msg.className = 'auth-msg error';
        }
    });

    // Sign out
    document.getElementById('extSignOut').addEventListener('click', async () => {
        const user = await getExtSession();
        if (user) {
            const { scanHistory } = await chrome.storage.local.get(['scanHistory']);
            await chrome.storage.local.set({ [`scanHistory_${user.email}`]: scanHistory || [] });
        }
        await clearExtSession();
        await chrome.storage.local.remove('scanHistory');
        loadStats();
        loadRecentScans();
        renderExtAuth();
    });
}

// Global scanning toggle (enable / disable extension entirely)
async function initSiteToggle() {
    const toggle = document.getElementById('siteToggle');
    const label = document.getElementById('siteToggleLabel');
    const thumb = document.getElementById('siteToggleThumb');
    const track = document.getElementById('siteToggleTrack');

    const { scanningEnabled = true } = await chrome.storage.local.get('scanningEnabled');

    function applyState(enabled) {
        toggle.checked = enabled;
        thumb.style.left = enabled ? '23px' : '3px';
        track.style.background = enabled ? '#d4a200' : '#4a3c00';
        label.textContent = enabled ? 'Scanning enabled' : 'Scanning disabled';
        label.style.color = enabled ? '#c8a800' : '#888';
    }

    applyState(scanningEnabled);

    toggle.addEventListener('change', async () => {
        await chrome.storage.local.set({ scanningEnabled: toggle.checked });
        applyState(toggle.checked);
        // Notify all content scripts
        const tabs = await chrome.tabs.query({ url: ['http://*/*', 'https://*/*'] });
        tabs.forEach(t => chrome.tabs.sendMessage(t.id, { action: 'setSiteEnabled', enabled: toggle.checked }).catch(() => {}));
    });
}

initSiteToggle();

// ── Scan detail panel ─────────────────────────────────────────────────
function initDetailPanel() {
    document.getElementById('detailBack').addEventListener('click', hideScanDetail);
}

function showScanDetail(scan) {
    const score = scan.riskScore != null ? Math.round(scan.riskScore) : null;
    const level = scan.riskLevel || 'low';

    // Score value + colour
    const scoreEl = document.getElementById('detailScore');
    scoreEl.textContent = score != null ? `${score}%` : '—';
    scoreEl.style.color = level === 'high' ? '#ff5577' : level === 'medium' ? '#ffbb33' : '#00c864';

    // Badge
    const badge = document.getElementById('detailBadge');
    badge.textContent = level.toUpperCase();
    badge.style.background = level === 'high' ? 'rgba(255,51,102,0.2)'
                           : level === 'medium' ? 'rgba(255,170,0,0.2)'
                           : 'rgba(0,255,136,0.2)';
    badge.style.color = level === 'high' ? '#ff5577' : level === 'medium' ? '#ffbb33' : '#00c864';

    document.getElementById('detailSubject').textContent = scan.subject || 'No subject';
    document.getElementById('detailUrl').textContent     = scan.senderEmail || scan.sender || '—';
    document.getElementById('detailTime').textContent    = scan.timestamp
        ? new Date(scan.timestamp).toLocaleString()
        : '—';

    // Switch views
    document.getElementById('scanDetail').classList.add('visible');
    document.querySelector('.content').style.display = 'none';
}

function hideScanDetail() {
    document.getElementById('scanDetail').classList.remove('visible');
    document.querySelector('.content').style.display = '';
}
