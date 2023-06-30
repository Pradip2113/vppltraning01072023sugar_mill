// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Back To Sampling', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Back To Sampling', {
	issue_list: function(frm) {
		frm.clear_table("cane_harvesting_data")
		frm.refresh_field('cane_harvesting_data')
		frm.call({
			method: 'list',//function name defined in python
			doc: frm.doc, //current document
		});
		
	}
});

frappe.ui.form.on('Back To Sampling', {
	check: function(frm) {
		frm.call({
			method: 'selectall',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});
