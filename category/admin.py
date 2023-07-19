from django.contrib import admin
from .models import Genre, Device

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Genre, GenreAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Device, DeviceAdmin)
