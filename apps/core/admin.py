from django.contrib import admin
from django.utils.html import format_html

from apps.portfolio.admin_site import portfolio_admin_site

from .models import Profile, SocialLink


# =========================================================
# CUSTOM ADMIN REGISTRATION
# =========================================================

def portfolio_register(model):

    def decorator(admin_class):

        portfolio_admin_site.register(
            model,
            admin_class,
        )

        return admin_class

    return decorator


# =========================================================
# PROFILE
# =========================================================

@portfolio_register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    save_on_top = True

    list_display = (
        "profile_preview",
        "name",
        "title",
        "email",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "title",
        "tagline",
        "email",
        "phone",
        "location",
    )

    readonly_fields = (
        "profile_image_preview",
        "created_at",
        "updated_at",
    )

    class Media:
        css = {
        "all": ("admin/css/custom_admin.css",)
        }

    fieldsets = (

        # =================================================
        # PERSONAL INFORMATION
        # =================================================

        (
            "Personal Information",
            {
                "fields": (
                    "name",
                    "title",
                    "tagline",
                    "email",
                    "phone",
                    "location",
                )
            },
        ),

        # =================================================
        # ABOUT
        # =================================================

        (
            "About",
            {
                "fields": (
                    "bio",
                )
            },
        ),

        # =================================================
        # PROFILE IMAGE
        # =================================================

        (
            "Profile Image",
            {
                "fields": (
                    "profile_image",
                    "profile_image_preview",
                )
            },
        ),

        # =================================================
        # RESUME
        # =================================================

        (
            "Resume",
            {
                "fields": (
                    "resume",
                )
            },
        ),

        # =================================================
        # STATUS
        # =================================================

        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),

        # =================================================
        # SYSTEM INFORMATION
        # =================================================

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    ordering = (
        "name",
    )

    list_per_page = 20


    # =====================================================
    # PROFILE IMAGE — LIST
    # =====================================================

    @admin.display(
        description="Photo",
    )
    def profile_preview(self, obj):

        if not obj.profile_image:
            return "—"

        return format_html(
            '<img src="{}" '
            'style="width:55px;'
            'height:55px;'
            'object-fit:cover;'
            'border-radius:50%;'
            'border:1px solid #ddd;">',
            obj.profile_image.url,
        )


    # =====================================================
    # PROFILE IMAGE — EDIT
    # =====================================================

    @admin.display(
        description="Current Profile Image",
    )
    def profile_image_preview(self, obj):

        if not obj.profile_image:
            return "No profile image uploaded."

        return format_html(
            '<img src="{}" '
            'style="width:180px;'
            'height:180px;'
            'object-fit:cover;'
            'border-radius:50%;'
            'border:1px solid #ddd;">',
            obj.profile_image.url,
        )

    def has_add_permission(self, request):
        return not Profile.objects.exists()


# =========================================================
# SOCIAL LINKS
# =========================================================

@portfolio_register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):

    list_display = (
        "platform_display",
        "profile",
        "url",
        "is_visible",
        "order",
    )

    list_filter = (
        "platform",
        "is_visible",
        "profile",
    )

    search_fields = (
        "platform",
        "profile__name",
        "url",
    )

    ordering = (
        "order",
        "platform",
    )

    list_per_page = 25

    fieldsets = (

        # =================================================
        # SOCIAL PLATFORM
        # =================================================

        (
            "Social Platform",
            {
                "fields": (
                    "profile",
                    "platform",
                    "url",
                )
            },
        ),

        # =================================================
        # DISPLAY
        # =================================================

        (
            "Display Settings",
            {
                "fields": (
                    "icon",
                    "is_visible",
                    "order",
                )
            },
        ),
    )


    # =====================================================
    # PLATFORM DISPLAY
    # =====================================================

    @admin.display(
        description="Platform",
    )
    def platform_display(self, obj):

        return format_html(
            "<strong>{}</strong>",
            obj.platform.title(),
        )


    # =====================================================
    # NORMALIZE PLATFORM
    # =====================================================

    def save_model(
        self,
        request,
        obj,
        form,
        change,
    ):

        obj.platform = (
            obj.platform.strip().lower()
        )

        super().save_model(
            request,
            obj,
            form,
            change,
        )