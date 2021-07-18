from typing import ItemsView

from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .models import Post


# Create your views here.
class PostIndex(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"


class PostDetalheUpdateView(UpdateView):
    model = Post
