from django.db import models
from django.conf import settings


class Character(models.Model):
    name = models.CharField(max_length=50, null=False)
    art_forms = models.CharField(max_length=100, null=True, blank=True)
    art_preference = models.CharField(max_length=100, null=True, blank=True)
    art_inspiration = models.CharField(max_length=100, null=True, blank=True)
    art_emotions = models.CharField(max_length=100, null=True, blank=True)
    art_themes = models.CharField(max_length=100, null=True, blank=True)
    art_creation = models.CharField(max_length=100, null=True, blank=True)
    art_role = models.CharField(max_length=100, null=True, blank=True)
    art_feedback = models.CharField(max_length=100, null=True, blank=True)
    art_goals = models.CharField(max_length=100, null=True, blank=True)
    creative_process = models.CharField(max_length=100, null=True, blank=True)
    technical_skill = models.CharField(max_length=100, null=True, blank=True)
    art_experimentation = models.CharField(max_length=100, null=True, blank=True)
    target_audience = models.CharField(max_length=100, null=True, blank=True)
    cultural_influences = models.CharField(max_length=100, null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=False)

    def __str__(self):
        return self.name
