from django.urls import path

from .views import *

urlpatterns=[
    path('contact/',register_page,name='register'),
    path('login/',login_page, name='login'),
    path('home/',home,name='home'),
]