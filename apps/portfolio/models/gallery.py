from django.db import models


class GalleryImage(models.Model):

    title = models.CharField(
        max_length=200,
        blank=True,
    )

    image = models.ImageField(
        upload_to="gallery/",
    )

    caption = models.TextField(
        blank=True,
    )

    category = models.CharField(
        max_length=100,
        blank=True,
    )

    is_featured = models.BooleanField(
        default=False,
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
        ordering = [
            "order",
            "-created_at",
        ]

    def __str__(self):
        return self.title or f"Gallery Image {self.pk}"