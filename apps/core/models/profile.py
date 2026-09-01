from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    tagline = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
    )

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=150, blank=True)

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name