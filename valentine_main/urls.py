"""
URL configuration for valentine_main app.

This module defines the URL patterns for the Valentine's Day website.
"""

from django.urls import path
from . import views

app_name = 'valentine_main'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('api/love-message/', views.get_love_message, name='get_love_message'),
    path('api/floating-notes/', views.get_floating_notes, name='get_floating_notes'),
]
