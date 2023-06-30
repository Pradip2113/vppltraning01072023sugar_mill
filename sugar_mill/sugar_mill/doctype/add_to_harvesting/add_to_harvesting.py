# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AddtoHarvesting(Document):
    
    # pass
    @frappe.whitelist()
    def list(self):
        village_items = [d.village_link for d in self.village]
        condition_1 = "{}".format("  or  ".join(["d.area == '{}'".format(name) for name in village_items]))
        circle_office_items = [d.circle_office_link for d in self.circle_office]
        condition_2 = "{}".format("  or  ".join(["d.circle_office == '{}'".format(name) for name in circle_office_items]))
        crop_variety_items = [d.crop_variety_link for d in self.crop_variety]
        condition_3 = "{}".format("  or  ".join(["d.crop_variety == '{}'".format(name) for name in crop_variety_items]))
        crop_type_items = [d.crop_type_link for d in self.crop_type]
        condition_4 = "{}".format("  or  ".join(["d.crop_type == '{}'".format(name) for name in crop_type_items]))

        if condition_1 == "":
            frappe.throw("Please fill up village")
        if condition_2 == "":
            frappe.throw("Please fill up circle_office")
        if condition_3 == "":
            frappe.throw("Please fill up crop_variety")
        if condition_4 == "":
            frappe.throw("Please fill up crop_type")

    #     # frappe.msgprint("this is working")
        doc = frappe.db.get_list(
            "Crop Sampling",
            fields=[
                "name",
                "id",
                "grower_name",
                "form_number",
                "plantattion_ratooning_date",
                "area",
                "circle_office",
                "crop_variety",
                "plantation_status",
                "season",
                "average_brix",
                "no_of_pairs",
                "crop_type"
            ],
        )
        for d in doc:
            # frappe.msgprint(str(d.plantattion_ratooning_date))
            if (d.plantation_status == "To Sampling"
                and (
                    str(self.from_date)
                    <= str(d.plantattion_ratooning_date)
                    <= str(self.to_date)
                )
                and (float(self.from_brix) <= float(d.average_brix) <= float(self.to_brix))
                and (float(self.from_pairs)<= float(d.no_of_pairs)<= float(self.to_pairs))
                and (self.season == d.season)
                and eval(condition_1)
                and eval(condition_2)
                and eval(condition_3)
                and eval(condition_4)
                
            ):  # d.plantation_status != "Added To Sampling" and
    #             # if(self.village == d.area) and (self.circle_office == d.circle_office) and (self.crop_variety == d.crop_variety):
                self.append(
                    "crop_sampling_data",
                    {
                        "id": d.id,
                        "crop_sample_id":d.name,
                        "brix": d.average_brix,
                        "no_of_pairs": d.no_of_pairs,
                        "grower_name": d.grower_name,
                        "form_number": d.form_number,
                        "plantattion_ratooning_date": d.plantattion_ratooning_date,
                        "plantation_status": d.plantation_status,
                        "area": d.area,
                        "circle_office": d.circle_office,
                        "crop_variety": d.crop_variety,
                        "season": d.season,
                        "crop_type":d.crop_type
                    },
                )
        if not self.get("crop_sampling_data"):
            frappe.throw("The record You are looking for are not available")

    @frappe.whitelist()
    def selectall(self):
        children = self.get("crop_sampling_data")

        if not children:
            return
        all_selected = all([child.check for child in children])
        value = 0 if all_selected else 1
        for child in children:
            child.check = value

    def before_save(self):
        for row in self.get('crop_sampling_data'):
            if row.check:
                doc=frappe.new_doc('Crop Harvesting')
                doc.brix =row.brix
                doc.crop_sample_id=row.crop_sample_id
                doc.no_of_pairs=row.no_of_pairs
                doc.id =row.id
                doc.insert()
                doc.save
                moc = frappe.db.get_all("Crop Harvesting", fields=["name"], order_by="creation DESC", limit=1)
                frappe.db.set_value("Crop Harvesting", moc[0].name, "plantation_status","To Harvesting")
                
                
        for po in self.get("crop_sampling_data"):
                if po.check:
                    frappe.db.set_value("Cane Master", po.id ,"plantation_status", "To Harvesting")
                    frappe.db.set_value("Crop Sampling", po.crop_sample_id ,"plantation_status", "To Harvesting")
            
     
    # def on_trash(self):
        
    #     doc =frappe.db.get_list("Crop Sampling")
    #     for i in self.get('crop_sampling_data'):
    #         for a in doc:
    #             eachdoc= frappe.get_doc("Crop Sampling",a.name)
    #             if i.id == eachdoc.id:
    #                 eachdoc.plantation_status="To Sampling"
    #                 eachdoc.save()
    #                 break
                
    #     moc = frappe.db.get_list("Crop Harvesting", fields=["id","name"])
    #     for j in self.get('crop_sampling_data'):
    #         for c in moc:
    #             if j.id == c.id:
    #                 frappe.delete_doc("Crop Harvesting",c.name)
    #                 break
