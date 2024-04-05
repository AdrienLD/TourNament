from django.contrib import admin
from .models import Tournoi, Match, Equipe, Joueur

admin.site.register(Tournoi)
admin.site.register(Match)
admin.site.register(Equipe)
admin.site.register(Joueur)
