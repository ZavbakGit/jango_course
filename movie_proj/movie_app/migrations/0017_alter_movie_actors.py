# Generated by Django 4.2.6 on 2023-11-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0016_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movie_app.actor'),
        ),
    ]