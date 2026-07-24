app_name = "tnl_customizations"
app_title = "TNL Customizations"
app_publisher = "TNL"
app_description = "Client branding and customizations for TNL ERP"
app_email = "nihal@tnl.sa"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "tnl_customizations",
# 		"logo": "/assets/tnl_customizations/logo.png",
# 		"title": "TNL Customizations",
# 		"route": "/tnl_customizations",
# 		"has_permission": "tnl_customizations.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tnl_customizations/css/tnl_customizations.css"
# app_include_js = "/assets/tnl_customizations/js/tnl_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/tnl_customizations/css/tnl_customizations.css"
# web_include_js = "/assets/tnl_customizations/js/tnl_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tnl_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tnl_customizations/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tnl_customizations.utils.jinja_methods",
# 	"filters": "tnl_customizations.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tnl_customizations.install.before_install"
# after_install = "tnl_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tnl_customizations.uninstall.before_uninstall"
# after_uninstall = "tnl_customizations.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tnl_customizations.utils.before_app_install"
# after_app_install = "tnl_customizations.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tnl_customizations.utils.before_app_uninstall"
# after_app_uninstall = "tnl_customizations.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "tnl_customizations.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tnl_customizations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tnl_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"tnl_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"tnl_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tnl_customizations.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tnl_customizations.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tnl_customizations.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "tnl_customizations.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
    "frappe.apps.get_apps": "tnl_customizations.overrides.apps.get_apps"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tnl_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tnl_customizations.utils.before_request"]
# after_request = ["tnl_customizations.utils.after_request"]

# Job Events
# ----------
# before_job = ["tnl_customizations.utils.before_job"]
# after_job = ["tnl_customizations.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tnl_customizations.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

fixtures = [
    {
        "dt": "Desktop Icon",
        "filters": [
            ["name", "in", ["Raven", "Frappe HR"]]
        ]
    }
]
