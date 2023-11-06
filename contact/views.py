from django.shortcuts import render

from .models import Contact, Footer


def contact_page(request):
    contacts = Contact.objects.all()

    if request.method == "POST":
        model = Contact.objects.create(full_name=request.POST.get('full_name', None),
                                       email=request.POST.get('email'),
                                       place=request.POST.get('place', None),
                                       message=request.POST.get('message', None)
                                       )
    return render(request, 'contact.html')
def footer_page(request):
    footer=Footer.objects.all().first()
    ctx={
        "footer":footer,

    }

    return render(request,"base.html",ctx)
# Create your views here.
