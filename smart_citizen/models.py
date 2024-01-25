from django.db import models


class SmartCitizen(models.Model):
    name_en = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    name_bn = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    father = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    mother = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    birthday = models.DateField(
        max_length=255,
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.name_en)
