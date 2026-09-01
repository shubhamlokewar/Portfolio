from django.contrib import admin

from apps.portfolio.admin_site import portfolio_admin_site

from .models import ContactMessage


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
# CONTACT MESSAGES
# =========================================================

@portfolio_register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "message_preview",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
        "message",
    )

    list_filter = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "name",
        "email",
        "subject",
        "message",
        "created_at",
    )

    list_per_page = 25

    fieldsets = (
        (
            "Sender",
            {
                "fields": (
                    "name",
                    "email",
                ),
            },
        ),

        (
            "Message",
            {
                "fields": (
                    "subject",
                    "message",
                ),
            },
        ),

        (
            "Received",
            {
                "fields": (
                    "created_at",
                ),
            },
        ),
    )

    @admin.display(
        description="Message",
    )
    def message_preview(self, obj):

        if not obj.message:
            return "—"

        text = obj.message.strip()

        if len(text) > 70:
            text = text[:70] + "..."

        return text