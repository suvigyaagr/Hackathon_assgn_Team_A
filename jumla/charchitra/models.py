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


class Video(models.Model):
    v_name = models.CharField(max_length=100)
    a_id = models.ManyToManyField(Actor)
    g_id = models.ManyToManyField(Genre)
    language = models.CharField(max_length=20)
    url = models.URLField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.v_name}'


class VideoPrice(models.Model):
    v_id = models.ForeignKey(Video)
    dur_id = models.ForeignKey(Duration)
    v_price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__ (self):
        return f'{self.v_id} -> {self.v_price}'

class VideoPackPrice(models.Model):
    a_id = models.ForeignKey(Actor)
    g_id = models.ForeignKey(Genre)
    duration = models.ForeignKey(Duration)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Subscribe(models.Model):
    u_id = models.ForeignKey('login.User')
    is_pack = models.NullBooleanField(default=False)
    v_id = models.ForeignKey(Video)
    p_id = models.ForeignKey(VideoPackPrice)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.ForeignKey(Duration)
    subscription_time = models.DateTimeField('date published')
