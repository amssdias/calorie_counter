from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from apps.foods.models import Food


@receiver(post_save, sender=Food)
def slugify_food(sender, instance, created, *args, **kwargs):
    if created:
        new_slug = f"{instance.name} {instance.brand}"
        instance.slug = slugify(new_slug)
        instance.save()