# Generated by Django 3.2.23 on 2023-12-30 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='band',
        ),
    ]
