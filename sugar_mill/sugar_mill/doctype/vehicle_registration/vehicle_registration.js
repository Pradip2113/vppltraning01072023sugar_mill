// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Registration item', {
	cart_no:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total1 = 0;
	frm.doc.vehicle_details_tab.forEach(function(d) { total1 = parseFloat(d.idx); });
	frm.set_value("total_numbers_of_vehicle", total1);
	refresh_field("total_numbers_of_vehicle");
  },
  vehicle_details_tab_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total1 = 0;
	frm.doc.vehicle_details_tab.forEach(function(d) { total1 = parseFloat(d.idx); });
	frm.set_value("total_numbers_of_vehicle", total1);
	refresh_field("total_numbers_of_vehicle");
   }
 });

 frappe.ui.form.on('Vehicle Registration', {
	after_save: function(frm) {
		frm.call({
			method:'vivo',//function name defined in python
			doc: frm.doc, //current document
		});
		
	}
});

frappe.ui.form.on("Vehicle Registration item", "submit_date", function(frm, cdt, cdn){
	var d = locals[cdt][cdn];   
	frappe.model.set_value(cdt, cdn, "no_of_days", frappe.datetime.get_day_diff(d.submit_date, d.issue_date) +1);
	refresh_field("no_of_days");
	});
	frappe.ui.form.on("Vehicle Registration item", "issue_date", function(frm, cdt, cdn){
	var d = locals[cdt][cdn];   
	frappe.model.set_value(cdt, cdn, "no_of_days", frappe.datetime.get_day_diff(d.submit_date, d.issue_date) +1 );
	refresh_field("no_of_days");
	});


	frappe.ui.form.on("Vehicle Registration", {
		refresh: function(frm) {
			// if (frm.doc.isfarmer == 1) { // Replace with the name of the checkbox field
				frm.set_query("transporter_code", function() { // Replace with the name of the link field
					return {
						filters: [
							["Farmer List", "is_transporter", '=', 1] // Replace with your actual filter criteria
						]
					};
				});
			// }
		}
	});





// frappe.ui.form.on('Vehicle Registration', {
// 	after_save: function(frm) {frm.call({
// 			method:'slip_number',//function name defined in python
// 			doc: frm.doc, //current document
// 		});
// 	}
// });

// frappe.ui.form.on('Vehicle Registration item', {
// 	submit_date: function(frm) {
// 		frm.call({
// 			method:'sugar_mill.sugar_mill.doctype.vehicle_registration_item.calculate_days',//function name defined in python  method: "sugar_mill.sugar_mill.doctype.vehicle_registration_item.calculate_days_between_dates" 
// 			doc: frm.doc, //current document       /home/quantbitserver/bench-vppl/apps/sugar_mill/sugar_mill/sugar_mill/doctype/vehicle_registration_item/vehicle_registration_item.py
// 		});
		
// 	}
// });


// frappe.call({
// 	method: "sugar_mill.sugar_mill.doctype.vehicle_registration_item.calculate_days",
// 	args: {
// 	  docname: "Vehicle Registration Item",
// 	},
// 	callback: function (response) {
// 	  // Process the response here
// 	},
//   });
  

// frappe.ui.form.on('Vehicle Registration item', {
// 	submit_date: function(frm) {
// 		frm.call({
// 			method:'calculate_days_between_dates',//function name defined in python
// 			doc: frm.doc, //current document
// 		});
		
// 	}
// });


// frappe.ui.form.on('Vehicle Registration item', {
//     submit_date: function(frm) {
//         calculateNumberOfDays(frm);
//     }
// });

// function calculateNumberOfDays(frm) {
//     var start_date = frappe.datetime.str_to_obj(frm.doc.issue_date);
//     var end_date = frappe.datetime.str_to_obj(frm.doc.submit_date);

//     // Calculate the time difference in milliseconds
//     var timeDiff = end_date.getTime() - start_date.getTime();

//     // Convert the time difference from milliseconds to days
//     var numberOfDays = Math.ceil(timeDiff / (1000 * 3600 * 24));

//     // Set the value of the 'number_of_days' field
//     // frm.set_value('no_of_days', numberOfDays);
// 	frappe.msgprint(numberOfDays)
// }


// frappe.ui.form.on('Vehicle Registration item', {
//     submit_date: function(frm) {
//         calculateNumberOfDays(frm);
//     }
// });

// function calculateNumberOfDays(frm) {
//     var start_date = frappe.datetime.str_to_obj(frm.doc.issue_date);
//     var end_date = frappe.datetime.str_to_obj(frm.doc.submit_date);

//     // Calculate the time difference in milliseconds
//     var timeDiff = end_date.getTime() - start_date.getTime();

//     // Convert the time difference from milliseconds to days
//     var numberOfDays = Math.ceil(timeDiff / (1000 * 3600 * 24));

//     // Set the value of the 'no_of_days' field
//     frm.doc.no_of_days = numberOfDays;
//     refresh_field('no_of_days');
// }



// 	// JavaScript program to illustrate
// 	// calculation of no. of days between two date
	
// 	// To set two dates to two variables
// 	var date1 = new Date("06/30/2019");
// 	var date2 = new Date("07/30/2019");
	
// 	// To calculate the time difference of two dates
// 	var Difference_In_Time = date2.getTime() - date1.getTime();
	
// 	// To calculate the no. of days between two dates
// 	var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24);
	
// 	//To display the final no. of days (result)
// 	console.log( Difference_In_Days);


	// frappe.ui.form.on('Vehicle Registration item', {
	// 	submit_date: function(frm) {
	// 		calculateNumberOfDays(frm);
	// 	}
	// });
	
	// function calculateNumberOfDays(frm) {
	// 	var start_date = frappe.datetime.str_to_obj(frm.doc.issue_date);
	// 	var end_date = frappe.datetime.str_to_obj(frm.doc.submit_date);
	// 	frappe.msgprint(start_date);
	// 	// Calculate the time difference in milliseconds
	// 	var timeDiff = end_date.getTime() - start_date.getTime();
	
	// 	// Convert the time difference from milliseconds to days
	// 	var numberOfDays = timeDiff / (1000 * 3600 * 24);
	// 	console.log(numberOfDays);
	
	// 	// Set the value of the 'no_of_days' field
	// 	// frm.doc.no_of_days = numberOfDays;
	// 	// refresh_field('no_of_days');
	// }
	
