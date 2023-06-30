// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Dose Type", "refresh", function(frm) {
    frm.fields_dict['fertilize_details'].grid.get_field('fertilize_name').get_query = function(doc, cdt, cdn) {
        var child = locals[cdt][cdn];
        //console.log(child);
        return {    
            filters:[
                ['item_group', '=', 'AGRICULRE FERTLZER & CHIMECAL']
            ]
        };
    };
});
