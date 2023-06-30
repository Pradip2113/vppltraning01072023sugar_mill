// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Advance Request', {
	gang_type: function(frm) {
		frm.call({
			method:'fetch_amount',//function name defined in python
			doc: frm.doc, //current document
		});
		
	}
});

// frappe.ui.form.on('Advance Request', {
// 	contractor_name: function(frm) {
// 		frm.call({
// 			method:'paid_amount',//function name defined in python
// 			doc: frm.doc, //current document
// 		});
		
// 	}
// });

frappe.ui.form.on("Advance Request item", {
	advance:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total1 = 0;
	var total2 = 0.0;
	frm.doc.items.forEach(function(d) { total1 += d.advance; });
	frm.set_value("paid_amount_till_today", total1);
	total2 = frm.doc.amount_limit - total1;
	frm.set_value("remaining_amount", total2);
	refresh_field("paid_amount_till_today");
	refresh_field("remaining_amount");

  },
   items_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total1 = 0;
	var total2 = 0.0;
	frm.doc.items.forEach(function(d) { total1 += d.advance; });
	frm.set_value("paid_amount_till_today", total1);
	total2 = frm.doc.amount_limit - total1;
	frm.set_value("remaining_amount", total2);
	refresh_field("paid_amount_till_today");
	refresh_field("remaining_amount");
   }
 });