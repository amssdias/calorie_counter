from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from apps.foods.models import Food
from apps.foods.models.registered_food import RegisteredFood


@receiver(post_save, sender=Food)
def slugify_food(sender, instance, created, *args, **kwargs):
    if created:
        new_slug = f"{instance.name} {instance.id} {instance.brand}"
        instance.slug = slugify(new_slug)
        instance.save()

@receiver(post_save, sender=RegisteredFood)
def slugify_food(sender, instance, created, *args, **kwargs):
    if created:
        new_slug = f"{instance.food.name} {instance.meal} {instance.user.uuid}"
        instance.slug = slugify(new_slug)
        instance.save()
