# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import string    
import random


class CaneInwardSlip(Document):
		
	# def before_save(self):
	# 	ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))  
	# 	self.uin='N-'+ran
	# 	self.name=self.uin

	# @frappe.whitelist()
	# def cn(self):
	# 	# eachdoc = frappe.get_doc("Vehicle Registration", self.transporter_code)
	# 	doc = frappe.get_all('Vehicle Registration item', filters={'driver_name':self.transporter_code}, fields={"cart_no","name"})
	# 	for d in doc:
	# 		self.cartno=d.cart_no
	# 		break

	@frappe.whitelist()
	def vivo(self):
		doc = frappe.get_all('H and T Contract', filters={'name': self.transporter_code}, fields={'name','vehicle_no','transporter_code','harvester_code','transporter_name','harvester_name','trolly_1','trolly_2','total_vehicle','vehicle_type'})
		for s in doc:
			self.transporter_name = s.transporter_name
			self.harvester_code = s.harvester_code
			self.harvester_name = s.harvester_name
			self.vehicle_type = s.vehicle_type
			self.vehicle_number = s.vehicle_no
			self.tolly_1 = s.trolly_1
			self.tolly_2 = s.trolly_2
   
	@frappe.whitelist()
	def slip_number(self):
		self.slip_no = self.get_new_slip_number()
	@frappe.whitelist()
	def get_new_slip_number(self):
		last_slip = frappe.db.get_value('Cane Inward Slip', filters={}, fieldname='slip_no', order_by='creation desc')
		if last_slip:
			new_slip = int(last_slip) + 1
		else:
			new_slip = 1
		return str(new_slip)

		# last_slip = frappe.db.get_value('Cane Inward Slip', filters={'shift': self.shift}, fieldname='slip_no', order_by='creation desc')
		# if last_slip:
		# 	new_slip = int(last_slip.split('-')[1]) + 1
		# else:
		# 	new_slip = 1
		# return self.shift + '-' + str(new_slip)



			
				

