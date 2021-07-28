from django import forms

from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = (
            "nome_comentario",
            "email_comentario",
            "comentario",
        )
        labels = {"nome_comentario": "Autor", "email_comentario": "Email"}
        widgets = {
            "nome_comentario": forms.widgets.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "email_comentario": forms.widgets.EmailInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "comentario": forms.widgets.Textarea(
                attrs={
                    "class": "form-control",
                },
            ),
        }

    def clean(self):
        data = self.cleaned_data
        nome = data.get("nome_comentario")
        email = data.get("email_comentario")
        comentario = data.get("comentario")
        if len(nome) < 5:
            self.add_error("nome_comentario", "nome precisa ter mais de 5 caracteres.")

        if not email:
            self.add_error("email_comentario", "ddddddd.")
