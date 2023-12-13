from django.shortcuts import render

from .models import Contact, Footer

print(222222222222222)


def contact_page(request):
    return render(request, 'contact.html')


def footer_page(request):
    footer = Footer.objects.all().first()
    ctx = {
        "footer": footer,

    }

    return render(request, "base.html", ctx)


def footer_page_menu(request):
    footer = Footer.objects.all().first()
    ctx = {
        "footer_menu": footer,

    }

    return render(request, "menu.html", ctx)
# Create your views here.
