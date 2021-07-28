from django.db import models


# Create your models here.

class CollectionPoint(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class FlashCards(models.Model):
    cardId = models.ForeignKey(CollectionPoint, on_delete=models.CASCADE)
    front = models.CharField(max_length=100)
    back = models.CharField(max_length=100)

    def __str__(self):
        return self.cardId
