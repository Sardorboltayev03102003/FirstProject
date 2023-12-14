from django.contrib import admin

from contact.models import Contact, Footer


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'place', 'message', 'created_at']
    search_fields = ['name']


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'email', 'location',)
    search_fields = ('number',)





admin.site.register(Contact, ContactAdmin),
admin.site.register(Footer, FooterAdmin)
# Register your models here.
