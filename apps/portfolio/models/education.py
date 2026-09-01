from django.core.validators import MinValueValidator
from django.db import models


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    field_of_study = models.CharField(max_length=150, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(
        blank=True,
        null=True,
    )

    grade = models.CharField(
        max_length=50,
        blank=True,
    )

    description = models.TextField(blank=True)

    institution_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)],
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.degree} - {self.institution}"