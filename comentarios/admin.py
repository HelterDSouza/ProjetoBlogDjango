from django.contrib import admin

from .models import Comentario


# Register your models here.
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome_comentario",
        "email_comentario",
        "usuario_comentario",
        "data_comentario",
        "publicado_comentario",
    )
    list_editable = ("publicado_comentario",)
    list_display_links = (
        "id",
        "nome_comentario",
        "email_comentario",
    )
