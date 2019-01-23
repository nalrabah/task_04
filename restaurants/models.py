from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=120)
	description = models.CharField(max_length=120)
	opening_time = models.TimeField(auto_now=False)
	closing_time = models.TimeField(auto_now=False)

	def __str__(self):
		return self.name