from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = (
        "id",
        "titulo",
        "autor",
        "data",
        "publicado",
        "categoria",
    )

    list_editable = ("publicado",)
    list_display_links = (
        "id",
        "titulo",
    )
    summernote_fields = ("conteudo", "")
