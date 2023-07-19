from django.contrib import admin
from .models import Blog, BlogReports, BlogTag

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Blog, BlogAdmin)

class BlogReportsAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(BlogReports, BlogReportsAdmin)

class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(BlogTag, BlogTagAdmin)
