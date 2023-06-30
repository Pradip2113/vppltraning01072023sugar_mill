# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TestChild(Document):
	@frappe.whitelist()
	def vivek(self):
		# doc = frappe.db.get_list(
		# 		"Cane Master",
		# 		fields=[
		# 			"name",
		# 			"plantattion_ratooning_date",
		# 			"area",
		# 			"circle_office",
		# 			"crop_variety",
					
		# 		],
		# 	)
		# for d in doc:
		# 	frappe.db.set_value("Cane Master", d.name ,"plantation_status", "New")
		# 	frappe.msgprint(str(d.name)) #SI-23-24-00418
		# doc = frappe.db.get_list("Sales Invoice",fields=["name"],)
		BMC_CHILD = frappe.get_all("Sales Invoice Item", filters={"parent": "SI-23-24-00418"}, fields=["name", "item_code","item_name"])
		for d in BMC_CHILD:
			frappe.msgprint(d.item_name)

	@frappe.whitelist()
	def abhi(self):
		doc = frappe.db.get_list("Crop Sampling",fields=["name"],)
		for d in doc:
			frappe.db.set_value("Crop Sampling", d.name ,"plantation_status", "To Sampling")
   
