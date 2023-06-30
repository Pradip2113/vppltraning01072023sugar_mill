# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.data import date_diff

class VehicleRegistration(Document):

    # pass
	@frappe.whitelist()
	def vivo(self):
		doc = frappe.get_all('Vehicle Registration', filters={'h_and_t_contract': self.h_and_t_contract}, fields={"total_numbers_of_vehicle","name"})
		# frappe.msgprint(str(s))
		for s in doc:
			# frappe.msgprint(str(s.total_numbers_of_vehicle))
			frappe.db.set_value("H and T Contract", self.h_and_t_contract, "total_vehicle",self.total_numbers_of_vehicle)
			frappe.db.set_value("H and T Contract", self.h_and_t_contract, "vehicle_type",self.vehicle_type)
			frappe.db.set_value("H and T Contract", self.h_and_t_contract, "transporter_code",self.transporter_code)
   
	# @frappe.whitelist()
	# def mgmg(self):
	# 	self.no_of_days = date_diff(self.submit_date, self.issue_date)
 
	# def __init__(self, submit_date, issue_date):
	# 	self.submit_date = submit_date
	# 	self.issue_date = issue_date

	# def calculate_days_between_dates(self):
	# 	new_date = self.submit_date + timedelta(days=1)
	# 	self.submit_date = new_date

	# 	self.no_of_days = (self.issue_date - self.submit_date).days
			
  