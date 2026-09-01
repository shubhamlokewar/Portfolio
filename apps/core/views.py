from django.shortcuts import render

from apps.core.models import Profile

from apps.portfolio.models import (
    Achievement,
    Certificate,
    Education,
    Experience,
    GalleryImage,
    Project,
    Skill,
    Technology,
)


def home(request):

    profile = Profile.objects.filter(
        is_active=True
    ).first()

    educations = Education.objects.all()

    achievements = Achievement.objects.all()

    certificates = Certificate.objects.all()

    gallery_images = GalleryImage.objects.all()

    projects = Project.objects.filter(
        is_published=True
    )

    experiences = Experience.objects.all()
    skills = Skill.objects.all()

    technologies = Technology.objects.all()

    return render(
        request,
        "home.html",
        {
            "profile": profile,
            "educations": educations,
            "achievements": achievements,
            "certificates": certificates,
            "gallery_images": gallery_images,
            "projects": projects,
            "experiences": experiences,
            "skills": skills,
            "technologies": technologies,
        },
    )