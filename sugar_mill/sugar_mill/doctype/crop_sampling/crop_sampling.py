# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CropSampling(Document):
    @frappe.whitelist()
    def before_save(self):
        
        if self.average_brix:
            if self.no_of_pairs==0:
                    frappe.throw("Please Enter No. Of Pairs")
            sam = frappe.get_doc("Cane Sampling Formula", "Cane Sampling Formula",fields=["from_brix", "from_pairs","to_brix","to_pairs"])
            minimum_brix=sam.minimum_brix
            minimum_pairs=sam.minimum_pairs
            
            existing_cropsampling = frappe.get_all('Crop Harvesting', filters={'crop_sample_id': self.name})
            # frappe.msgprint(str(existing_cropsampling))
            if len(existing_cropsampling)==0:
                
                if ((float(minimum_brix) <= float(self.average_brix) ) and (float(minimum_pairs)<= float(self.no_of_pairs)) and self.plantation_status == "To Sampling"):
                    doc=frappe.new_doc('Crop Harvesting')
                    doc.brix =self.average_brix
                    doc.crop_sample_id=self.name
                    doc.no_of_pairs=self.no_of_pairs
                    doc.id =self.id
                    
                    doc.average_brix = 0
                    doc.insert()
                    doc.save
                    moc = frappe.db.get_all("Crop Harvesting", fields=["name"], order_by="creation DESC", limit=1)
                    frappe.db.set_value("Crop Harvesting", moc[0].name, "plantation_status","To Harvesting")
                    frappe.msgprint(f"सॅम्पलिंग पूर्ण झाले")
                    frappe.msgprint(f"{self.id} तोडणीसाठी जाऊ शकतो.")
                    self.plantation_status="To Harvesting"
                    frappe.db.set_value("Cane Master", self.id ,"plantation_status", "To Harvesting")
                else:
                    frappe.msgprint(f"ऊसची परिपक्वता पूर्ण नाही")
                    # frappe.msgprint(f" {self.id}  चा तोडणीसाठीचा कालावधी पूर्ण झालेला नाही.")
            else:
                frappe.msgprint(f"{self.id} तोडणीसाठी गेला आहे.")
                
            # frappe.msgprint(f"तुमचे सरासरी ब्रिक्स {from_brix} ते {to_brix} दरम्यान असणे आवश्यक आहे आणि जोड्यांची संख्या {from_pairs} ते {to_pairs} दरम्यान असणे आवश्यक आहे")
        # for s in sam:

    def on_trash(self):
        frappe.db.set_value("Cane Master", self.id ,"plantation_status", "New")
		# doc = frappe.db.get_list("Cane Master")  #fields=["plantation_status", "name","form_number"
		# for a in doc:

			# eachdoc= frappe.get_doc("Cane Master",a.name)
			# if self.id == eachdoc.name:
			# 	eachdoc.plantation_status="New"
			# 	eachdoc.save()
			# 	break
	# def before_save(self):
	# 	frappe.db.set_value("Crop Sampling", self.id ,"plantation_status", "Add to Sampling")