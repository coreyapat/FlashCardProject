from django.db import models

# Create your models here.
class FlashCards(models.Model):
    front = models.CharField(max_length=100)
    back = models.CharField(max_length=100)