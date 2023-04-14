from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    # text to put at the end of each page's <title>.
    site_title = 'DJ Template '

    # text to put in each page's <h1> (and above login form).
    site_header = 'DJ Template Dashboard'

    # text to put at the top of the admin index page.
    index_title = 'DJ Template'


custom_admin_site = CustomAdminSite()
