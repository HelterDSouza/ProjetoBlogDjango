from django.urls import path

from . import views

app_name = "posts"


urlpatterns = [
    path("", views.PostIndex.as_view(), name="index"),
    path("post/<int:pk>", views.PostDetalheView.as_view(), name="post_detalhes"),
    path(
        "categoria/<str:categoria>",
        views.PostCategoriaListView.as_view(),
        name="post_categoria",
    ),
    path("busca/", views.PostBuscaListView.as_view(), name="post_busca"),
]
