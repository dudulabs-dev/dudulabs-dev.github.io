/* ==========================================================================
   Dudulabs Dev Interactive Scripting
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  initHeader();
  initMobileMenu();
  initTypingEffect();
  initScrollReveal();
  initSkillsProgress();
  fetchGithubProjects();
  initScrollSpy();
});

/* ==========================================================================
   Header Scroll Effect
   ========================================================================== */
function initHeader() {
  const header = document.getElementById('main-header');
  
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
}

/* ==========================================================================
   Mobile Navigation Toggle
   ========================================================================== */
function initMobileMenu() {
  const toggleBtn = document.getElementById('nav-toggle');
  const menu = document.getElementById('nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');
  
  toggleBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
    const isExpanded = menu.classList.contains('active');
    toggleBtn.setAttribute('aria-expanded', isExpanded);
    toggleBtn.querySelector('i').className = isExpanded 
      ? 'fa-solid fa-xmark' 
      : 'fa-solid fa-bars';
  });

  // Close menu when clicking a link
  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      menu.classList.remove('active');
      toggleBtn.querySelector('i').className = 'fa-solid fa-bars';
    });
  });
}

/* ==========================================================================
   Hero Section Dynamic Typing Effect
   ========================================================================== */
function initTypingEffect() {
  const target = document.getElementById('dynamic-typing');
  const words = ["Elegant Solutions.", "Creative Designs.", "Futuristic Code.", "Interactive Art."];
  let wordIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typingSpeed = 100;

  function type() {
    const currentWord = words[wordIndex];
    
    if (isDeleting) {
      target.textContent = currentWord.substring(0, charIndex - 1);
      charIndex--;
      typingSpeed = 50; // Faster deletion
    } else {
      target.textContent = currentWord.substring(0, charIndex + 1);
      charIndex++;
      typingSpeed = 120; // Normal typing speed
    }

    if (!isDeleting && charIndex === currentWord.length) {
      typingSpeed = 2000; // Wait before deleting
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      isDeleting = false;
      wordIndex = (wordIndex + 1) % words.length;
      typingSpeed = 500; // Pause before next word
    }

    setTimeout(type, typingSpeed);
  }

  // Add typing cursor styling dynamically
  target.style.borderRight = "3px solid var(--accent-cyan)";
  target.style.paddingRight = "5px";
  target.style.animation = "blink-caret 0.75s step-end infinite";
  
  // Create stylesheet rule for cursor blink
  const styleSheet = document.createElement("style");
  styleSheet.innerText = `
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: var(--accent-cyan) }
    }
  `;
  document.head.appendChild(styleSheet);

  setTimeout(type, 1000);
}

/* ==========================================================================
   Scroll Reveal Animation
   ========================================================================== */
function initScrollReveal() {
  const reveals = document.querySelectorAll('.reveal');
  
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  });

  reveals.forEach(reveal => {
    revealObserver.observe(reveal);
  });
}

/* ==========================================================================
   Skills Level Progress Bar Animation
   ========================================================================== */
function initSkillsProgress() {
  const skillBars = document.querySelectorAll('.skill-bar');
  
  const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target;
        const level = bar.getAttribute('data-level');
        bar.style.width = level;
        skillObserver.unobserve(bar); // Animate only once
      }
    });
  }, {
    threshold: 0.5
  });

  skillBars.forEach(bar => {
    skillObserver.observe(bar);
  });
}

/* ==========================================================================
   GitHub API Project Fetcher
   ========================================================================== */
async function fetchGithubProjects() {
  const grid = document.getElementById('github-projects-grid');
  const githubUser = 'dudulabs-dev';
  
  // Hardcoded premium fallback projects in case API fails or has rate limits
  const fallbackProjects = [
    {
      name: 'dudulabs-dev.github.io',
      description: 'The creative personal homepage for Dudulabs Dev showcasing projects and skills with premium aesthetics.',
      language: 'CSS / JS',
      stargazers_count: 5,
      html_url: `https://github.com/${githubUser}/dudulabs-dev.github.io`
    },
    {
      name: 'blog-generator',
      description: 'A markdown-based static blog generator built with Node.js, focusing on SEO performance and clean architecture.',
      language: 'JavaScript',
      stargazers_count: 12,
      html_url: `https://github.com/${githubUser}/blog-generator`
    },
    {
      name: 'discord-bot',
      description: 'An advanced modular Discord bot featuring music streaming, custom API integration, and database features.',
      language: 'TypeScript',
      stargazers_count: 18,
      html_url: `https://github.com/${githubUser}/discord-bot`
    },
    {
      name: 'wire-reward',
      description: 'A Web3 utility enabling loyalty rewards via smart contracts on EVM-compatible chains.',
      language: 'Solidity',
      stargazers_count: 24,
      html_url: `https://github.com/${githubUser}/wire-reward`
    },
    {
      name: 'category-classifier',
      description: 'Lightweight machine learning model in Python to classify complex hierarchical data sets.',
      language: 'Python',
      stargazers_count: 15,
      html_url: `https://github.com/${githubUser}/category-classifier`
    },
    {
      name: 'match-master',
      description: 'A real-time competitive matchmaking backend API built with Rust using WebSocket protocols.',
      language: 'Rust',
      stargazers_count: 32,
      html_url: `https://github.com/${githubUser}/match-master`
    }
  ];

  try {
    // Try fetching from User endpoint. If empty, or 404, we can catch it.
    let response = await fetch(`https://api.github.com/users/${githubUser}/repos?sort=updated&per_page=10`);
    
    // If not successful (e.g. Rate limit or 404), throw error to trigger fallback
    if (!response.ok) {
      throw new Error(`GitHub API returned status ${response.status}`);
    }
    
    let repos = await response.json();
    
    // Filter out forks and index pages repo if desired, or sort by stars
    repos = repos.filter(repo => !repo.fork);
    repos.sort((a, b) => b.stargazers_count - a.stargazers_count);
    
    // If user has no repos, use fallback
    if (repos.length === 0) {
      renderProjects(fallbackProjects, grid);
    } else {
      // Use up to 6 repositories
      renderProjects(repos.slice(0, 6), grid);
    }
  } catch (error) {
    console.warn("GitHub API error, rendering fallback projects:", error);
    renderProjects(fallbackProjects, grid);
  }
}

function renderProjects(projects, container) {
  container.innerHTML = '';
  
  projects.forEach((repo, index) => {
    const card = document.createElement('div');
    card.className = 'project-card glass-panel reveal';
    // Add staggered delay for reveal animation
    card.style.transitionDelay = `${index * 0.1}s`;
    
    const lang = repo.language || 'Code';
    const stars = repo.stargazers_count || 0;
    
    card.innerHTML = `
      <div class="project-meta">
        <span class="project-lang">${lang}</span>
        <span class="project-stars"><i class="fa-solid fa-star"></i> ${stars}</span>
      </div>
      <h3 class="project-title">${repo.name}</h3>
      <p class="project-desc">${repo.description || 'No description available. Check the repository for details.'}</p>
      <a href="${repo.html_url}" target="_blank" class="project-link" aria-label="Go to ${repo.name} github repository">
        Explore Code <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
      </a>
    `;
    
    container.appendChild(card);
    
    // Explicitly observe the new dynamically created element
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
        }
      });
    }, { threshold: 0.1 });
    
    revealObserver.observe(card);
  });
}

/* ==========================================================================
   Navigation Scroll Spy
   ========================================================================== */
function initScrollSpy() {
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('.nav-link');
  
  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPosition = window.scrollY + 100; // Offset for header height
    
    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });
}
