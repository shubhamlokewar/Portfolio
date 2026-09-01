from django.contrib import admin
from django.utils.html import format_html

from .admin_site import portfolio_admin_site

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


# =========================================================
# CUSTOM ADMIN REGISTRATION
# =========================================================

def portfolio_register(model):
    """
    Register a ModelAdmin with the custom Portfolio AdminSite.
    """

    def decorator(admin_class):
        portfolio_admin_site.register(
            model,
            admin_class,
        )

        return admin_class

    return decorator


# =========================================================
# SKILLS
# =========================================================

@portfolio_register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "name",
        "category",
    )

    ordering = (
        "category",
        "name",
    )

    list_per_page = 25


# =========================================================
# TECHNOLOGIES
# =========================================================

@portfolio_register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "name",
        "category",
    )

    ordering = (
        "category",
        "name",
    )

    list_per_page = 25


# =========================================================
# PROJECTS
# =========================================================

@portfolio_register(Project)
class ProjectAdmin(admin.ModelAdmin):

    save_on_top = True

    list_display = (
        "project_thumbnail",
        "title",
        "publication_status",
        "featured_status",
        "order",
        "updated_at",
    )

    list_filter = (
        "is_published",
        "is_featured",
        "technologies",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    filter_horizontal = (
        "technologies",
    )

    readonly_fields = (
        "project_image_preview",
        "created_at",
        "updated_at",
    )

    ordering = (
        "order",
        "-created_at",
    )

    list_per_page = 20

    fieldsets = (
        (
            "Project Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "short_description",
                    "description",
                ),
            },
        ),

        (
            "Project Images",
            {
                "fields": (
                    "thumbnail",
                    "featured_image",
                    "project_image_preview",
                ),
            },
        ),

        (
            "Technologies",
            {
                "fields": (
                    "technologies",
                ),
            },
        ),

        (
            "Project Links",
            {
                "fields": (
                    "github_url",
                    "live_url",
                ),
            },
        ),

        (
            "Timeline",
            {
                "fields": (
                    "start_date",
                    "end_date",
                ),
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "is_published",
                    "is_featured",
                    "order",
                ),
            },
        ),

        (
            "System Information",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    @admin.display(
        description="Preview",
    )
    def project_thumbnail(self, obj):

        image = obj.thumbnail or obj.featured_image

        if not image:
            return "—"

        return format_html(
            '<img src="{}" '
            'style="width:64px;'
            'height:45px;'
            'object-fit:cover;'
            'border-radius:7px;">',
            image.url,
        )

    @admin.display(
        description="Status",
        ordering="is_published",
    )
    def publication_status(self, obj):

        if obj.is_published:

            return format_html(
                '<span class="admin-status '
                'admin-status-success">{}</span>',
                "Published",
            )

        return format_html(
            '<span class="admin-status '
            'admin-status-muted">{}</span>',
            "Draft",
        )

    @admin.display(
        description="Featured",
        boolean=True,
    )
    def featured_status(self, obj):

        return obj.is_featured

    @admin.display(
        description="Image Preview",
    )
    def project_image_preview(self, obj):

        if not obj.thumbnail and not obj.featured_image:
            return "No project images uploaded."

        html = '<div class="project-admin-previews">'

        if obj.thumbnail:
            html += (
                '<div class="project-admin-preview-item">'
                '<span>Thumbnail</span>'
                f'<img src="{obj.thumbnail.url}">'
                '</div>'
            )

        if obj.featured_image:
            html += (
                '<div class="project-admin-preview-item">'
                '<span>Featured Image</span>'
                f'<img src="{obj.featured_image.url}">'
                '</div>'
            )

        html += "</div>"

        return format_html(html)


# =========================================================
# EXPERIENCE
# =========================================================

@portfolio_register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "position",
        "company",
        "employment_type",
        "start_date",
        "end_date",
        "current_status",
        "order",
    )

    list_filter = (
        "employment_type",
        "is_current",
        "company",
    )

    search_fields = (
        "position",
        "company",
        "description",
    )

    ordering = (
        "order",
        "-start_date",
    )

    list_per_page = 20

    fieldsets = (
        (
            "Job Information",
            {
                "fields": (
                    "position",
                    "company",
                    "employment_type",
                ),
            },
        ),

        (
            "Responsibilities",
            {
                "fields": (
                    "description",
                ),
            },
        ),

        (
            "Employment Period",
            {
                "fields": (
                    "start_date",
                    "end_date",
                    "is_current",
                ),
            },
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "order",
                ),
            },
        ),
    )

    @admin.display(
        description="Status",
        boolean=True,
    )
    def current_status(self, obj):
        return obj.is_current


# =========================================================
# EDUCATION
# =========================================================

