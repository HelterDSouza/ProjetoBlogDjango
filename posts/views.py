from typing import ItemsView

from categorias.models import Categoria
from django.db.models import Case, Count, Q, When
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from .models import Post


# Create your views here.
class PostIndex(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset().filter(publicado=True)
        qs = qs.order_by("-id")
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(When(post_comentario__publicado_comentario=True, then=1))
            )
        )
        return qs


class PostDetalheUpdateView(UpdateView):
    model = Post


class PostCategoriaListView(PostIndex):
    template_name = "posts/post_categoria.html"

    def get_queryset(self):
        qs = super().get_queryset()
        categoria = self.kwargs.get("categoria", None)
        if not categoria:
            return qs
        qs = qs.filter(categoria__nome_categoria__iexact=categoria)
        return qs


class PostBuscaListView(PostIndex):
    template_name = "posts/post_busca.html"



