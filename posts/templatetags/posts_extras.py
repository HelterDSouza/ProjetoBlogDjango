from django import template

register = template.Library()


@register.filter(name="plural_comentarios")
def plural_comentario(value):
    try:
        value = int(value)

        if value == 0:
            return f"nenhum comentário"
        elif value == 0:
            return f"{value} comentário"
        else:
            return f"{value} comentários"

    except:

        return f"{value} comentário(s)"
