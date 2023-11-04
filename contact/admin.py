from django.contrib import admin

from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'place', 'message',  'created_at']
    search_fields = ['name']

admin.site.register(Contact, ContactAdmin)
# Register your models here.
