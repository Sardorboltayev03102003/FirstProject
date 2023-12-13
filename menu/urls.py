from django.urls import path

from .models import Menu
from .views import menu_page

urlpatterns = [
    path('menu/', menu_page, name="menu"),

]
