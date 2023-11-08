from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=60, validators=[MinLengthValidator(3)])
    rating = models.PositiveIntegerField()
    feedback = models.TextField()

    def get_url(self):
        return reverse('feedback-detail', args=[self.id])
