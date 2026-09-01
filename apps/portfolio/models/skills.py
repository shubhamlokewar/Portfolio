from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=100,
        blank=True,
    )

    order = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.name

class Skill(models.Model):

    name = models.CharField(
        max_length=100,
    )

    category = models.CharField(
        max_length=100,
        blank=True,
    )

    class Meta:
        ordering = [
            "category",
            "name",
        ]

    def __str__(self):
        return self.name    