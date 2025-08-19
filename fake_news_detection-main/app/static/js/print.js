/**
 * Print and Download functionality for Anuj Nandal's Fake News Detector
 */

// Enhanced Print functionality
function generatePrintableReport() {
    const reportData = {
        timestamp: new Date().toLocaleString(),
        analysisType: 'Fake News Detection',
        analyzer: 'Anuj Nandal\'s AI News Verifier',
        version: '1.0'
    };
    
    return reportData;
}

// Print report with enhanced formatting
function printReport() {
    // Set the print date
    const printDateElement = document.getElementById('printDate');
    if (printDateElement) {
        printDateElement.textContent = new Date().toLocaleString();
    }
    
    // Add print class to body for additional styling
    document.body.classList.add('printing');
    
    // Print after a small delay to ensure styles are applied
    setTimeout(() => {
        window.print();
        // Remove print class after printing
        setTimeout(() => {
            document.body.classList.remove('printing');
        }, 1000);
    }, 100);
}

// Enhanced download functionality
function downloadReport() {
    const printDateElement = document.getElementById('printDate');
    if (printDateElement) {
        printDateElement.textContent = new Date().toLocaleString();
    }
    
    // Show helpful notification
    showPrintNotification();
    
    // Trigger print dialog
    setTimeout(() => window.print(), 800);
}

function showPrintNotification() {
    const notification = document.createElement('div');
    notification.className = 'print-notification';
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        border: 1px solid var(--glass-border);
        border-radius: 15px;
        padding: 20px;
        color: white;
        font-weight: 500;
        z-index: 1000;
        max-width: 320px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        animation: slideInRight 0.3s ease-out;
    `;
    
    notification.innerHTML = `
        <div style="display: flex; align-items: center; margin-bottom: 10px;">
            <i class="fas fa-file-pdf" style="color: #4facfe; margin-right: 10px; font-size: 1.2rem;"></i>
            <h6 style="margin: 0; color: white;">Download as PDF</h6>
        </div>
        <p style="margin: 0; font-size: 0.85rem; color: #b8c5d6; line-height: 1.4;">
            In the print dialog:<br>
            1. Select <strong style="color: white;">"Save as PDF"</strong><br>
            2. Choose your destination<br>
            3. Click <strong style="color: white;">"Save"</strong>
        </p>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove notification after 6 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-in';
        setTimeout(() => notification.remove(), 300);
    }, 6000);
}

// Add CSS animations for notifications
document.addEventListener('DOMContentLoaded', function() {
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideInRight {
            from { 
                transform: translateX(100%); 
                opacity: 0; 
            }
            to { 
                transform: translateX(0); 
                opacity: 1; 
            }
        }
        
        @keyframes slideOutRight {
            from { 
                transform: translateX(0); 
                opacity: 1; 
            }
            to { 
                transform: translateX(100%); 
                opacity: 0; 
            }
        }
        
        .printing {
            transition: all 0.3s ease;
        }
        
        @media print {
            .print-notification {
                display: none !important;
            }
        }
    `;
    document.head.appendChild(style);
});
