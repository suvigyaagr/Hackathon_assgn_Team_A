from django.db import models


# Create your models here.
class Actor(models.Model):
    a_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f'{self.a_name}'


# Create your models here.
class Genre(models.Model):
    g_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f'{self.g_name}'


class Duration(models.Model):
    d_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f'{self.d_name}'


class Videos(models.Model):
    v_name = models.CharField(max_length=100)
    a_id = models.ManyToManyField(Actor)
    g_id = models.ManyToManyField(Genre)
    language = models.CharField(max_length=20)
    url = models.URLField(max_length=300)
    description = models.CharField(max_length=500)


