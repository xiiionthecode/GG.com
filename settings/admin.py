from django.contrib import admin
from .models import Generally, LandingPage

class GenerallyAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Generally, GenerallyAdmin)

class LandingPageAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(LandingPage, LandingPageAdmin)
