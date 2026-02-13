"""
Models for Valentine's Day website.

This module defines the database models for the Valentine's Day website,
including the Image model for the photo gallery.
"""

from django.db import models
from django.contrib.auth.models import User


class Image(models.Model):
    """
    Model representing a Valentine-themed image in the gallery.
    
    Attributes:
        title (str): The title of the image
        image (file): The image file itself
        description (str): Optional description of the image
        uploaded_by (User): The user who uploaded the image
        uploaded_at (datetime): When the image was uploaded
        is_active (bool): Whether the image is displayed in the gallery
    """
    
    title = models.CharField(max_length=200, verbose_name='Image Title')
    image = models.ImageField(upload_to='valentine_gallery/', verbose_name='Image File')
    description = models.TextField(blank=True, verbose_name='Description')
    uploaded_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='uploaded_images',
        verbose_name='Uploaded By'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Uploaded At')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    
    class Meta:
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return self.title


class LoveMessage(models.Model):
    """
    Model representing a love message that can be displayed on the website.
    
    Attributes:
        message (str): The love message text
        author (str): The author of the message (optional)
        is_active (bool): Whether the message is displayed
        created_at (datetime): When the message was created
    """
    
    message = models.TextField(verbose_name='Love Message')
    author = models.CharField(max_length=100, blank=True, verbose_name='Author')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    
    class Meta:
        verbose_name = 'Love Message'
        verbose_name_plural = 'Love Messages'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.message[:50] + '...' if len(self.message) > 50 else self.message
