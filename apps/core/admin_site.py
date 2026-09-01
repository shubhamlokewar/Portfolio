from django.contrib.admin import AdminSite


class PortfolioAdminSite(AdminSite):

    site_header = "Shubham Lokewar"
    site_title = "Portfolio Admin"
    index_title = "Portfolio Management"
    site_url = "/"