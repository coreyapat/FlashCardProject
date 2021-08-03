from django.db import models


# Create your models here.

class CollectionPoint(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FlashCards(models.Model):
    front = models.TextField(max_length=200)
    back = models.TextField(max_length=200)
    card = models.ForeignKey(CollectionPoint, on_delete=models.CASCADE)

    def __str__(self):
        return self.card
