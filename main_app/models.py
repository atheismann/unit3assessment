from django.db import models

# Create your models here.
class Wish(models.Model):
  description = models.CharField(max_length=250)
  quantity = models.IntegerField()