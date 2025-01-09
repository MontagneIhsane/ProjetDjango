from django.contrib import admin
from .models import Carte

@admin.register(Carte)
class carteAdmin(admin.ModelAdmin):
    list_display = ( 'titre','nom', 'image', 'date_naissance', 'poste', 'equipe')