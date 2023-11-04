from django.urls import path

from .views import baseapp_page

urlpatterns=[
    path('',baseapp_page,name='base')
]