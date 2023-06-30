# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AdvanceRequest(Document):
	
	@frappe.whitelist()
	def fetch_amount(self):
		doc = frappe.get_all('Season Wise Advance Item', filters={'season': self.season,'plant':self.plant,'vehicle_type':self.vehicle_type,'gang_type':self.gang_type},fields=["name", "advance","gang_type","vehicle_type","plant","season"])
		for s in doc:
			self.amount_limit = s.advance
		
	# @frappe.whitelist()
	# def paid_amount(self):
		# total=0.0
		# doc=frappe.db.get_list('Advance Request', filters={'contractor_name': self.contractor_name},fields={'name','paid_amount_till_today'})
		# for d in doc:
		# 	doc1=frappe.get_doc('Advance Request',d.name)
		# 	total=total+doc1.paid_amount_till_today
		# self.paid_amount_till_today=total
		# frappe.msgprint(str(total))
  
	@frappe.whitelist()
	def before_save(self):
		if self.amount_limit < self.amount_to_be_paid+self.paid_amount_till_today:
			frappe.throw("Exceeding the Limit ......")
      
      
      
	# 		self.limit_amount = s.advance
	# 	total=0.0
	# 	doc=frappe.db.get_list('Advance Request', filters={'contractor_name': self.contractor_name},fields={'name','advance_amount'})
	# 	for d in doc:
	# 		doc1=frappe.get_doc('Advance Request',d.name)
	# 		total=total+doc1.advance_amount
	# 	self.paid_amount=total
  
  
	# def before_save(self):
	# 	if self.limit_amount < self.advance_amount+self.paid_amount:
	# 		frappe.throw("Exceeding the Limit ......")
		
