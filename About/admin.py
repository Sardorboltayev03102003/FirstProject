from django.contrib import admin

from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'text','body', 'created_at']
    search_fields = ['name']


admin.site.register(About, AboutAdmin)

# Register your models here.
