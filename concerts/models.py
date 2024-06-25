from django.db import models

# Create your models here.

class Concert(models.Model):
  city = models.CharField( max_length=60)
  date = models.DateField()
  price = models.IntegerField( null=True)
  
  def __str__(self):
    return self.city
