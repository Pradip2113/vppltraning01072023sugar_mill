// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Test Child', {
	name1: function(frm) {
		frm.call({
			method: 'vivek',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});

frappe.ui.form.on('Test Child', {
	check: function(frm) {
		frm.call({
			method: 'abhi',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});

