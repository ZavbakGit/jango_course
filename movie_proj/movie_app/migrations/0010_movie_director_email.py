# Generated by Django 4.2.6 on 2023-11-06 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_movie_director_alter_movie_budget_alter_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director_email',
            field=models.EmailField(default='sun_wait@mail.ru', max_length=254),
        ),
    ]