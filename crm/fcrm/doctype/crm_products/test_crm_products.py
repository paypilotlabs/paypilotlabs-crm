import unittest


class TestProductDetailsScript(unittest.TestCase):
	def test_product_change_replaces_existing_rate(self):
		from crm.fcrm.doctype.crm_products.crm_products import get_product_details_script

		script = get_product_details_script("CRM Deal")

		self.assertIn("row.rate = a.rate ?? 0", script)
		self.assertNotIn("!row.rate", script)
		self.assertIn("row.product_code !== productCode", script)
