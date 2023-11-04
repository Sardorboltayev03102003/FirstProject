from django.shortcuts import render


def baseapp_page(request):
    return render(request, 'base.html')

# Create your views here.
