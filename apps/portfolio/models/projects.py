from django.db import models

from .skills import Technology


class Project(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        unique=True,
    )

    short_description = models.CharField(
        max_length=300,
    )

    description = models.TextField()

    thumbnail = models.ImageField(
        upload_to="projects/thumbnails/",
        blank=True,
        null=True,
    )

    featured_image = models.ImageField(
        upload_to="projects/featured/",
        blank=True,
        null=True,
    )

    technologies = models.ManyToManyField(
        Technology,
        related_name="projects",
        blank=True,
    )

    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    start_date = models.DateField(
        blank=True,
        null=True,
    )

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]
        indexes = [
            models.Index(
                fields=["is_published", "is_featured"]
            ),
        ]

    def __str__(self):
        return self.title