from django.db import models


# Create your models here.
class Actor(models.Model):
    actor_id = models.CharField(max_length=40)
    actor_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.actor_id}'


# Create your models here.
class Genre(models.Model):
    genre_id = models.CharField(max_length=40)
    genre_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.genre_id}'
