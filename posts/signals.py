from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from PIL import Image

from .models import Post


@receiver(post_save, sender=Post, dispatch_uid="update_post_title")
def resize_image(sender, instance, **kwargs):
    NEW_WIDTH = 800
    img = Image.open(instance.image.path)

    width, height = img.size
    new_height = round((NEW_WIDTH * height) / width)
    if width <= NEW_WIDTH:
        img.close()

        return

    img.resize((NEW_WIDTH, new_height)).save(instance.image.path)
    img.close()
