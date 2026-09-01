from django.db import models


class Achievement(models.Model):
    title = models.CharField(max_length=200)

    organization = models.CharField(
        max_length=200,
        blank=True,
    )

    date = models.DateField(
        blank=True,
        null=True,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="achievements/",
        blank=True,
        null=True,
    )

    url = models.URLField(blank=True)

    order = models.PositiveIntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["order", "-date"]

    def __str__(self):
        return self.title