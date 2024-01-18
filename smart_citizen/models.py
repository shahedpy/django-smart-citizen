from django.db import models


class SmartCitizen(models.Model):
    name = models.CharField()
    father = models.CharField()
    mother = models.CharField()
    birthday = models.CharField()

    def __str__(self):
        return str(self.name)
