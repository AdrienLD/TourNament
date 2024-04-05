# Generated by Django 3.2.25 on 2024-04-05 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournois', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournoi',
            name='type_sport',
            field=models.CharField(choices=[('football', 'Football'), ('basketball', 'Basketball'), ('tennis', 'Tennis'), ('rugby', 'Rugby'), ('volleyball', 'Volleyball'), ('handball', 'Handball'), ('pingpong', 'Ping Pong'), ('badminton', 'Badminton'), ('boxe', 'Boxe'), ('natation', 'Natation'), ('athletisme', 'Athlétisme'), ('golf', 'Golf')], max_length=50),
        ),
    ]
