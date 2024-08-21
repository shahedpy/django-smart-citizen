from django.db import models


class SmartCitizen(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
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
    father = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    mother = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
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
