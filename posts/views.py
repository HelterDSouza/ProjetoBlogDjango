from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

# Create your views here.


def index(request):
    return render(request, "", {})