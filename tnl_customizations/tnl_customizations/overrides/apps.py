import frappe
from frappe.apps import get_apps as original_get_apps

APP_REBRANDING = {
    "raven": {
        "title": "Discussion",
        "logo": "/assets/tnl_customizations/images/discussion-logo.png",
    },
    "hrms": {
        "title": "People",
        "logo": "/assets/tnl_customizations/images/people-logo.svg",
    },
}


@frappe.whitelist()
def get_apps():
    apps = original_get_apps()

    for app in apps:
        branding = APP_REBRANDING.get(app["name"])
        if branding:
            app.update(branding)

    return apps