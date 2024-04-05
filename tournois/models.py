from django.db import models

class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class Tournoi(models.Model):
    TYPE_SPORT_CHOICES = [
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('tennis', 'Tennis'),
        ('rugby', 'Rugby'),
        ('volleyball', 'Volleyball'),
        ('handball', 'Handball'),
        ('pingpong', 'Ping Pong'),
        ('badminton', 'Badminton'),
        ('boxe', 'Boxe'),
        ('natation', 'Natation'),
        ('athletisme', 'Athlétisme'),
        ('golf', 'Golf')
    ]
    nom = models.CharField(max_length=100)
    type_sport = models.CharField(max_length=50, choices=TYPE_SPORT_CHOICES)
    equipes = models.ManyToManyField(Equipe, related_name='tournois')

    def __str__(self):
        return self.nom


class Match(models.Model):
    tournoi = models.ForeignKey(Tournoi, on_delete=models.CASCADE)
    equipe1 = models.ForeignKey(Equipe, related_name='matchs_as_e1', on_delete=models.CASCADE, null=True)
    equipe2 = models.ForeignKey(Equipe, related_name='matchs_as_e2', on_delete=models.CASCADE, null=True)
    score_equipe1 = models.IntegerField(default=0)
    score_equipe2 = models.IntegerField(default=0)

class Joueur(models.Model):
    nom = models.CharField(max_length=100)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='joueurs')