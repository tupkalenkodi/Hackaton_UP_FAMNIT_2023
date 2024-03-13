from django.db import models
from django.conf import settings
from Character.models import Character


class HistoryItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    theme = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.theme
