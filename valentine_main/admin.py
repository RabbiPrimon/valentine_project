"""
Admin configuration for Valentine's Day website.

This module defines the admin interface for managing the website's content,
including images and love messages.
"""

from django.contrib import admin
from .models import Image, LoveMessage


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Image model.
    
    Allows admin users to manage gallery images through the Django admin interface.
    """
    
    list_display = ('title', 'uploaded_by', 'uploaded_at', 'is_active')
    list_filter = ('is_active', 'uploaded_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
    readonly_fields = ('uploaded_at',)
    
    fieldsets = (
        ('Image Information', {
            'fields': ('title', 'image', 'description')
        }),
        ('Metadata', {
            'fields': ('uploaded_by', 'uploaded_at', 'is_active'),
            'classes': ('collapse',)
        }),
    )


@admin.register(LoveMessage)
class LoveMessageAdmin(admin.ModelAdmin):
    """
    Admin configuration for the LoveMessage model.
    
    Allows admin users to manage love messages through the Django admin interface.
    """
    
    list_display = ('message', 'author', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('message', 'author')
    list_editable = ('is_active',)
    readonly_fields = ('created_at',)
