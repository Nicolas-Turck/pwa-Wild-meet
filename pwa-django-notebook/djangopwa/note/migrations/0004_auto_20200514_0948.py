# Generated by Django 2.2.7 on 2020-05-14 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20200509_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encounter',
            name='country',
        ),
        migrations.RemoveField(
            model_name='encounter',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='encounter',
            name='species',
        ),
        migrations.AddField(
            model_name='encounter',
            name='biotopes',
            field=models.CharField(blank=True, choices=[('foret', 'foret'), ('bois', 'bois'), ('clairiere', 'clairieres'), ('cultures', 'cultures'), ('parc urbain et jardin', 'parc urbain et jardin'), ('haies chemin bord de route', 'haies chemin bord de route'), ('terrain en friches terrain vagues', 'terrain en friches terrain vagues'), ('verger bosquets', 'verger bosquets'), ('falaise', 'falaise'), ('grotte', 'grotte'), ('point d eau', 'point d eau'), ('tourbieres ou marais ', 'tourbieres ou marais'), ('dune', 'dune'), ('bras de mer ', 'bras de mer'), ('estuaires', 'estuaires'), ('marais salées', 'marais salées'), ('cotes rocheuse falaises maritimes', 'cotes rocheuse falaises maritimes')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='encounter',
            name='relief',
            field=models.CharField(blank=True, choices=[('montagnes', 'montagnes'), ('plateaux, vallées', 'plateaux, vallées'), ('plaines', 'plaines')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='encounter',
            name='types',
            field=models.CharField(blank=True, choices=[('empreintes', 'empreintes'), ('déjection', 'déjection'), ('terrier', 'terrier'), ('pots', 'pots'), ('poils', 'poils'), ('plumes', 'plumes'), ('pelote de déjection', 'pelote de déjection'), ('reste de repas', 'reste de repas'), ('grattage au sol ', 'grattage aux sol'), ('marquage sur végétations', 'marquage sur végétations'), ('coulées', 'coulées'), ('couches', 'couches')], default=None, max_length=100),
        ),
    ]