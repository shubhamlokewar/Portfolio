from django.db import models

from .profile import Profile


class SocialLink(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="social_links",
    )

    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=100, blank=True)

    is_visible = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.profile.name} - {self.platform}"