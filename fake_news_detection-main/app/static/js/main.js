document.addEventListener('DOMContentLoaded', function() {
    // Initialize any components that need JavaScript
    
    // Animate progress bar on results page
    const progressBar = document.querySelector('.progress-bar');
    if (progressBar) {
        progressBar.style.width = '0%';
        setTimeout(() => {
            progressBar.style.width = progressBar.getAttribute('aria-valuenow') + '%';
        }, 200);
    }
    
    // Add animation to result page elements
    const resultCard = document.querySelector('.result-card');
    if (resultCard) {
        resultCard.classList.add('fade-in');
        
        // Animate analysis sections
        const sections = document.querySelectorAll('.analysis-section, .tips-section, .article-preview');
        sections.forEach((section, index) => {
            setTimeout(() => {
                section.classList.add('fade-in');
            }, 300 + (index * 150));
        });
    }
});

// Function to load sample fake news text
function loadSampleText() {
    const sampleTexts = [
        `BREAKING: NASA Scientists Break Silence, Admit Stunning Discovery of 'Alien Megastructure' Around Nearby Star. Top astronomers from NASA have finally confirmed what they've suspected for years - a massive artificial structure orbits a star just 50 light years from Earth. "We can no longer deny the evidence," said Dr. James Mitchell, lead researcher at NASA's SETI division. "The regular patterns of light blockage can only be explained by an engineered structure." The White House has called an emergency meeting with world leaders to discuss potential contact protocols. The discovery, initially dismissed as instrument error, has been independently verified by observatories in 15 countries.`,
        
        `EXCLUSIVE: Scientists Find Miracle Cure for Cancer in Common Household Item. In a groundbreaking discovery that pharmaceutical companies don't want you to know about, researchers at a private laboratory have found that a common household spice completely eliminates cancer cells within days. The study, which was suppressed by major medical journals, shows that mixing the spice with warm water and drinking it daily led to complete remission in 98% of terminal patients. "Big Pharma doesn't want this information public because they can't profit from it," said lead researcher Dr. Robert Anderson. Share this information before it gets taken down!`,
        
        `ALERT: Government Confirms Weather Control Technology Used to Create Recent Hurricanes. A leaked document from the Department of Defense reveals that the recent string of devastating hurricanes were actually created using the government's HAARP weather modification system. The classified report, authenticated by three independent sources, explains that the hurricanes were generated as a test of the system's capabilities. "Weather warfare is the next frontier in national defense," states the document, which outlines plans for creating targeted weather events in foreign territories. Officials have refused to comment on the leak, and mainstream media outlets have been ordered to suppress the story.`
    ];
    
    const randomIndex = Math.floor(Math.random() * sampleTexts.length);
    document.getElementById('news_text').value = sampleTexts[randomIndex];
}