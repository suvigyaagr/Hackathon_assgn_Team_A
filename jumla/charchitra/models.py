from django.db import models


# Create your models here.
class Actor(models.Model):
    # a_id = models.CharField(max_length=40)
    a_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.a_id}'


# Create your models here.
class Genre(models.Model):
    # g_id = models.CharField(max_length=40)
    g_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.g_id}'


class Duration(models.Model):
    # dur_id = models.CharField(max_length=40)
    d_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.dur_id}'


class Video(models.Model):
    v_name = models.CharField(max_length=100)
    a_id = models.ManyToManyField(Actor)
    g_id = models.ManyToManyField(Genre)
    language = models.CharField(max_length=20)
    url = models.URLField(max_length=300)
    description = models.CharField(max_length=500)

    def __str_(self):
        return f'{self.v_name}'


class VideoPrice(models.Model):
    v_id = models.ForeignKey(Videos)
    dur_id = models.ForeignKey(Duration)
    v_price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__ (self):
        return f'{self.v_id} -> {self.v_price}'

