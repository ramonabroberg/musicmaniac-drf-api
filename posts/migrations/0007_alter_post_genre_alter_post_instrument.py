# Generated by Django 4.2.13 on 2024-05-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20240111_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('Select_genre', 'Select genre...'), ('Blues', 'Blues'), ('Classical', 'Classical'), ('Country', 'Country'), ('Electronic_dance_music', 'Electronic Dance Music'), ('Folk', 'Folk'), ('Jazz', 'Jazz'), ('Metal', 'Metal'), ('Pop', 'Pop'), ('R&B', 'R&B'), ('Rock', 'Rock'), ('Soul', 'Soul'), ('Other', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='instrument',
            field=models.CharField(choices=[('Select_instrument', 'Select instrument...'), ('Bassist_here', 'Bassist here'), ('Bassist_wanted', 'Bassist wanted'), ('Drummer_here', 'Drummer here'), ('Drummer_wanted', 'Drummer wanted'), ('Guitarist_here', 'Guitarist here'), ('Guitarist_wanted', 'Guitarist wanted'), ('Keyboardist_here', 'Keyboardist/pianist here'), ('Keyboardist_wanted', 'Keyboardist/pianist wanted'), ('Vocalist_here', 'Vocalist here'), ('Vocalist_wanted', 'Vocalist wanted'), ('Other', 'Other')], max_length=30),
        ),
    ]