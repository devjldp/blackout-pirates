from django.db import models

# Create your models here.

class Concerts(models.Model):
  city = models.CharField( max_length=60)
  date = models.DateField()
