// frappe.ui.form.on('Bank Details', {
//   refresh: function(frm) {
//           frm.set_query("branch", function(doc,cdn,cdt) { 
//             var d = locals[cdt][cdn];// Replace with the name of the link field
//               return {
//                   filters: [
//                       ["Bank Master", "branch", '=', d.branch] // Replace with your actual filter criteria
//                   ]
//               };
//           });
//       }
//   });


frappe.ui.form.on('Bank Details', 'refresh', function(frm) {
  cur_frm.fields_dict['bank_name'].grid.get_field('bank_name').get_query = function(doc, cdt, cdn) {
      return {
          filters: {
              'bank_name': ['like', '%'],
              'bank_master': {
                  'is_society': 0
              }
          }
      };
  };
});
frappe.ui.form.on('Bank Details', {
	branch: function (frm) {
		frm.call({
			method:'fetchbranch',
			doc: frm.doc,
		});	
	}
})

frappe.ui.form.on('Bank Details', {
	bank_name: function (frm) {
		frm.call({
			method:'fetchbranch',
			doc: frm.doc,
		});	
	}
})
// frappe.ui.form.on('Bank Details', {
//   nationalize_bank: function(frm,cdt,cdn) {
//           frappe.msgprint("ozzzzzo");
//           var d = locals[cdt][cdn];
//           frm.set_query("bank_name", function(doc,cdt,cdn) { // Replace with the name of the link field
//               return {
//                   filters: [
//                       [cdt,cdn,"Nationalize Bank", "bank_name", '=', d.nationalize_bank] // Replace with your actual filter criteria
//                   ]
//               };
//           });
//       }
//   });


frappe.ui.form.on('Farmer List', {
    branch: function(frm) {
      var branch = frm.doc.branch;
      if (branch === 'Bedkihal') {
        frm.set_value('naming_series', 'FA-.#');
      } else if (branch === 'Nagpur') {
        frm.set_value('naming_series', 'NG-.#');
      }
    }
  });
  


