from django.shortcuts import render

from .models import About


def about_page(request):
    about = About.objects.all()
    ctx = {
        "about": about,
    }
    return render(request, 'about.html', ctx)

# Create your views here.
