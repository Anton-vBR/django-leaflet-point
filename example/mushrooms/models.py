from django.db import models

class MushroomSpot(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField()
    lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(
        max_digits=9, decimal_places=6, null=True)

    def __str__(self):
        return str(self.title)