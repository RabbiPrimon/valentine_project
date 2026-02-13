"""
Views for Valentine's Day website.

This module defines the views for rendering the Valentine's Day website pages,
including the home page with animations, gallery, and other features.
"""

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Image, LoveMessage
import random
from datetime import datetime


def home(request):
    """
    View for the home page with colorful animations and features.
    
    Displays:
    - Animated floating hearts
    - Colorful gradient backgrounds
    - Falling confetti
    - Pulsing "Happy Valentine's Day" text
    - Countdown timer to Valentine's Day
    - Love message generator
    - Floating love notes
    """
    
    # Get active love messages
    love_messages = LoveMessage.objects.filter(is_active=True)
    random_message = random.choice(love_messages) if love_messages.exists() else None
    
    # Countdown to Valentine's Day
    today = datetime.now()
    current_year = today.year
    valentine_date = datetime(current_year, 2, 14)
    
    # If Valentine's Day has passed this year, use next year
    if today > valentine_date:
        valentine_date = datetime(current_year + 1, 2, 14)
    
    days_until = (valentine_date - today).days
    hours_until = 24 - today.hour
    minutes_until = 60 - today.minute
    
    context = {
        'days_until': days_until,
        'hours_until': hours_until,
        'minutes_until': minutes_until,
        'random_message': random_message,
        'love_messages': love_messages,
    }
    
    return render(request, 'valentine_main/home.html', context)


def gallery(request):
    """
    View for the photo gallery page.
    
    Displays Valentine-themed images with hover effects.
    Only shows active images.
    """
    
    images = Image.objects.filter(is_active=True).order_by('-uploaded_at')
    
    context = {
        'images': images,
    }
    
    return render(request, 'valentine_main/gallery.html', context)


@require_http_methods(["GET"])
def get_love_message(request):
    """
    AJAX view to get a random love message.
    
    Returns:
        JsonResponse with a random love message
    """
    
    messages = LoveMessage.objects.filter(is_active=True)
    
    if messages.exists():
        message = random.choice(messages)
        return JsonResponse({
            'message': message.message,
            'author': message.author if message.author else 'Anonymous'
        })
    
    return JsonResponse({
        'message': 'Happy Valentine\'s Day!',
        'author': 'System'
    })


@require_http_methods(["GET"])
def get_floating_notes(request):
    """
    AJAX view to get floating love notes.
    
    Returns:
        JsonResponse with a list of floating love notes
    """
    
    notes = [
        "You are my sunshine ☀️",
        "I love you more than pizza 🍕",
        "Be mine forever 💕",
        "Love is in the air 💘",
        "You make my heart skip a beat 💓",
        "Together forever ❤️",
        "My heart belongs to you 💖",
        "Love you to the moon and back 🌙",
        "You are my everything 💝",
        "Happy Valentine's Day! 💗",
    ]
    
    # Return 5 random notes
    random_notes = random.sample(notes, min(5, len(notes)))
    
    return JsonResponse({
        'notes': random_notes
    })
