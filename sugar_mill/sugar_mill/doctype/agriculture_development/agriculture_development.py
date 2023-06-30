import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class AgricultureDevelopment(Document):
	@frappe.whitelist()
	def Calculate_Fertilizer(self,doctype,basel,preeathing,earth,rainy,ratoon1,ratoon2,area,croptype,cropvariety,areafixed,areagunta):
		# frappe.msgprint(str(areagunta))
		data = frappe.db.sql("""
                      select tabitem.item_code 'ItemCode',tabitem.item_name 'ItemName',tabitem.item_group 'Itemgroup',tabitem.name  , ceiling(ifnull(tabdose.quantity,0)* %(areagunta)s) 'Baselqty',
					  ceiling(ifnull(tabPreEarth.quantity,0) * %(areagunta)s)  'preearthqty',ceiling(ifnull(tabEarthing.quantity,0)* %(areagunta)s)  'earthingqty',ceiling(ifnull(tabRainy.quantity,0) * %(areagunta)s)  'Rainyqty',
     	              ceiling(ifnull(tabRatoon1.quantity,0) * %(areagunta)s)  'Ratoon1qty',	ceiling(ifnull(tabRatoon2.quantity,0) * %(areagunta)s)  'Ratoon2qty'
					from `tabItem` tabitem 
					left join
					(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
						from `tabDose Type` tabDosetype
						inner join `tabDose Type Item` tabDosetypeItem
						on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(basel)s and  tabDosetype.crop_type = %(croptype)s  
					) tabdose on tabdose.fertilize_name = tabitem.item_code
					left join
					(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
						from `tabDose Type` tabDosetype
						inner join `tabDose Type Item` tabDosetypeItem
						on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(preearth)s and  tabDosetype.crop_type = %(croptype)s  
					) tabPreEarth on tabPreEarth.fertilize_name = tabitem.item_code
					left join
						(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
					from `tabDose Type` tabDosetype
					inner join `tabDose Type Item` tabDosetypeItem
					on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(earthing)s and  tabDosetype.crop_type = %(croptype)s 
						) tabEarthing on tabEarthing.fertilize_name = tabitem.item_code
					left join
						(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
					from `tabDose Type` tabDosetype
					inner join `tabDose Type Item` tabDosetypeItem
					on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(rainy)s and  tabDosetype.crop_type = %(croptype)s  
						) tabRainy on tabRainy.fertilize_name = tabitem.item_code
                    left join
						(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
					from `tabDose Type` tabDosetype
					inner join `tabDose Type Item` tabDosetypeItem
					on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(ratoon1)s and  tabDosetype.crop_type = %(croptype)s   
						) tabRatoon1 on tabRatoon1.fertilize_name = tabitem.item_code
							left join
						(
						select tabDosetypeItem.fertilize_name,tabDosetypeItem.parent,tabDosetypeItem.quantity,tabDosetypeItem.uom
					from `tabDose Type` tabDosetype
					inner join `tabDose Type Item` tabDosetypeItem
					on tabDosetypeItem.parent =  tabDosetype.name  where dose = %(ratoon2)s and  tabDosetype.crop_type = %(croptype)s   
						) tabRatoon2 on tabRatoon2.fertilize_name = tabitem.item_code					
                       where tabitem.item_group = 'AGRICULRE FERTLZER & CHIMECAL'  AND (
        IFNULL(tabdose.quantity, 0) <> 0
        OR IFNULL(tabPreEarth.quantity, 0) <> 0
        OR IFNULL(tabEarthing.quantity, 0) <> 0 
        OR IFNULL(tabRainy.quantity, 0) <> 0 
        OR IFNULL(tabRatoon1.quantity, 0) <> 0 
        OR IFNULL(tabRatoon2.quantity, 0) <> 0 
    ) order by  tabitem.item_code
										""",{
							'basel': basel	,	'preearth': preeathing,'earthing': earth, 'rainy': rainy,'area' : area ,'ratoon1' : ratoon1,'ratoon2' : ratoon2, 'croptype' : croptype,'areagunta':areagunta
						},  as_dict=1)	
		if data:
			# frappe.msgprint(str(data))
			for row in data:			
				self.append("agriculture_development_item",{
								"item_code":row.ItemCode,
								"basel":row.Baselqty,
								"pre_earthing":row.preearthqty,
								"earth":row.earthingqty,
								"rainy":row.Rainyqty,
        						"ratoon_1":row.Ratoon1qty,
                                "ratoon_2":row.Ratoon2qty,
								"qty": float(row.Baselqty) + float(row.preearthqty) + float(row.earthingqty) +  float(row.Rainyqty) + float(row.Ratoon1qty) +float(row.Ratoon2qty)
								
								}
								)	
		else :
			return 0
		return data
  
		# if(basel == "True"):
		# 	databasel = frappe.ge_all("Dose Type",filters={'dose': 'Basel'},fields=["*"])
		# 	frappe.msgprint(str(databasel))
		# 	for d in databasel:				
		# 		frappe.msgprint(d.area)

		# if(preeathing == "True"):
		# 	datapreeathing = frappe.get_all("Dose Type",filters={'dose': 'Pre-Earth'},fields=["*"])
		# 	frappe.msgprint(str(datapreeathing))
		# 	for d in datapreeathing:				
		# 		frappe.msgprint(d.area)
    
		# if(earth == "True"):
		# 	dataearth = frappe.get_all("Dose Type",filters={'dose': 'Earthing'},fields=["*"])
		# 	frappe.msgprint(str(dataearth))
		# 	for d in dataearth:				
		# 		frappe.msgprint(d.area)

		# if(rainy == "True"):
		# 	datarainy = frappe.get_all("Dose Type",filters={'dose': 'Rainy'},fields=["*"])
		# 	frappe.msgprint(str(datarainy))
		# 	for d in datarainy:				
		# 		frappe.msgprint(d.area)

