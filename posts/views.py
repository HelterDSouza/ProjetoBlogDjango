from typing import ItemsView

from categorias.models import Categoria
from comentarios.forms import ComentarioForm
from comentarios.models import Comentario
from django.contrib import messages
from django.db.models import Case, Count, Q, When
from django.shortcuts import redirect, render
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
    template_name = "posts/post_detalhe.html"
    form_class = ComentarioForm
    context_object_name = "post"

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post
        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user

        comentario.save()
        messages.success(self.request, "Comentario enviado com sucesso")
        return redirect("posts:post_detalhes", pk=post.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(
            post_comentario=post,
            publicado_comentario=True,
        )
        context["comentarios"] = comentarios
        return context


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

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get("termo", None)
        if not termo:
            return qs
        qs = qs.filter(
            Q(titulo__icontains=termo)
            | Q(autor__first_name__iexact=termo)
            | Q(conteudo__icontains=termo)  # Tirar Talvez
            | Q(excerto__icontains=termo)
            | Q(categoria__nome_categoria__iexact=termo)
        )

        return qs
