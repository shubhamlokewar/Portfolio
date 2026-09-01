from django.contrib.admin import AdminSite


class PortfolioAdminSite(AdminSite):
    """
    Custom administration site for the portfolio CMS.
    """

    site_header = "shubhamlokewar."
    site_title = "Portfolio Admin"
    index_title = "Portfolio Dashboard"

    index_template = "admin/index.html"

    def each_context(self, request):
        context = super().each_context(request)

        from .models import (
            Achievement,
            Certificate,
            Education,
            Experience,
            GalleryImage,
            Project,
            Skill,
            Technology,
        )

        context.update(
            {
                "admin_project_count": Project.objects.count(),
                "admin_skill_count": Skill.objects.count(),
                "admin_technology_count": Technology.objects.count(),
                "admin_experience_count": Experience.objects.count(),
                "admin_education_count": Education.objects.count(),
                "admin_certificate_count": Certificate.objects.count(),
                "admin_achievement_count": Achievement.objects.count(),
                "admin_gallery_count": GalleryImage.objects.count(),
            }
        )

        return context


portfolio_admin_site = PortfolioAdminSite(
    name="portfolio_admin"
)