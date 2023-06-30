// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Retail Sale', {
    refresh: function(frm) {
        // if (frm.doc.isfarmer == 1) { // Replace with the name of the checkbox field
            frm.set_query("party_type", function() { // Replace with the name of the link field
                return {
                    filters: [
                        ["Name", 'in', ["Customer", "Supplier","Employee","Shareholder"]]
                    ]
                };
            });
        // }
    }
});


frappe.ui.form.on('Retail Sale', {
	party: function (frm) {
		frm.call({
			method:'fetch_shares',
			doc: frm.doc,
		});	
	}
})

frappe.ui.form.on('Retail Sales Item', {
	item_code: function (frm) {
		frm.call({
			method:'fetch_qty',
			doc: frm.doc,
		});	
	}
})
