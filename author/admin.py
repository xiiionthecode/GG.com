from django.contrib import admin
from .models import Author, AuthorInfo, AuthorReport

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Author, AuthorAdmin)

class AuthorInfoAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(AuthorInfo, AuthorInfoAdmin)

class AuthorReportAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(AuthorReport, AuthorReportAdmin)
