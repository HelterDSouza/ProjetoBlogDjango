from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, related_name="autor", on_delete=models.DO_NOTHING)
    data = DateTimeField(default=timezone.now)
    conteudo = models.TextField()
    excerto = models.TextField()
    categoria = models.ForeignKey(
        "categorias.Categoria",
        related_name="categoria",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to="post/img/%Y/%m/%d", blank=True, null=True)
    publicado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo
