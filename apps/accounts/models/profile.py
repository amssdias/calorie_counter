import uuid
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    weight_target = models.IntegerField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
