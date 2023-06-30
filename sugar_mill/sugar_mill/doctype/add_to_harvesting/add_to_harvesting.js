// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Add to Harvesting', {
	// refresh: function(frm) {

	// }
});

frappe.ui.form.on('Add to Harvesting', {
	issue_list: function(frm) {
		frm.clear_table("crop_sampling_data")
		frm.refresh_field('crop_sampling_data')
		frm.call({
			method: 'list',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});
frappe.ui.form.on('Add to Harvesting', {
	check: function(frm) {
		frm.call({
			method:'selectall',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});

// frappe.ui.form.on('Add to Harvesting', {
// 	add_for_harvesting: function(frm) {
// 		frm.clear_table("selected_for_harvesting")
// 		frm.refresh_field('selected_for_harvesting')
// 		frm.call({
// 			method: 'mist',//function name defined in python
// 			doc: frm.doc, //current document
// 		});

// 	}
// });