frappe.ui.form.on('Bank Details', {
	farmer: function(frm) {
		frm.call({
			method: 'validation_to_bank_details',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});
frappe.ui.form.on('Bank Details', {
	harvester: function(frm) {
		frm.call({
			method: 'validation_to_bank_details',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});
frappe.ui.form.on('Bank Details', {
	transporter: function(frm) {
		frm.call({
			method: 'validation_to_bank_details',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});


frappe.ui.form.on('Farmer List', {
    validate: function(frm) {
        var aadhaar_number = frm.doc.aadhaar_number;
        if (aadhaar_number && !/^\d{12}$/.test(aadhaar_number)) {
            frappe.msgprint("Aadhaar Number must be 12 digits only");
            frappe.msgprint("आधार क्रमांक १२ अंकी असणे आवश्यक आहे");
            validated = false;
        }
    }
});
// frappe.ui.form.on('Farmer List', {
//     mobile_number: function(frm) {
//         var mobile_number = frm.doc.mobile_number;
//         if (mobile_number && !/^\d{10}$/.test(mobile_number)) {
//             frappe.msgprint("Mobile Number must be 10 digits only");
//             frappe.msgprint("मोबाईल नंबर १० अंकी असणे आवश्यक आहे");
//             validated = false;
//         } 
//     }
// });

// frappe.ui.form.on('Farmer List', {
//     validate: function(frm) {
//         var pan_no = frm.doc.pan_number;
//         if (!validate_pan(pan_no)) {
//             frappe.msgprint("Invalid PAN number");
//             frappe.msgprint("पॅन नंबर चुकीचा आहे");
//             validated = false;
//         }
//     }
// });

// function validate_pan(pan_no) {
//     var regex = /[A-Z]{5}[0-9]{4}[A-Z]{1}/;
//     return pan_no.length <= 10 && regex.test(pan_no);
// }

// Age Calculation from Date of Birth
frappe.ui.form.on('Farmer List', {
    date_of_birth: function(frm) {
      // frappe.msgprint("gdfffhfh")
        frm.set_value('age', '');
        var dob = new Date(frm.doc.date_of_birth);
        var today = new Date();
        var age = today.getFullYear() - dob.getFullYear();
        var month = today.getMonth() - dob.getMonth();
        if (month < 0 || (month === 0 && today.getDate() < dob.getDate())) {
            age--;
        }
        frm.set_value('age', age);
    }
});

frappe.ui.form.on('Bank Details', {
	is_active: function(frm) {
		frm.call({
			method: 'on_no',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});




// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Farmer List', {
// 	aadhaar_number: function(frm) {
// 		frm.call({
// 						method:'aadhaar_number_vali',//function name defined in python
// 						doc: frm.doc, //current document
// 					});

// 	}
// });

// cur_frm.fields_dict.aadhaar_number.df.get_query = function() {
//     return {
//         filters: {
//             "length": 12
//         }
//     };
// };

// frappe.ui.form.on('Farmer List', {
//     aadhaar_number: function(frm) {
//         if (frm.doc.aadhaar_number && frm.doc.aadhaar_number.length !== 12) {
//             frappe.msgprint("The Aadhar No should be 12 digits.");
//         }d
//     }
// });

// frappe.ui.form.on('Farmer List', {
//     validate: function(frm) {
//         if (frm.doc.aadhaar_number && frm.doc.aadhaar_number.length !== 12) {
//             frappe.msgprint("The Aadhar No should be 12 digits.");
//             validated = false;
//         }
//     }
// });



// frappe.ui.form.on('Farmer List', {supplier_type: function(frm) {frm.call({method: 'update_docs',doc: frm.doc, });},});
// frappe.ui.form.on('Farmer List', {supplier_name: function(frm) {frm.call({method: 'update_docs',doc: frm.doc, });},});
// frappe.ui.form.on('Farmer List', {supplier_group: function(frm) {frm.call({method: 'update_docs',doc: frm.doc, });},});
// frappe.ui.form.on('Farmer List', {village: function(frm) {frm.call({method: 'update_docs',doc: frm.doc, });},});
// frappe.ui.form.on('Farmer List', {taluka: function(frm) {frm.call({method: 'update_docs',doc: frm.doc, });},});
// frappe.ui.form.on('Farmer List', {circle_office: function(frm) {frm.call({method: 'update_docs',doc: frm.doc, });},});
// frappe.ui.form.on('Farmer List', {state: function(frm) {frm.call({method: 'update_docs',doc: frm.doc, });},});
// frappe.ui.form.on('Farmer List', {pin_code: function(frm) {frm.call({method: 'update_docs',doc: frm.doc, });},});


// frappe.ui.form.on('Farmer List', {
// 	refresh: function(frm) {
//      frappe.msgprint("abcdefg")
// frappe.listview_settings['Farmer List'] = {
	
//     hide_in_listview: ['name'], // Specify the field(s) you want to hide
//     get_indicator: function(doc) {
//         // Your custom indicator logic here
//     }
// };

// 	}
// });


// frappe.ui.form.on('Farmer List', {
// 	refresh: function(frm) {
// 		frappe.msgprint("abcdefg");
// 	},
// });

// frappe.listview_settings['Farmer List'] = {
// 	hide_in_listview: ['status'], // Specify the field(s) you want to hide
// 	get_indicator: function(doc) {
// 		// Your custom indicator logic here
// 	}
// };







// frappe.ui.form.on('Farmer List', 'refresh', function(frm) {
//     // Hide the ID column in the list view
//     frappe.listview_settings['Farmer List'].hide_in_listview = ['name'];

//     // Refresh the list view to apply the changes
//     frappe.listview_settings['Farmer List'].refresh();
// });

// frappe.ui.form.on('Farmer List', {
//     refresh: function(frm) {
//         frappe.msgprint("sfgdjh")
//         // Hide the ID column in the list view
//         frm.get_field('name').toggle(false);
//     }
// });

