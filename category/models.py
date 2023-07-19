from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)
    hex_color_code = models.CharField(max_length=255)
    URL = models.CharField(max_length=255, unique=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Genres"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=255)
    URL = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Devices"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.name