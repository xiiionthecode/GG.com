from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Author(models.Model):
    mail = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=32)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Author"

    def __str__(self):
         return self.username
    

class AuthorInfo(models.Model):
    Author = models.OneToOneField(Author, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = "Informations"
        verbose_name_plural = "Informations"

    def __str__(self):
         return self.display_name + "(" + Author.username + ")"

class AuthorReport(models.Model):
    Author = models.OneToOneField(Author, on_delete=models.CASCADE)
    blogs = models.IntegerField(default=0)
    note = RichTextField()

    class Meta :
        verbose_name = "Reports"
        verbose_name_plural = "Reports"

    def __str__(self):
         return self.Author.username
