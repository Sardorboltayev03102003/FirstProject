from django.contrib import admin

from .models import *


class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu_name', 'menu_about', 'menu_price', 'menu_image', 'created_at']
    search_fields = ['menu_name']


class Menu_CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'jobs', 'about', 'created_at')
    search_fields = ('id', 'name')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Menu_Customer, Menu_CustomerAdmin)

# Register your models here.
