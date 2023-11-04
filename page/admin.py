from django.contrib import admin

from .models import Stuff, Gallery, Reservation


class StuffAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'job']
    search_fields = ['name']


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    search_fields = ['image']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'place', 'name', 'email', 'number']
    search_fields = ['name']


admin.site.register(Stuff, StuffAdmin),
admin.site.register(Gallery, GalleryAdmin),
admin.site.register(Reservation, ReservationAdmin),

# Register your models here.
