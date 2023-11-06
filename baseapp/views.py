from django.shortcuts import render
from contact.models import Footer

def generate_url(lon, lat):
    return f'https://www.google.com/maps/@{lon},{lat}z?entry=ttu'

def baseapp_page(request):
    footer = Footer.objects.all().first()
    ctx = {
        "footer": footer,
        'url': generate_url(lon=footer.longitude, lat=footer.latitude)
    }
    return render(request, 'base.html', context=ctx)

# Create your views here.