@portfolio_register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = (
        "degree",
        "institution",
        "field_of_study",
        "start_date",
        "end_date",
        "grade",
        "order",
    )

    list_filter = (
        "institution",
        "field_of_study",
    )

    search_fields = (
        "degree",
        "institution",
        "field_of_study",
        "grade",
        "description",
    )

    ordering = (
        "order",
        "-start_date",
    )

    list_per_page = 20

    fieldsets = (
        (
            "Education Details",
            {
                "fields": (
                    "degree",
                    "institution",
                    "field_of_study",
                    "grade",
                ),
            },
        ),

        (
            "Study Period",
            {
                "fields": (
                    "start_date",
                    "end_date",
                ),
            },
        ),

        (
            "Description",
            {
                "fields": (
                    "description",
                ),
            },
        ),

        (
            "Institution Link",
            {
                "fields": (
                    "institution_url",
                ),
            },
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "order",
                ),
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


# =========================================================
# CERTIFICATES
# =========================================================

@portfolio_register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "issuing_organization",
        "issue_date",
        "expiration_date",
        "credential_id",
        "order",
    )

    list_filter = (
        "issuing_organization",
    )

    search_fields = (
        "title",
        "issuing_organization",
        "credential_id",
    )

    ordering = (
        "order",
        "-issue_date",
    )

    list_per_page = 20


# =========================================================
# ACHIEVEMENTS
# =========================================================

@portfolio_register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    list_display = (
        "thumbnail_preview",
        "title",
        "organization",
        "date",
        "order",
    )

    list_filter = (
        "organization",
        "date",
    )

    search_fields = (
        "title",
        "organization",
        "description",
    )

    ordering = (
        "order",
        "-date",
    )

    list_per_page = 20

    fieldsets = (
        (
            "Achievement Details",
            {
                "fields": (
                    "title",
                    "organization",
                    "date",
                    "description",
                ),
            },
        ),

        (
            "Achievement Image",
            {
                "fields": (
                    "image",
                    "image_preview",
                ),
            },
        ),

        (
            "External Link",
            {
                "fields": (
                    "url",
                ),
            },
        ),

        (
            "Display Settings",
            {
                "fields": (
                    "order",
                ),
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    readonly_fields = (
        "image_preview",
        "created_at",
        "updated_at",
    )

    @admin.display(description="Image")
    def thumbnail_preview(self, obj):

        if not obj.image:
            return "—"

        return format_html(
            '<img src="{}" '
            'style="width:80px;'
            'height:55px;'
            'object-fit:cover;'
            'border-radius:7px;">',
            obj.image.url,
        )

    @admin.display(description="Current Image")
    def image_preview(self, obj):

        if not obj.image:
            return "No image uploaded."

        return format_html(
            '<img src="{}" '
            'style="max-width:400px;'
            'max-height:300px;'
            'object-fit:contain;'
            'border-radius:10px;'
            'border:1px solid #e5e7eb;'
            'padding:5px;">',
            obj.image.url,
        )


# =========================================================
# GALLERY
# =========================================================

@portfolio_register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    save_on_top = True

    list_display = (
        "thumbnail_preview",
        "title",
        "category",
        "featured_status",
        "order",
        "created_at",
    )

    list_filter = (
        "category",
        "is_featured",
    )

    search_fields = (
        "title",
        "caption",
        "category",
    )

    ordering = (
        "order",
        "-created_at",
    )

    readonly_fields = (
        "image_preview",
        "created_at",
        "updated_at",
    )

    list_per_page = 20

    fieldsets = (
        (
            "Image",
            {
                "fields": (
                    "image",
                    "image_preview",
                ),
            },
        ),

        (
            "Information",
            {
                "fields": (
                    "title",
                    "caption",
                    "category",
                ),
            },
        ),

        (
            "Display",
            {
                "fields": (
                    "is_featured",
                    "order",
                ),
            },
        ),

        (
            "System Information",
            {
                "classes": ("collapse",),
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )

    @admin.display(description="Image")
    def thumbnail_preview(self, obj):

        if not obj.image:
            return "—"

        return format_html(
            '<img src="{}" '
            'style="width:70px;'
            'height:50px;'
            'object-fit:cover;'
            'border-radius:7px;">',
            obj.image.url,
        )

    @admin.display(
        description="Featured",
        boolean=True,
    )
    def featured_status(self, obj):
        return obj.is_featured

    @admin.display(description="Preview")
    def image_preview(self, obj):

        if not obj.image:
            return "No image uploaded."

        return format_html(
            '<img src="{}" '
            'style="max-width:500px;'
            'max-height:350px;'
            'object-fit:contain;'
            'border-radius:10px;">',
            obj.image.url,
        )