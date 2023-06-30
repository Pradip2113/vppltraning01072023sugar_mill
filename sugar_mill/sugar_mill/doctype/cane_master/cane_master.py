# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CaneMaster(Document):
	def before_save(self):
		existing_cane_record = frappe.get_all('Cane Master', filters={'name': self.name})
		if len(existing_cane_record)==1:
			s = frappe.get_all('Crop Sampling', filters={'id': self.name}, fields={"plantation_status","name"})
			h = frappe.get_all('Crop Harvesting', filters={'id': self.name}, fields={"plantation_status","name"})
			for m in s:
				# frappe.msgprint(m.plantation_status)
				if m.plantation_status=="To Sampling" or m.plantation_status=="To Harvesting":
					frappe.db.set_value("Crop Sampling", m.name, "season",self.season)
					frappe.db.set_value("Crop Sampling", m.name, "plantation_status",self.plantation_status)
					frappe.db.set_value("Crop Sampling", m.name, "plant_name",self.plant_name)
					frappe.db.set_value("Crop Sampling", m.name, "form_number",self.form_number)
					# frappe.db.set_value("Crop Sampling", m.name, "grower_code",self.grower_code)
					frappe.db.set_value("Crop Sampling", m.name, "grower_name",self.grower_name)
					frappe.db.set_value("Crop Sampling", m.name, "mobile_no",self.mobile_no)
					frappe.db.set_value("Crop Sampling", m.name, "company_name",self.company_name)
					frappe.db.set_value("Crop Sampling", m.name, "is_kisan_card",self.is_kisan_card)
					frappe.db.set_value("Crop Sampling", m.name, "survey_number",self.survey_number)
					frappe.db.set_value("Crop Sampling", m.name, "area",self.area)
					frappe.db.set_value("Crop Sampling", m.name, "country",self.country)
					frappe.db.set_value("Crop Sampling", m.name, "circle_office",self.circle_office)
					frappe.db.set_value("Crop Sampling", m.name, "taluka",self.taluka)
					frappe.db.set_value("Crop Sampling", m.name, "district",self.district)
					frappe.db.set_value("Crop Sampling", m.name, "states",self.states)
					frappe.db.set_value("Crop Sampling", m.name, "route",self.route)
					frappe.db.set_value("Crop Sampling", m.name, "route_km",self.route_km)
					frappe.db.set_value("Crop Sampling", m.name, "crop_name",self.crop_name)
					frappe.db.set_value("Crop Sampling", m.name, "crop_type",self.crop_type)
					frappe.db.set_value("Crop Sampling", m.name, "crop_variety",self.crop_variety)
					frappe.db.set_value("Crop Sampling", m.name, "area_acrs",self.area_acrs)
					frappe.db.set_value("Crop Sampling", m.name, "plantattion_ratooning_date",self.plantattion_ratooning_date)
					frappe.db.set_value("Crop Sampling", m.name, "irrigation_source",self.irrigation_source)
					frappe.db.set_value("Crop Sampling", m.name, "irrigation_method",self.irrigation_method)
					frappe.db.set_value("Crop Sampling", m.name, "soil_type",self.soil_type)
					frappe.db.set_value("Crop Sampling", m.name, "seed_material",self.seed_material)
					frappe.db.set_value("Crop Sampling", m.name, "road_side",self.road_side)
					frappe.db.set_value("Crop Sampling", m.name, "supervisor_name",self.supervisor_name)
					frappe.db.set_value("Crop Sampling", m.name, "plantation_system",self.plantation_system)
			for n in h:
				if n.plantation_status=="To Harvesting":
					frappe.db.set_value("Crop Harvesting", n.name, "season",self.season)
					frappe.db.set_value("Crop Harvesting", n.name, "plantation_status",self.plantation_status)
					frappe.db.set_value("Crop Harvesting", n.name, "plant_name",self.plant_name)
					frappe.db.set_value("Crop Harvesting", n.name, "form_number",self.form_number)
					# frappe.db.set_value("Crop Harvesting", n.name, "grower_code",self.grower_code)
					frappe.db.set_value("Crop Harvesting", n.name, "grower_name",self.grower_name)
					frappe.db.set_value("Crop Harvesting", n.name, "mobile_no",self.mobile_no)
					frappe.db.set_value("Crop Harvesting", n.name, "company_name",self.company_name)
					frappe.db.set_value("Crop Harvesting", n.name, "is_kisan_card",self.is_kisan_card)
					frappe.db.set_value("Crop Harvesting", n.name, "survey_number",self.survey_number)
					frappe.db.set_value("Crop Harvesting", n.name, "area",self.area)
					frappe.db.set_value("Crop Harvesting", n.name, "country",self.country)
					frappe.db.set_value("Crop Harvesting", n.name, "circle_office",self.circle_office)
					frappe.db.set_value("Crop Harvesting", n.name, "taluka",self.taluka)
					frappe.db.set_value("Crop Harvesting", n.name, "district",self.district)
					frappe.db.set_value("Crop Harvesting", n.name, "states",self.states)
					frappe.db.set_value("Crop Harvesting", n.name, "route",self.route)
					frappe.db.set_value("Crop Harvesting", n.name, "route_km",self.route_km)
					frappe.db.set_value("Crop Harvesting", n.name, "crop_name",self.crop_name)
					frappe.db.set_value("Crop Harvesting", n.name, "crop_type",self.crop_type)
					frappe.db.set_value("Crop Harvesting", n.name, "crop_variety",self.crop_variety)
					frappe.db.set_value("Crop Harvesting", n.name, "area_acrs",self.area_acrs)
					frappe.db.set_value("Crop Harvesting", n.name, "plantattion_ratooning_date",self.plantattion_ratooning_date)
					frappe.db.set_value("Crop Harvesting", n.name, "irrigation_source",self.irrigation_source)
					frappe.db.set_value("Crop Harvesting", n.name, "irrigation_method",self.irrigation_method)
					frappe.db.set_value("Crop Harvesting", n.name, "soil_type",self.soil_type)
					frappe.db.set_value("Crop Harvesting", n.name, "seed_material",self.seed_material)
					frappe.db.set_value("Crop Harvesting", n.name, "road_side",self.road_side)
					frappe.db.set_value("Crop Harvesting", n.name, "supervisor_name",self.supervisor_name)
					frappe.db.set_value("Crop Harvesting", n.name, "plantation_system",self.plantation_system)
    
				
