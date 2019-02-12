from django.db import models

# Create your models here.
class User(models.Model):
	u_id = models.CharField(max_length=40)
	u_pass = models.CharField(max_length=40)

	def __str__(self):
		return f'{self.u_id}'