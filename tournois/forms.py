from django import forms
from .models import Tournoi, Equipe, Match, Joueur

class TournoiForm(forms.ModelForm):
    class Meta:
        model = Tournoi
        fields = ['nom', 'type_sport']


class EquipeForm(forms.ModelForm):

    class Meta:
        model = Equipe
        fields = ['nom']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['equipe1', 'equipe2', 'score_equipe1', 'score_equipe2']

    def __init__(self, *args, **kwargs):
        tournoi = kwargs.pop('tournoi', None)
        super(MatchForm, self).__init__(*args, **kwargs)
        if tournoi:
            self.fields['equipe1'].queryset = Equipe.objects.filter(tournois=tournoi).order_by('nom')
            self.fields['equipe2'].queryset = Equipe.objects.filter(tournois=tournoi).order_by('nom')
        else:
            self.fields['equipe1'].queryset = Equipe.objects.none()
            self.fields['equipe2'].queryset = Equipe.objects.none()

class JoueurForm(forms.ModelForm):
    class Meta:
        model = Joueur
        fields = ['nom', 'equipe']