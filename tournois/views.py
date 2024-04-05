from django.views.generic import ListView
from .models import Equipe, Match, Tournoi, Joueur
from .forms import TournoiForm, EquipeForm, MatchForm, JoueurForm
from django.shortcuts import render, redirect, get_object_or_404

class TournoiListView(ListView):
    model = Tournoi
    template_name = 'tournois.html'
    context_object_name = 'tournois'


def ajouter_tournoi(request):
    if request.method == 'POST':
        form = TournoiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_tournois') 
    else:
        form = TournoiForm()
    return render(request, 'ajout_tournoi.html', {'form': form})

def add_equipe(request, nom_tournoi):
    tournoi = get_object_or_404(Tournoi, nom=nom_tournoi)
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            equipe = form.save(commit=False)
            equipe.save()
            tournoi.equipes.add(equipe)
    else:
        form = EquipeForm()
    return render(request, 'ajout_equipe.html', {'form': form})

def gestion_match(request, nom_tournoi):
    tournoi = get_object_or_404(Tournoi, nom=nom_tournoi)
    if request.method == 'POST':
        form = MatchForm(request.POST, tournoi=tournoi)
        if form.is_valid():
            match = form.save(commit=False)
            match.tournoi = tournoi
            match.save()
            return redirect('liste_tournois')
    else:
        form = MatchForm(tournoi=tournoi)
    return render(request, 'ajout_match.html', {'form': form, 'tournoi': tournoi})

def liste_matchs(request, nom_tournoi):
    tournoi = get_object_or_404(Tournoi, nom=nom_tournoi)
    matchs = Match.objects.filter(tournoi=tournoi)
    return render(request, 'matchs.html', {'tournoi': tournoi, 'matchs': matchs})

def ajouter_joueur(request, nom_team):
    team = get_object_or_404(Equipe, nom=nom_team)
    if request.method == 'POST':
        form = JoueurForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = JoueurForm()
    return render(request, 'ajout_joueur.html', {'form': form})