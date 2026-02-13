/**
 * Valentine's Day Website JavaScript
 * 
 * This file contains all the JavaScript functionality for the Valentine's Day website,
 * including animations, interactivity, and AJAX requests.
 */

(function() {
    'use strict';

    // ==================== DOM Ready ====================
    document.addEventListener('DOMContentLoaded', function() {
        initNavigation();
        initAudioPlayer();
        initScrollEffects();
    });

    // ==================== Navigation ====================
    function initNavigation() {
        const navbar = document.querySelector('.navbar');
        const navToggle = document.querySelector('.nav-toggle');
        const navMenu = document.querySelector('.nav-menu');

        // Navbar scroll effect
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Mobile menu toggle
        if (navToggle) {
            navToggle.addEventListener('click', function() {
                navToggle.classList.toggle('active');
                navMenu.classList.toggle('active');
            });
        }

        // Close mobile menu when clicking a link
        const navLinks = document.querySelectorAll('.nav-link');
        navLinks.forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // ==================== Audio Player ====================
    function initAudioPlayer() {
        const audioToggle = document.getElementById('audioToggle');
        const bgMusic = document.getElementById('bgMusic');

        if (audioToggle && bgMusic) {
            audioToggle.addEventListener('click', function() {
                if (bgMusic.paused) {
                    bgMusic.volume = 0.3;
                    bgMusic.play().then(function() {
                        audioToggle.classList.add('playing');
                    }).catch(function(error) {
                        console.log('Audio playback failed:', error);
                    });
                } else {
                    bgMusic.pause();
                    audioToggle.classList.remove('playing');
                }
            });
        }
    }

    // ==================== Scroll Effects ====================
    function initScrollEffects() {
        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href !== '#') {
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                }
            });
        });

        // Intersection Observer for fade-in animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.animate-on-scroll').forEach(function(el) {
            observer.observe(el);
        });
    }

    // ==================== Utility Functions ====================
    
    /**
     * Create a floating heart element
     */
    window.createFloatingHeart = function() {
        const container = document.getElementById('floatingHearts');
        if (!container) return;

        const heartSymbols = ['💕', '💖', '💗', '💓', '💞', '💘', '❤️', '💝'];
        const heart = document.createElement('div');
        heart.className = 'heart';
        heart.innerHTML = heartSymbols[Math.floor(Math.random() * heartSymbols.length)];
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDuration = (Math.random() * 3 + 4) + 's';
        heart.style.fontSize = (Math.random() * 1.5 + 1) + 'rem';
        container.appendChild(heart);

        setTimeout(function() {
            heart.remove();
        }, 6000);
    };

    /**
     * Create confetti effect
     */
    window.createConfetti = function() {
        const container = document.getElementById('confettiContainer');
        if (!container) return;

        const colors = ['#ff6b9d', '#feca57', '#48dbfb', '#1dd1a1', '#9b59b6', '#ff9ff3'];
        
        for (let i = 0; i < 50; i++) {
            const confetti = document.createElement('div');
            confetti.className = 'confetti';
            confetti.style.left = Math.random() * 100 + 'vw';
            confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            confetti.style.animationDelay = Math.random() * 5 + 's';
            confetti.style.animationDuration = (Math.random() * 3 + 4) + 's';
            confetti.style.borderRadius = Math.random() > 0.5 ? '50%' : '0';
            container.appendChild(confetti);
        }
    };

    /**
     * Get new love message via AJAX
     */
    window.getNewMessage = function() {
        fetch('/api/love-message/')
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                var messageEl = document.getElementById('loveMessage');
                if (messageEl) {
                    messageEl.textContent = data.message;
                }
            })
            .catch(function(error) {
                console.error('Error fetching message:', error);
            });
    };

    /**
     * Create floating notes
     */
    window.createFloatingNotes = function() {
        const container = document.getElementById('floatingNotes');
        if (!container) return;

        fetch('/api/floating-notes/')
            .then(function(response) {
                return response.json();
            })
            .then(function(data) {
                data.notes.forEach(function(note, index) {
                    const noteEl = document.createElement('div');
                    noteEl.className = 'floating-note';
                    noteEl.textContent = note;
                    noteEl.style.left = (Math.random() * 80 + 10) + 'vw';
                    noteEl.style.top = (Math.random() * 60 + 20) + 'vh';
                    noteEl.style.animationDelay = (index * 2) + 's';
                    container.appendChild(noteEl);
                });
            })
            .catch(function(error) {
                console.error('Error fetching notes:', error);
            });
    };

    /**
     * Create mouse trail effect
     */
    window.createMouseTrail = function() {
        document.addEventListener('mousemove', function(e) {
            if (Math.random() > 0.9) {
                const heart = document.createElement('div');
                heart.innerHTML = '💕';
                heart.style.position = 'fixed';
                heart.style.left = e.clientX + 'px';
                heart.style.top = e.clientY + 'px';
                heart.style.pointerEvents = 'none';
                heart.style.fontSize = '1rem';
                heart.style.animation = 'floatUp 2s ease-out forwards';
                heart.style.zIndex = '9999';
                document.body.appendChild(heart);

                setTimeout(function() {
                    heart.remove();
                }, 2000);
            }
        });
    };

})();
