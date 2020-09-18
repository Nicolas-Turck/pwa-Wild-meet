from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
"""class Userapp(models.Model):
    class for user account
    pseudo = models.CharField(max_length=255,default=None)
    email = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=255,default=None)"""


class Encounter(models.Model):
    """class for register encounter """
    title = models.CharField(max_length=255,default=None)
    TYPES_CHOICES = (
        ('empreintes', 'empreintes'),
        ('déjection', 'déjection'),
        ('terrier', 'terrier'),
        ('pots', 'pots'),
        ('poils', 'poils'),
        ('plumes', 'plumes'),
        ('pelote de déjection', 'pelote de déjection'),
        ('reste de repas', 'reste de repas'),
        ('grattage au sol ', 'grattage aux sol'),
        ('marquage sur végétations', 'marquage sur végétations'),
        ('coulées', 'coulées'),
        ('couches', 'couches'),
    )
    types = models.CharField(max_length=100, choices=TYPES_CHOICES, default=None, blank=True)
    BIOTOPES_CHOICES = (
        ('foret', 'foret'),
        ('bois', 'bois'),
        ('clairiere', 'clairieres'),
        ('cultures', 'cultures'),
        ('parc urbain et jardin', 'parc urbain et jardin'),
        ('haies chemin bord de route', 'haies chemin bord de route'),
        ('terrain en friches terrain vagues', 'terrain en friches terrain vagues'),
        ('verger bosquets', 'verger bosquets'),
        ('falaise', 'falaise'),
        ('grotte', 'grotte'),
        ('point d eau', 'point d eau'),
        ('tourbieres ou marais ', 'tourbieres ou marais'),
        ('dune', 'dune'),
        ('bras de mer ', 'bras de mer'),
        ('estuaires', 'estuaires'),
        ('marais salées', 'marais salées'),
        ('cotes rocheuse falaises maritimes', 'cotes rocheuse falaises maritimes'),


    )
    biotopes = models.CharField(max_length=100, choices=BIOTOPES_CHOICES, default=None, blank=True)
    RELIEF_CHOICES = (
        ('montagnes', 'montagnes'),
        ('plateaux, vallées', 'plateaux, vallées'),
        ('plaines', 'plaines'),

    )
    relief = models.CharField(max_length=100, choices=RELIEF_CHOICES, default=None, blank=True)
    """SPECIES_CHOICES = (
        ('insectes', 'insectes'),
        ('mollusques', 'mollusques'),
        ('mammifères', 'mammifères'),
        ('oiseaux', 'oiseaux'),
        ('poissons', 'poissons'),
        ('amphibiens', 'amphibiens'),
        ('reptiles', 'reptiles'),
        ('plantes', 'plantes'),
        ('autres', 'autres')
    )
    species = models.CharField(max_length=100, choices=SPECIES_CHOICES, default=None,  blank=True)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Femelle', 'Female'),
    )
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES,default=None, blank=True)"""
    content = models.TextField(default=None)
    photo = models.ImageField(upload_to='media/', default=None, blank=True)
    #country = CountryField(blank_label='(select country)', default=None, blank=True)
    LOCATIONS_CHOICES = (
        ('Alsace', 'Alsace'),
        ('Aquitaine', 'Aquitaine'),
        ('Auvergne', 'Auvergne'),
        ('Basse-Normandie', 'Basse-Normandie'),
        ('Bourgogne', 'Bourgogne'),
        ('Bretagne', 'Bretagne'),
        ('Centre', 'Centre'),
        ('Champagne-Ardenne', 'Champagne-Ardenne'),
        ('Corse', 'Corse'),
        ('Franche-Comté', 'Franche-Comté'),
        ('Haute-Normandie', 'Haute-Normandie'),
        ('Île-de-France', 'Île-de-France'),
        ('Languedoc-Roussillon', 'Languedoc-Roussillon'),
        ('Limousin', 'Limousin'),
        ('Lorraine', 'Lorraine'),
        ('Midi-Pyrénées', 'Midi-Pyrénées'),
        ('Nord-Pas-de-Calais', 'Nord-Pas-de-Calais'),
        ('Pays de la Loire', 'Pays de la Loire'),
        ('Picardie', 'Picardie'),
        ('Poitou-Charentes', 'Poitou-Charentes'),
        ('Provence-Alpes-Côte d\'Azur', 'Provence-Alpes-Côte d\'Azur'),
        ('Rhône-Alpes', 'Rhône-Alpes'),
        ('Mayotte', 'Mayotte'),
        ('Martinique', 'Martinique'),
        ('Guadeloupe', 'Guadeloupe'),
        ('Reunion', 'Reunion'),
        ('Guyane', 'Guyane'),
        ('etranger', 'etranger'),
    )
    locations = models.CharField(max_length=255, choices=LOCATIONS_CHOICES, default=None, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, blank=True)