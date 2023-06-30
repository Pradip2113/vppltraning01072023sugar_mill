# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HandTContract(Document):
	@frappe.whitelist()
	def on_submit(self):
#   ----------------------------------------------------------------------------------------
		moc = frappe.new_doc("Vehicle Registration")
		moc.h_and_t_contract = self.name
		moc.vehicle_number = self.vehicle_no
		moc.contractor_name = self.h_and_t_group
		moc.vehicle_type = self.vehicle_type
		moc.total_numbers_of_vehicle = self.total_vehicle
		moc.transporter_code = self.transporter_code
		moc.season = self.season
		moc.trolly__1 = self.trolly_1
		moc.trolly_2 = self.trolly_2
		for i in range(int(self.total_vehicle)):
			vehicle_detail = moc.append("vehicle_details_tab", {})
			vehicle_detail.trolly_1 = self.trolly_1
			vehicle_detail.trolly_2 = self.trolly_2
			vehicle_detail.driver_name = self.transporter_code
		moc.save()

#  -------------------------------------------------------------------------------------------
	@frappe.whitelist()
	def on_update_after_submit(self):
		frappe.db.set_value("Vehicle Registration", str(self.season)+"-"+str(self.name), "contractor_name",self.h_and_t_group)
		frappe.db.set_value("Vehicle Registration",str(self.season)+"-"+str(self.name), "transporter_code",self.transporter_code)
		frappe.db.set_value("Vehicle Registration",str(self.season)+"-"+str(self.name), "vehicle_number",self.vehicle_no)
		# frappe.db.set_value("Vehicle Registration",str(self.season)+"-"+str(self.name), "contractor_name",self.harvester_code)
		frappe.db.set_value("Vehicle Registration",str(self.season)+"-"+str(self.name), "vehicle_type",self.vehicle_type)
		frappe.db.set_value("Vehicle Registration",str(self.season)+"-"+str(self.name), "total_numbers_of_vehicle",self.total_vehicle)
		frappe.db.set_value("Vehicle Registration",str(self.season)+"-"+str(self.name), "transporter_code",self.transporter_code)
		frappe.db.set_value("Vehicle Registration",str(self.season)+"-"+str(self.name), "season",self.season)
		self.changing_the_no_of_chart_after_updating()
	# @frappe.whitelist()
	# def eeeuu(self):
	# 	chil = frappe.get_all("Vehicle Registration item", fields=["name","cart_no"])
	# 	for m in chil:
	# 		frappe.db.set_value("Vehicle Registration item", m.name, "cart_no",m.name)
   
	@frappe.whitelist()
	def changing_the_no_of_chart_after_updating(self):
		doc = frappe.get_all('Vehicle Registration item', filters={'parent': str(self.season) + "-" + str(self.name)}, fields=["name", "idx"], order_by="name DESC")
		no_doc_remove =len(doc)-int(self.total_vehicle)
		no_doc_insert = int(self.total_vehicle) - len(doc)
		if no_doc_remove>0:
			moc = frappe.get_all('Vehicle Registration item', filters={'parent': str(self.season) + "-" + str(self.name)}, fields=["name", "idx"], order_by="name DESC", limit=no_doc_remove)
			for m in moc:
				frappe.delete_doc('Vehicle Registration item', m.name)

		if no_doc_insert>0:
			for i in range(int(no_doc_insert)):
				new_doc = frappe.new_doc('Vehicle Registration item')
				new_doc.parent = str(self.season) + "-" + str(self.name)
				new_doc.parentfield = "vehicle_details_tab"
				new_doc.parenttype = "Vehicle Registration"
				new_doc.idx = len(doc)+i+1
				new_doc.insert(ignore_permissions=True)


			
		
    
 


