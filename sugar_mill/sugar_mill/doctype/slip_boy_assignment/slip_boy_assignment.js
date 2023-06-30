// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Slip Boy Assignment', {
    refresh: function(frm) {
            frm.set_query("village", function() { // Replace with the name of the link field
                return {
                    filters: [
                        ["Village", "circle_office", '=', frm.doc.circle_office] // Replace with your actual filter criteria
                    ]
                };
            });
        }
    });

