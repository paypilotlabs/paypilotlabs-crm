import json
import os

import frappe

# Version-aware base test case: frappe v16 ships IntegrationTestCase ; v15 only
# has FrappeTestCase. Tests import CRMTestCase so the same suite runs on both.
try:
	from frappe.tests import IntegrationTestCase as CRMTestCase
except ImportError:
	from frappe.tests.utils import FrappeTestCase as CRMTestCase


def before_tests():
	skip_test_records_of_other_apps()
	load_crm_user_test_records()


def skip_test_records_of_other_apps():
	"""Stop test record generation from walking into DocTypes of apps other than frappe and crm."""
	own_modules = frappe.get_module_list("frappe") + frappe.get_module_list("crm")
	other_doctypes = frappe.get_all("DocType", filters={"module": ["not in", own_modules]}, pluck="name")
	for doctype in other_doctypes:
		frappe.local.test_objects.setdefault(doctype, [])


def load_crm_user_test_records():
	"""Load CRM user test records from crm/tests/test_records.json"""
	test_records_path = os.path.join(os.path.dirname(__file__), "test_records.json")

	if os.path.exists(test_records_path):
		with open(test_records_path) as f:
			test_records = json.load(f)

		for record in test_records:
			if not frappe.db.exists("User", record.get("email")):
				doc = frappe.get_doc(record)
				doc.insert(ignore_permissions=True, ignore_if_duplicate=True)
