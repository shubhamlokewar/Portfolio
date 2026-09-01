from django.db import models


class Certificate(models.Model):
    title = models.CharField(max_length=200)

    issuing_organization = models.CharField(
        max_length=200,
    )

    issue_date = models.DateField(
        blank=True,
        null=True,
    )

    expiration_date = models.DateField(
        blank=True,
        null=True,
    )

    credential_id = models.CharField(
        max_length=150,
        blank=True,
    )

    credential_url = models.URLField(
        blank=True,
    )

    certificate_image = models.ImageField(
        upload_to="certificates/",
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
    )

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
        ordering = ["order", "-issue_date"]

    def __str__(self):
        return self.title