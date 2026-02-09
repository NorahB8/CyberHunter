// CyberHunter Popup Script
document.addEventListener('DOMContentLoaded', async () => {
    loadStats();
    loadRecentScans();
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
