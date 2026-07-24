import frappe
from frappe.apps import get_apps as original_get_apps


@frappe.whitelist()
def get_apps():
    return original_get_apps()
