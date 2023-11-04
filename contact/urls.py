from django.urls import path

from .models import *
from .views import *

urlpatterns = [
    path('contact/', contact_page, name='contact')
]
