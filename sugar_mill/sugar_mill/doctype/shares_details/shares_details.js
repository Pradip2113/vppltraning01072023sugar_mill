// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Shares Details', {
    refresh: function(frm) {
        // if (frm.doc.isfarmer == 1) { // Replace with the name of the checkbox field
            frm.set_query("member_type", function() { // Replace with the name of the link field
                return {
                    filters: [
                        ["Name", 'in', ["Customer", "Supplier","Employee","Shareholder"]]
                    ]
                };
            });
        // }
    }
});
