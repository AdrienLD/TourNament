from django.urls import path
from .views import TournoiListView , ajouter_tournoi, add_equipe, gestion_match, liste_matchs, ajouter_joueur

urlpatterns = [
    path('list/', TournoiListView.as_view(), name='liste_tournois'),
    path('add-tournoi/', ajouter_tournoi, name='add_tournois'),
    path('add-equipe/<str:nom_tournoi>/', add_equipe, name='add_equipe'),
    path('add-match/<str:nom_tournoi>/', gestion_match, name='add_match'),
    path('match/<str:nom_tournoi>/', liste_matchs, name='liste_matchs'),
    path('add-joueur/<str:nom_team>', ajouter_joueur, name='add_joueur')
]
