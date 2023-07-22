from django.db import models
from django.utils.translation import gettext as _
import uuid
from datetime import datetime

class GenderChoices(models.IntegerChoices):
    null = 0 ,
    male = 1 ,
    female = 2 , 
    whatyounedd = 3 ,

class AdminLogin(models.Model):
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=datetime.now)
    
