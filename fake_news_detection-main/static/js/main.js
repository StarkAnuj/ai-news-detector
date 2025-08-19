// Initialize AOS
document.addEventListener('DOMContentLoaded', function() {
  AOS.init({
    duration: 800,
    easing: 'ease',
    once: true,
    offset: 100
  });
  
  // Initialize particles.js
  if (document.getElementById('particles-js')) {
    particlesJS('particles-js', {
      "particles": {
        "number": {
          "value": 80,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": "#7e57c2"
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          }
        },
        "opacity": {
          "value": 0.5,
          "random": false,
          "anim": {
            "enable": false,
            "speed": 1,
            "opacity_min": 0.1,
            "sync": false
          }
        },
        "size": {
          "value": 3,
          "random": true,
          "anim": {
            "enable": false,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 150,
          "color": "#7e57c2",
          "opacity": 0.4,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 2,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": false,
          "attract": {
            "enable": false,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "grab"
          },
          "onclick": {
            "enable": true,
            "mode": "push"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 140,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 40,
            "duration": 2,
            "opacity": 8,
            "speed": 3
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 4
          },
          "remove": {
            "particles_nb": 2
          }
        }
      },
      "retina_detect": true
    });
  }
});

// Theme switcher functionality
const toggleSwitch = document.querySelector('#checkbox');
const currentTheme = localStorage.getItem('theme');

// Check for saved theme preference
if (currentTheme) {
  document.documentElement.classList.add(currentTheme);
  
  if (currentTheme === 'light-theme') {
    toggleSwitch.checked = true;
  }
}

// Theme switch handler
function switchTheme(e) {
  if (e.target.checked) {
    document.documentElement.classList.add('light-theme');
    localStorage.setItem('theme', 'light-theme');
  } else {
    document.documentElement.classList.remove('light-theme');
    localStorage.setItem('theme', 'dark-theme');
  }
}

toggleSwitch.addEventListener('change', switchTheme);

// Mobile menu functionality
const menuToggle = document.querySelector('#mobile-menu');
const navMenu = document.querySelector('.nav-menu');

menuToggle.addEventListener('click', function() {
  menuToggle.classList.toggle('active');
  navMenu.classList.toggle('active');
  
  // Animate hamburger menu
  const bars = document.querySelectorAll('.bar');
  if (menuToggle.classList.contains('active')) {
    bars[0].style.transform = 'rotate(-45deg) translate(-5px, 6px)';
    bars[1].style.opacity = '0';
    bars[2].style.transform = 'rotate(45deg) translate(-5px, -6px)';
  } else {
    bars[0].style.transform = 'none';
    bars[1].style.opacity = '1';
    bars[2].style.transform = 'none';
  }
});

// Close mobile menu when clicking on nav-links
document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    menuToggle.classList.remove('active');
    navMenu.classList.remove('active');
    
    const bars = document.querySelectorAll('.bar');
    bars[0].style.transform = 'none';
    bars[1].style.opacity = '1';
    bars[2].style.transform = 'none';
  });
});

// Form submission handler
const contactForm = document.getElementById('contactForm');

if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const subject = document.getElementById('subject').value;
    const message = document.getElementById('message').value;
    
    // Here you would normally send this data to your backend
    console.log('Form submitted:', { name, email, subject, message });
    
    // Show success message
    const formGroups = document.querySelectorAll('.form-group');
    formGroups.forEach(group => group.style.display = 'none');
    
    const button = contactForm.querySelector('button');
    button.style.display = 'none';
    
    const successMessage = document.createElement('div');
    successMessage.classList.add('success-message');
    successMessage.innerHTML = `
      <i class="fas fa-check-circle"></i>
      <h3>Message Sent Successfully!</h3>
      <p>Thank you for reaching out, ${name}. I'll get back to you soon.</p>
    `;
    
    contactForm.appendChild(successMessage);
    
    // Reset form
    contactForm.reset();
  });
}

// Animate skill bars on scroll
function animateSkillBars() {
  const skillItems = document.querySelectorAll('.skill-item');
  
  if (skillItems.length === 0) return;
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const progressBar = entry.target.querySelector('.progress');
        if (progressBar) {
          const width = progressBar.style.width;
          progressBar.style.width = '0%';
          setTimeout(() => {
            progressBar.style.width = width;
          }, 100);
        }
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  
  skillItems.forEach(item => {
    observer.observe(item);
  });
}

// Function to initialize project section animations
function initProjectAnimations() {
  // Get all project cards
  const projectCards = document.querySelectorAll('.project-card');
  
  // Add staggered animations when cards come into view
  const projectObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        // Add class with delay based on index
        setTimeout(() => {
          entry.target.classList.add('fade-in-up');
        }, index * 150);
        
        // Add hover effect cursor
        entry.target.addEventListener('mousemove', handleProjectHover);
        entry.target.addEventListener('mouseleave', resetProjectCard);
        
        // Remove from observation
        projectObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  
  // Observe each project card
  projectCards.forEach(card => {
    projectObserver.observe(card);
  });
}

// Function to handle project card hover effects
function handleProjectHover(e) {
  // Don't apply effect on touch devices
  if (window.matchMedia('(hover: none)').matches) return;
  
  const card = this.querySelector('.project-