# Generated by Django 3.2.16 on 2023-02-06 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voiture',
            name='year',
        ),
    ]