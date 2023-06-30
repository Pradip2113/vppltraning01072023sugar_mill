frappe.ui.form.on('Agriculture Development', {
    refresh: function(frm) {
            frm.set_query("cane_registration_id", function() { // Replace with the name of the link field
                return {
                    filters: [
                        ["Cane Master", "season", '=', frm.doc.season] // Replace with your actual filter criteria
                    ]
                };
            });
        }
    });


frappe.ui.form.on('Agriculture Development', {
	update(frm) {
	    debugger
        frm.clear_table("agriculture_development_item")
		frm.refresh_field("agriculture_development_item")
	    var basel = "",preeathing ="",earth="",rainy="",ratoon1="",ratoon2="";
        var fixedarea = Number(frm.doc.development_area.toFixed(0))
        var guntacal = (frm.doc.development_area - fixedarea)
        var guntacalfix = Number(guntacal.toFixed(2))
        var areagunta = ((fixedarea*40)+(guntacalfix*100))/40
		var checkedB = frm.get_field('basel').get_value();
        if (checkedB) 
        {
           	basel = "Basel";
        }
        else 
        {
            basel = "False";
        }
        
        var checkedP = frm.get_field('pre_earthing').get_value();
        if (checkedP) 
        {
           	preeathing = "Pre-Earth";
        }
        else 
        {
            preeathing = "False";
        }
        
        var checkedE = frm.get_field('earth').get_value();
        if (checkedE) 
        {
           	earth = "Earthing";
        }
        else 
        {
            earth = "False";
        }
        
        var checkedR = frm.get_field('rainy').get_value();
        if (checkedR) 
        {
           	rainy = "Rainy";
        }
        else 
        {
            rainy = "False";
        }
        var checkedRt1 = frm.get_field('ratoon_1').get_value();
        if (checkedRt1) 
        {
            ratoon1 = "Ratoon 1";
        }
        else 
        {
            ratoon1 = "False";
        }
        var checkedRt2 = frm.get_field('ratoon_2').get_value();
        if (checkedRt2) 
        {
            ratoon2 = "Ratoon 2";
        }
        else 
        {
            ratoon2 = "False";
        }
      
       	frm.call	({
			method:"Calculate_Fertilizer",
			doc:frm.doc,
			args:{
				doctype:"Agriculture Development",
				basel:basel,
				preeathing:preeathing,
				earth:earth,
				rainy:rainy,
                ratoon1:ratoon1,
                ratoon2:ratoon2,
                croptype : frm.doc.crop_type,
                cropvariety : frm.doc.crop_variety,
				area:parseFloat(frm.doc.development_area),
                areafixed:fixedarea,
                areagunta:areagunta
				},
			callback: function(r) {
					// frappe.msgprint("Loaded")
					frm.refresh_field('table_9');
			}
		})
	
	},
    refresh(frm){
        debugger
        // frm.trigger("make_delivery_challan")
        frm.trigger("make_sales_order")
    },
    make_sales_order(frm){
        // if(frm.doc.docstatus === 1)
        // {
            frm.add_custom_button(__("Sales Order"),() => {
                frappe.model.open_mapped_doc({
                    method:"sugar_mill.sugar_mill.doctype.agriculture_development.agriculture_development.make_sales_order",
                    frm:frm
                })
            },__("Make")
            )
        // }
    //     frm.add_custom_button(__("Delivery Challan"),() => {
    //     debugger
    //         frm.call	({
	// 		method:"make_delivery_challan",
	// 		doc:frm.doc,
	// 		args:{
	// 			frm:frm
	// 			},
	// 		callback: function(r) {
	// 				frappe.msgprint("Loaded")
					
	// 		}
	// 	})
    // },__("Make"))
    }

});