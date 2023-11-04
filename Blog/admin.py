from django.contrib import admin

from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'theme', 'title', 'text','text2','text3', 'image', 'user', 'created_at']
    search_fields = ['id', 'theme']


admin.site.register(Blog, BlogAdmin)
# Register your models here.
