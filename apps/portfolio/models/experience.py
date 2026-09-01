from django.db import models


class Experience(models.Model):
    EMPLOYMENT_TYPES = [
        ("internship", "Internship"),
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("freelance", "Freelance"),
        ("contract", "Contract"),
        ("volunteer", "Volunteer"),
    ]

    company = models.CharField(max_length=200)
    position = models.CharField(max_length=150)

    employment_type = models.CharField(
        max_length=30,
        choices=EMPLOYMENT_TYPES,
        default="full_time",
    )

    location = models.CharField(
        max_length=150,
        blank=True,
    )

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True,
    )

    is_current = models.BooleanField(default=False)

    description = models.TextField()

    company_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-start_date"]

    def __str__(self):
        return f"{self.position} at {self.company}"