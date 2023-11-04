from django.shortcuts import render

from .models import Contact


def contact_page(request):
    contacts = Contact.objects.all()

    if request.method == "POST":
        model = Contact.objects.create(full_name=request.POST.get('full_name', None),
                                       email=request.POST.get('email'),
                                       place=request.POST.get('place', None),
                                       message=request.POST.get('message', None)
                                       )
    return render(request, 'contact.html')

# Create your views here.
