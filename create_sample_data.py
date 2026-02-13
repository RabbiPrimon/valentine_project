#!/usr/bin/env python
"""
Script to create sample love messages for the Valentine's Day website.
"""

import os
import sys
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'valentine_project.settings')
django.setup()

from valentine_main.models import LoveMessage

def create_sample_messages():
    """Create sample love messages."""
    
    messages = [
        "You are the love of my life, my soulmate, and my best friend.",
        "Every moment with you is a treasure I cherish.",
        "You make my heart skip a beat every time I see you.",
        "I love you more than words can express.",
        "You are my sunshine on cloudy days.",
        "Being with you is the best thing that ever happened to me.",
        "I fall in love with you more and more every day.",
        "You complete me in every way possible.",
        "My love for you grows stronger each passing day.",
        "You are the reason I believe in love.",
    ]
    
    authors = [
        "Romeo",
        "Shakespeare", 
        "Your Valentine",
        "Romeo",
        "Your Secret Admirer",
        "Your Sweetheart",
        " Forever Yours",
        "Love Doctor",
        "Your Soulmate",
        "Cupid",
    ]
    
    created_count = 0
    for i, (message, author) in enumerate(zip(messages, authors)):
        LoveMessage.objects.get_or_create(
            message=message,
            defaults={
                'author': author,
                'is_active': True
            }
        )
        created_count += 1
        print(f"Created message {i+1}: {message[:30]}...")
    
    print(f"\n{created_count} sample love messages created successfully!")
    print(f"Total messages in database: {LoveMessage.objects.count()}")

if __name__ == '__main__':
    create_sample_messages()
