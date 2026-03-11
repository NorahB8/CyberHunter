// CyberHunter Popup Script
document.addEventListener('DOMContentLoaded', async () => {
    loadStats();
    loadRecentScans();
    initTabs();
    initProfile();
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

document.getElementById('websiteLink').addEventListener('click', (e) => {
    e.preventDefault();
    chrome.tabs.create({ url: 'index.html' });
});

// ── Tab Navigation ─────────────────────────────────────────────────────────
function initTabs() {
    document.getElementById('scansTabBtn').addEventListener('click', () => {
        document.getElementById('scansTabBtn').classList.add('active');
        document.getElementById('profileTabBtn').classList.remove('active');
        document.getElementById('scansPanel').classList.add('active');
        document.getElementById('profilePanel').classList.remove('active');
    });
    document.getElementById('profileTabBtn').addEventListener('click', () => {
        document.getElementById('profileTabBtn').classList.add('active');
        document.getElementById('scansTabBtn').classList.remove('active');
        document.getElementById('profilePanel').classList.add('active');
        document.getElementById('scansPanel').classList.remove('active');
    });
}

// ── Profile Management ─────────────────────────────────────────────────────
const EXT_USERS_KEY = 'ext_cyberhunter_users';
const EXT_SESSION_KEY = 'ext_cyberhunter_session';

async function getExtUsers() {
    const result = await chrome.storage.local.get([EXT_USERS_KEY]);
    return result[EXT_USERS_KEY] || [];
}
async function saveExtUsers(users) {
    await chrome.storage.local.set({ [EXT_USERS_KEY]: users });
}
async function getExtSession() {
    const result = await chrome.storage.local.get([EXT_SESSION_KEY]);
    return result[EXT_SESSION_KEY] || null;
}
async function saveExtSession(user) {
    await chrome.storage.local.set({ [EXT_SESSION_KEY]: user });
}
async function clearExtSession() {
    await chrome.storage.local.remove(EXT_SESSION_KEY);
}

function formatDate(isoString) {
    if (!isoString) return '—';
    return new Date(isoString).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}

async function renderProfile() {
    const session = await getExtSession();
    if (session) {
        document.getElementById('profileView').style.display = 'block';
        document.getElementById('profileAuthView').style.display = 'none';

        const initial = (session.name || session.email)[0].toUpperCase();
        document.getElementById('profileAvatarLg').textContent = initial;
        document.getElementById('profileNameLg').textContent = session.name || 'User';
        document.getElementById('profileEmailLg').textContent = session.email;
        document.getElementById('profileJoined').textContent = formatDate(session.joinedDate);

        // Reuse scan stats
        const result = await chrome.storage.local.get(['scanHistory']);
        const history = result.scanHistory || [];
        document.getElementById('profileScans').textContent = history.length;
        document.getElementById('profileThreats').textContent = history.filter(
            s => s.riskLevel === 'high' || s.riskLevel === 'medium'
        ).length;
    } else {
        document.getElementById('profileView').style.display = 'none';
        document.getElementById('profileAuthView').style.display = 'block';
    }
}

function initProfile() {
    renderProfile();

    // Auth tab switching inside profile panel
    document.getElementById('extLoginTabBtn').addEventListener('click', () => {
        document.getElementById('extLoginTabBtn').classList.add('active');
        document.getElementById('extSignupTabBtn').classList.remove('active');
        document.getElementById('extLoginForm').style.display = 'block';
        document.getElementById('extSignupForm').style.display = 'none';
        document.getElementById('extLoginMsg').className = 'pf-msg';
    });
    document.getElementById('extSignupTabBtn').addEventListener('click', () => {
        document.getElementById('extSignupTabBtn').classList.add('active');
        document.getElementById('extLoginTabBtn').classList.remove('active');
        document.getElementById('extSignupForm').style.display = 'block';
        document.getElementById('extLoginForm').style.display = 'none';
        document.getElementById('extSignupMsg').className = 'pf-msg';
    });

    document.getElementById('extLoginSubmit').addEventListener('click', async () => {
        const email = document.getElementById('extLoginEmail').value.trim();
        const password = document.getElementById('extLoginPassword').value;
        const msg = document.getElementById('extLoginMsg');

        if (!email || !password) {
            msg.textContent = 'Please fill in all fields.';
            msg.className = 'pf-msg error';
            return;
        }
        const users = await getExtUsers();
        const user = users.find(u => u.email === email && u.password === password);
        if (!user) {
            msg.textContent = 'Incorrect email or password.';
            msg.className = 'pf-msg error';
            return;
        }
        await saveExtSession(user);
        renderProfile();
    });

    document.getElementById('extSignupSubmit').addEventListener('click', async () => {
        const name = document.getElementById('extSignupName').value.trim();
        const email = document.getElementById('extSignupEmail').value.trim();
        const password = document.getElementById('extSignupPassword').value;
        const msg = document.getElementById('extSignupMsg');

        if (!name || !email || !password) {
            msg.textContent = 'Please fill in all fields.';
            msg.className = 'pf-msg error';
            return;
        }
        if (password.length < 6) {
            msg.textContent = 'Password must be at least 6 characters.';
            msg.className = 'pf-msg error';
            return;
        }
        const users = await getExtUsers();
        if (users.find(u => u.email === email)) {
            msg.textContent = 'An account with this email already exists.';
            msg.className = 'pf-msg error';
            return;
        }
        const newUser = { name, email, password, joinedDate: new Date().toISOString() };
        users.push(newUser);
        await saveExtUsers(users);
        await saveExtSession(newUser);
        renderProfile();
    });

    document.getElementById('profileSignOutBtn').addEventListener('click', async () => {
        await clearExtSession();
        renderProfile();
    });
}
