// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on("Fertilizer Material Request Item", "qty", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
     if(d.rate >= 0 && d.qty >= 0){
        var result = ((d.rate * d.qty)).toFixed(2);
        frappe.model.set_value(cdt, cdn, 'amount', result);
    }
});

frappe.ui.form.on("Fertilizer Material Request Item", "rate", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
     if(d.rate >= 0 && d.qty >= 0){
        var result = ((d.rate * d.qty)).toFixed(2);
        frappe.model.set_value(cdt, cdn, 'amount', result);
    }
});
