# Generated by Django 2.2.7 on 2020-04-23 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Userapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(default=None, max_length=255)),
                ('email', models.CharField(default=None, max_length=255)),
                ('password', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=255)),
                ('species', models.CharField(blank=True, choices=[(1, 'insectes'), (2, 'mollusques'), (3, 'mammifères'), (4, 'oiseaux'), (5, 'poissons'), (6, 'amphobiens'), (7, 'reptiles'), (8, 'plantes'), (9, 'autres')], default=None, max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default=None, max_length=1)),
                ('content', models.TextField(default=None)),
                ('photo', models.ImageField(blank=True, default=None, upload_to='media/')),
                ('country', django_countries.fields.CountryField(blank=True, default=None, max_length=2)),
                ('locations', models.CharField(blank=True, choices=[(1, 'Alsace'), (2, 'Aquitaine'), (3, 'Auvergne'), (4, 'Basse-Normandie'), (5, 'Bourgogne'), (6, 'Bretagne'), (7, 'Centre'), (8, 'Champagne-Ardenne'), (9, 'Corse'), (10, 'Franche-Comté'), (11, 'Haute-Normandie'), (12, 'Île-de-France'), (13, 'Languedoc-Roussillon'), (14, 'Limousin'), (15, 'Lorraine'), (16, 'Midi-Pyrénées'), (17, 'Nord-Pas-de-Calais'), (18, 'Pays de la Loire'), (19, 'Picardie'), (20, 'Poitou-Charentes'), (21, 'Provence-Alpes-Côte d Azur'), (22, 'Rhône-Alpes'), (23, 'Mayotte'), (24, 'Martinique'), (25, 'Guadeloupe'), (26, 'Reunion'), (27, 'Guyane'), (28, 'etranger')], default=None, max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
