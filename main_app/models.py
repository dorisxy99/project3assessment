from django.db import models
from django.urls import reverse

# Create your models here.
class WishItem(models.Model):
    item = models.CharField(max_length=100)
