# Generated by Django 4.0.6 on 2022-07-29 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_modelfilm_delete_modelperson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelfilm',
            old_name='english',
            new_name='seen_or_not',
        ),
        migrations.RemoveField(
            model_name='modelfilm',
            name='land_production',
        ),
        migrations.AddField(
            model_name='modelfilm',
            name='genre',
            field=models.CharField(choices=[('H', 'Horreur'), ('SF', 'Science Fiction'), ('C', 'Comedie'), ('D', 'Drame'), ('A', 'Aventure'), ('M', 'Manga'), ('TH', 'Thriller'), ('Doc', 'Documentaire')], default='Horreur', max_length=25),
            preserve_default=False,
        ),
    ]