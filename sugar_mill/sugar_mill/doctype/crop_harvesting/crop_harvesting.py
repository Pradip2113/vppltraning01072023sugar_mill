# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CropHarvesting(Document):
	# pass
	def on_trash(self):
			# doc = frappe.db.get_list("Cane Master")  #fields=["plantation_status", "name","form_number"
			# for a in doc:
				# frappe.msgprint(self.crop_sample_id)
				if self.crop_sample_id !="Without Sampling":
					frappe.db.set_value("Crop Sampling", self.crop_sample_id ,"plantation_status", "To Sampling")
					frappe.db.set_value("Cane Master", self.id ,"plantation_status", "To Sampling")
				else:
					frappe.db.set_value("Cane Master", self.id ,"plantation_status", "New")
                
				# eachdoc= frappe.get_doc("Cane Master",a.name)
				# if self.id == eachdoc.name:
				# 	eachdoc.plantation_status="New"
				# 	eachdoc.save()
				# 	break

