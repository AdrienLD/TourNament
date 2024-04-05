# Generated by Django 3.2.25 on 2024-04-05 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tournoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type_sport', models.CharField(max_length=50)),
                ('matchs', models.ManyToManyField(related_name='tournois', to='tournois.Match')),
                ('equipes', models.ManyToManyField(related_name='tournois', to='tournois.Equipe')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='gagnant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='won_matches', to='tournois.equipe'),
        ),
        migrations.AddField(
            model_name='match',
            name='equipe1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='tournois.equipe'),
        ),
        migrations.AddField(
            model_name='match',
            name='equipe2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='tournois.equipe'),
        ),
    ]
