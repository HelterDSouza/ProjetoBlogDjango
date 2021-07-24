from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class Comentario(models.Model):
    nome_comentario = models.CharField(max_length=150)
    email_comentario = models.EmailField()
    comentario = models.TextField()
    post_comentario = models.ForeignKey(
        "posts.Post", related_name="post_comentario", on_delete=models.CASCADE
    )
    usuario_comentario = models.ForeignKey(
        User, related_name="user", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    data_comentario = models.DateTimeField(default=timezone.now)
    publicado_comentario = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_comentario
