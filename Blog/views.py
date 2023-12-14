from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from .models import Blog


def blog_page(request):
    blo = Blog.objects.all()
    ctx = {
        "blo": blo,
    }
    return render(request, 'blog.html', ctx)


def details(request):
    details = Blog.objects.first()
    ctx = {
        "details": details,
    }
    return render(request, "details.html", ctx)
# Create your views here.
