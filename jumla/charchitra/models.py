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


class Duration(modes.Model):
	# dur_id = models.CharField(max_length=40)
	d_name = models.CharField(max_length=40)

	def __str__(self):
		return f'{self.dur_id}'


