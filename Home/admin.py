from django.contrib import admin
from Home.models import HistoryItem


@admin.register(HistoryItem)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('user', 'character', 'theme')
    list_filter = ['user', 'character']
    search_fields = ['user', 'character']