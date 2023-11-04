from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'Invaildes')
            return redirect('login')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalied username or password')
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Already Account')
            print('Already Account')
            return redirect('register')

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username)

        user.set_password(password)
        user.save()
        print('Create account successfully')
    return render(request, 'register.html')
# Create your views here.
