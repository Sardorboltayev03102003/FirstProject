from django.shortcuts import render
from .models import *


def menu_page(request):
    menu = Menu.objects.all()

    ctx = {
        "menu": menu,
    }
    return render(request, 'menu.html', ctx)


def menu_customer_page(request):
    menu = Menu_Customer.objects.all()

    ctx = {
        "menu_customer": menu,
    }
    return render(request, 'menu.html', ctx)
# Create your views here.
