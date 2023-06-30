// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bank Master', {
    refresh: function(frm) {
            frm.set_query("nationalize_bank", function() { 
                return {
                    filters: [
                        // ["Name", 'in', ["Customer", "Supplier","Employee","Shareholder"]]
						["Bank Name", "is_socity", '=', 0],
                    ]
                };
            });
        // }
    }
});
