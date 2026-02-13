#!/usr/bin/env python
"""
Script to create a superuser for the Valentine's Day website.
"""

import os
import sys
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'valentine_project.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    """Create a superuser with the specified credentials."""
    
    username = 'user-admin'
    password = 'admin123'
    email = 'admin@valentine.com'
    
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists. Updating password...")
        user = User.objects.get(username=username)
        user.set_password(password)
        user.save()
        print(f"Password updated for user '{username}'")
    else:
        # Create the superuser
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Superuser '{username}' created successfully!")
    
    print(f"\nLogin credentials:")
    print(f"  Username: {username}")
    print(f"  Password: {password}")
    print(f"  Admin URL: http://localhost:8000/admin/")

if __name__ == '__main__':
    create_superuser()
