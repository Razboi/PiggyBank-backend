from django.db import models
from django.conf import settings


class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name
