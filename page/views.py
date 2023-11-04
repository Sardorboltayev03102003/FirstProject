from django.shortcuts import render

from .models import Stuff, Gallery, Reservation


def reservation_page(request):
    if request.method == "POST":
        model = Reservation()
        model.data=request.POST.get('data',None)
        model.person = request.POST.get('person', None)
        model.name = request.POST.get('name', None)
        model.email = request.POST.get('email', None)
        model.number = request.POST.get('number', None)
        model.save()
    return render(request, 'reservation.html')


def stuff_page(request):
    stuff = Stuff.objects.all()
    ctx = {
        "stuff": stuff
    }

    return render(request, 'stuff.html', ctx)


def gallery_page(request):
    gallery = Gallery.objects.all()

    ctx = {
        "gallery": gallery
    }
    return render(request, 'gallery.html', ctx)

# Create your views here.
