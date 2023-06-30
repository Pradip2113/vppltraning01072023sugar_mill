// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Crop Sampling', {
// 	sample_button: function(frm) {
// 		frm.call({
// 						method:'sample_button',//function name defined in python
// 						doc: frm.doc, //current document
// 					});

// 	}
// });

// frappe.ui.form.on('Add To Sampling', {
// 	check: function(frm) {
// 		frm.call({
// 			method:'vivek',//function name defined in python
// 			doc: frm.doc, //current document
// 		});

// 	}
// });

frappe.ui.form.on('Crop Sampling', {
    brix_top: function(frm) {
        frm.set_value('average_brix', (frm.doc.brix_top + frm.doc.brix_middle + frm.doc.brix_bottom)/3);
    },
    brix_middle: function(frm) {
        frm.set_value('average_brix', (frm.doc.brix_top + frm.doc.brix_middle + frm.doc.brix_bottom)/3);
    },
    brix_bottom: function(frm) {
        frm.set_value('average_brix', (frm.doc.brix_top + frm.doc.brix_middle + frm.doc.brix_bottom)/3);
    }
});