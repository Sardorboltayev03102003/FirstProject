from django.contrib import admin

from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu_name', 'menu_about', 'menu_price', 'menu_image', 'created_at']
    search_fields = ['menu_name']


admin.site.register(Menu, MenuAdmin)

# Register your models here.
