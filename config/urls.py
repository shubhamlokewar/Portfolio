from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from apps.portfolio.admin_site import portfolio_admin_site


urlpatterns = [
    path(
        "admin/",
        portfolio_admin_site.urls,
    ),

    path(
        "",
        include("apps.core.urls"),
    ),

    path(
        "contact/",
        include("apps.contact.urls"),
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )