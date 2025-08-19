/**
 * Anuj Nandal's AI News Verifier - Advanced JavaScript
 * Unique interactive features for fake news detection
 */

// Advanced text analysis and UI interactions
class NewsAnalyzer {
    constructor() {
        this.initializeUI();
        this.setupEventListeners();
        this.createParticleEffect();
    }

    initializeUI() {
        this.textArea = document.getElementById('news_text');
        this.analyzeBtn = document.querySelector('.btn-modern');
        this.loadingAnimation = document.getElementById('loadingAnimation');
        
        // Add real-time character counter
        this.addCharacterCounter();
        // Add typing effects
        this.addTypingEffects();
    }

    setupEventListeners() {
        // Form submission with advanced validation
        const form = document.getElementById('newsAnalysisForm');
        if (form) {
            form.addEventListener('submit', (e) => this.handleFormSubmit(e));
        }

        // Real-time text analysis
        if (this.textArea) {
            this.textArea.addEventListener('input', () => this.analyzeTextRealTime());
            this.textArea.addEventListener('paste', () => {
                setTimeout(() => this.analyzeTextRealTime(), 100);
            });
        }

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => this.handleKeyboardShortcuts(e));
    }

    handleFormSubmit(e) {
        const text = this.textArea.value.trim();
        
        // Advanced validation
        if (text.length < 50) {
            e.preventDefault();
            this.showNotification('Please enter at least 50 characters for accurate analysis.', 'warning');
            return;
        }

        if (text.length > 10000) {
            e.preventDefault();
            this.showNotification('Text too long. Please limit to 10,000 characters.', 'warning');
            return;
        }

        // Show advanced loading animation
        this.showAdvancedLoading();
    }

    analyzeTextRealTime() {
        const text = this.textArea.value;
        const wordCount = text.trim().split(/\s+/).filter(word => word.length > 0).length;
        const charCount = text.length;
        
        // Update counter
        const counter = document.getElementById('characterCounter');
        if (counter) {
            counter.innerHTML = `
                <div class="analysis-stats-mini">
                    <span><i class="fas fa-font"></i> ${charCount} chars</span>
                    <span><i class="fas fa-spell-check"></i> ${wordCount} words</span>
                    <span><i class="fas fa-clock"></i> ~${Math.ceil(wordCount / 200)} min read</span>
                </div>
            `;
        }

        // Real-time sentiment indicators
        this.updateSentimentIndicators(text);
    }

    addCharacterCounter() {
        if (this.textArea) {
            const counterDiv = document.createElement('div');
            counterDiv.id = 'characterCounter';
            counterDiv.className = 'character-counter';
            counterDiv.style.cssText = `
                margin-top: 10px;
                padding: 10px;
                background: rgba(255, 255, 255, 0.05);
                border-radius: 10px;
                font-size: 0.9rem;
                color: #b8c5d6;
            `;
            this.textArea.parentNode.insertBefore(counterDiv, this.textArea.nextSibling);
        }
    }

    addTypingEffects() {
        if (this.textArea) {
            this.textArea.addEventListener('keydown', () => {
                this.textArea.style.boxShadow = '0 0 20px rgba(102, 126, 234, 0.3)';
            });
            
            this.textArea.addEventListener('keyup', () => {
                setTimeout(() => {
                    this.textArea.style.boxShadow = '';
                }, 300);
            });
        }
    }

    updateSentimentIndicators(text) {
        // Simple sentiment analysis indicators
        const positiveWords = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic'];
        const negativeWords = ['bad', 'terrible', 'awful', 'horrible', 'shocking', 'breaking'];
        const urgentWords = ['urgent', 'breaking', 'exclusive', 'secret', 'hidden', 'revealed'];
        
        const words = text.toLowerCase().split(/\s+/);
        const positiveCount = words.filter(word => positiveWords.includes(word)).length;
        const negativeCount = words.filter(word => negativeWords.includes(word)).length;
        const urgentCount = words.filter(word => urgentWords.includes(word)).length;
        
        // Update UI indicators (if elements exist)
        const indicator = document.getElementById('sentimentIndicator');
        if (indicator) {
            let sentiment = 'neutral';
            if (urgentCount > 2) sentiment = 'suspicious';
            else if (negativeCount > positiveCount) sentiment = 'negative';
            else if (positiveCount > negativeCount) sentiment = 'positive';
            
            indicator.className = `sentiment-indicator ${sentiment}`;
        }
    }

    showAdvancedLoading() {
        if (this.loadingAnimation) {
            this.loadingAnimation.style.display = 'block';
            
            // Add progressive loading messages
            const messages = [
                'Initializing AI neural networks...',
                'Processing natural language patterns...',
                'Analyzing semantic structures...',
                'Cross-referencing knowledge base...',
                'Generating confidence scores...'
            ];
            
            let messageIndex = 0;
            const messageElement = this.loadingAnimation.querySelector('p');
            
            const messageInterval = setInterval(() => {
                if (messageIndex < messages.length) {
                    messageElement.textContent = messages[messageIndex];
                    messageIndex++;
                } else {
                    clearInterval(messageInterval);
                }
            }, 800);
        }
    }

    handleKeyboardShortcuts(e) {
        // Ctrl+Enter to submit
        if (e.ctrlKey && e.key === 'Enter') {
            e.preventDefault();
            const form = document.getElementById('newsAnalysisForm');
            if (form) form.submit();
        }
        
        // Ctrl+L to load sample
        if (e.ctrlKey && e.key === 'l') {
            e.preventDefault();
            this.loadSample('fake');
        }
        
        // Escape to clear
        if (e.key === 'Escape') {
            this.clearText();
        }
    }

    createParticleEffect() {
        // Create subtle floating particles for visual appeal
        const particleContainer = document.createElement('div');
        particleContainer.className = 'particle-container';
        particleContainer.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        `;
        
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.cssText = `
                position: absolute;
                width: 4px;
                height: 4px;
                background: rgba(102, 126, 234, 0.3);
                border-radius: 50%;
                animation: float ${5 + Math.random() * 10}s ease-in-out infinite;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                animation-delay: ${Math.random() * 10}s;
            `;
            particleContainer.appendChild(particle);
        }
        
        document.body.appendChild(particleContainer);
    }

    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            border-radius: 15px;
            padding: 15px 20px;
            color: white;
            font-weight: 500;
            z-index: 1000;
            animation: slideIn 0.3s ease-out;
            max-width: 300px;
        `;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease-in';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    loadSample(type) {
        const samples = {
            real: "Scientists at MIT have successfully developed a new breakthrough in renewable energy technology. The research, published in the peer-reviewed journal Nature Energy, describes a novel solar cell design that can achieve over 40% efficiency in converting sunlight to electricity. The study was conducted over three years with a team of 15 researchers and has been independently verified by leading experts in the field. The technology could significantly reduce the cost of solar power and accelerate the global transition to clean energy. The research team plans to begin pilot testing with industry partners next year.",
            
            fake: "BREAKING: Government secretly controls weather with hidden 5G towers! Leaked documents reveal shocking truth that mainstream media doesn't want you to know! Scientists who tried to expose this were mysteriously silenced! Share this before it gets deleted! This one weird trick will protect you from mind control rays - doctors hate this secret! Click here to learn more about how the deep state is manipulating your thoughts through weather modification technology! Don't let them fool you anymore!"
        };
        
        if (this.textArea) {
            this.textArea.value = samples[type] || samples.fake;
            this.analyzeTextRealTime();
            this.textArea.focus();
            
            // Add visual feedback
            this.showNotification(`${type === 'real' ? 'Real' : 'Fake'} news sample loaded!`, 'success');
        }
    }

    clearText() {
        if (this.textArea) {
            this.textArea.value = '';
            this.analyzeTextRealTime();
            this.textArea.focus();
            this.showNotification('Text cleared!', 'info');
        }
    }
}

// Global functions for backward compatibility
function loadSample(type) {
    if (window.newsAnalyzer) {
        window.newsAnalyzer.loadSample(type);
    }
}

function clearText() {
    if (window.newsAnalyzer) {
        window.newsAnalyzer.clearText();
    }
}

function loadSampleText() {
    loadSample('fake');
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.newsAnalyzer = new NewsAnalyzer();
    
    // Add CSS animations
    const style = document.createElement('style');
    style.textContent = `
        @keyframes slideIn {
            from { transform: translateX(100%); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        
        @keyframes slideOut {
            from { transform: translateX(0); opacity: 1; }
            to { transform: translateX(100%); opacity: 0; }
        }
        
        .analysis-stats-mini {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
        }
        
        .analysis-stats-mini span {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .sentiment-indicator {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-left: 10px;
        }
        
        .sentiment-indicator.positive { background: #4facfe; }
        .sentiment-indicator.negative { background: #fa709a; }
        .sentiment-indicator.suspicious { background: #ff6b6b; }
        .sentiment-indicator.neutral { background: #95a5a6; }
    `;
    document.head.appendChild(style);
});

// Export for modules (if needed)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = NewsAnalyzer;
}
