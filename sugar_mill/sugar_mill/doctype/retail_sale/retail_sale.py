# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RetailSale(Document):
	@frappe.whitelist()    
	def fetch_shares(self):
			# doc1=frappe.db.get_list('Shareholder',filters={'name':self.party},fields={'name','from_shareholder','no_of_shares'})
			doc1=frappe.db.get_list('Shareholder',fields={'name'})
			for d in doc1:
				doc2=frappe.db.get_list('Share Transfer',filters={'to_shareholder':d.name},fields={'name','to_shareholder','no_of_shares'})
				for m in doc2:
					# frappe.msgprint(str(m.no_of_shares))
					self.no_of_shares = m.no_of_shares
     
	@frappe.whitelist()
	def fetch_qty(self):
		total = 0.0
		for i in self.items:
			total = i.per_share_qty * self.no_of_shares
			i.qty = total
   

