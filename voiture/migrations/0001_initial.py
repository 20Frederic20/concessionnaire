# Generated by Django 3.2.16 on 2023-02-06 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('image', models.FileField(upload_to='media/uploads/')),
                ('marque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voiture.marque')),
            ],
        ),
    ]
