from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class DressingRoom(models.Model):
    class Meta:
        verbose_name = "Гримерка"
        verbose_name_plural = "Гримерки"

    floor = models.IntegerField(validators=[MinValueValidator(1)])
    number = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.floor} {self.number}'


class Director(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    director_email = models.EmailField()

    def get_url(self):
        return reverse('director-detail', args=[self.id])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"

    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)
    dressing = models.OneToOneField(DressingRoom,on_delete=models.SET_NULL,null=True,blank=True)

    def get_url(self):
        return reverse('actor-detail', args=[self.id])

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актёр {self.first_name} {self.last_name}'
        else:
            return f'Актриса {self.first_name} {self.last_name}'


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True,
                                 validators=[MinValueValidator(1)])
    slug = models.SlugField(default='', null=False, db_index=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='RUB')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'name = {self.name}, rating = {self.rating}%, year ={self.year}, budget ={self.budget}'