@frappe.whitelist()
def make_delivery_challan(source_name,target_doc = None):
	def set_missing_values(source,target):
		target.run_method("set_missing_values")
		target.run_method("calculate_taxes_and_totals")

	def update_item_quantity(source,target,source_parent):
		target.qty = source.qty
		target.item_code = source.item_code

	doclist = get_mapped_doc(
		"Agriculture Development",
				source_name,
		{
				"Agriculture Development":{
					"doctype": "Delivery Note",
				"field_map":{
								"supplier":"customer",
								"plant_name":"",
							},
				},
				"Agriculture Development Item":{
				"doctype":"Delivery Note Item",
				"field_map":{
                    "item_name":"item_name",
                    "stock_uom":"uom",
                    "season":"season",
				},
				"postprocess":update_item_quantity,
				},
			target_doc:
			set_missing_values,
		}
		)
	# frappe.msgprint("doclist")
	return doclist

@frappe.whitelist()
def make_sales_order(source_name,target_doc = None):
	def set_missing_values(source,target):
		target.run_method("set_missing_values")
		target.run_method("calculate_taxes_and_totals")

	def update_item_quantity(source,target,source_parent):
		target.qty = source.qty
		target.item_code = source.item_code

	doclist = get_mapped_doc(
		"Agriculture Development",
				source_name,
		{
				"Agriculture Development":{
					"doctype": "Sales Order",
				"field_map":{
								"supplier":"customer",
								"plant_name":"",
							},
				},
				"Agriculture Development Item":{
				"doctype":"Sales Order Item",
				"field_map":{
                    "item_name":"item_name",
                    "stock_uom":"uom",
                    "season":"season",
				},
				"postprocess":update_item_quantity,
				},
			target_doc:
			set_missing_values,
		}
		)
	# frappe.msgprint("doclist")
	return doclist

@frappe.whitelist()
def methodcheck(source_name,target_doc = None):
    pass
