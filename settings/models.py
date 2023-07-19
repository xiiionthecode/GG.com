from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime
import uuid, os
from ckeditor.fields import RichTextField 

class Generally(models.Model):
    logo = models.ImageField(upload_to="Importants/")
    icon = models.ImageField(upload_to="Importants/") 
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


    class Meta:
        verbose_name = "Generally"
        verbose_name_plural = "Generally"

class LandingPage(models.Model):
    meta_title = models.TextField()
    meta_descriptions = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)


    class Meta:
        verbose_name = "LandingPage"
        verbose_name_plural = "Landing Page"

