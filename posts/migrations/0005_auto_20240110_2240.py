# Generated by Django 3.2.23 on 2024-01-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('rock', 'Rock'), ('metal', 'Metal'), ('pop', 'Pop'), ('country', 'Country'), ('jazz', 'Jazz'), ('folk', 'Folk'), ('electronic_dance_music', 'Electronic Dance Music'), ('r&b', 'R&B'), ('classical', 'Classical'), ('other', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='instrument',
            field=models.CharField(choices=[('vocalist_wanted', 'Vocalist wanted'), ('vocalist_here', 'Vocalist here'), ('guitarist_wanted', 'Guitarist wanted'), ('guitarist_here', 'Guitarist here'), ('bassist_wanted', 'Bassist wanted'), ('bassist_here', 'Bassist here'), ('keyboardist_wanted', 'Keyboardist wanted'), ('keyboardist_here', 'Keyboardist here'), ('drummer_wanted', 'Drummer wanted'), ('drummer_here', 'Drummer here'), ('other', 'Other')], max_length=30),
        ),
    ]
