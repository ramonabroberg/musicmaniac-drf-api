# Generated by Django 3.2.23 on 2023-12-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='name', max_length=255),
        ),
    ]