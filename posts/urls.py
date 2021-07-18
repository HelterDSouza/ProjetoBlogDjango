from django.urls import path

from . import views

app_name = "posts"


urlpatterns = [
    path("", views.PostIndex.as_view(), name="index"),
    path("post/<int:pk>", views.PostDetalheUpdateView.as_view(), name="post_detalhes"),
]
