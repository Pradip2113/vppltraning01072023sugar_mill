frappe.ui.form.on('Farmer List View', {
	refresh: function(frm) {
	  var page_length = 200;
	  var page_number = 1;
  
	  loadFarmerList(page_number, page_length, '', frm);
	},
	vendor_name: function(frm) {
	  var page_length = 200;
	  var page_number = 1;
	  loadFarmerList(page_number, page_length, frm.doc.vendor_name, frm);
	}
  });
  
  function loadFarmerList(page_number, page_length, vendor_name, frm) {
	frappe.call({
	  method: 'frappe.client.get_list',
	  args: {
		doctype: 'Farmer List',
		fields: ['supplier_name', 'workflow_state', 'aadhaar_number', 'supplier_group', 'village', 'circle_office', 'name', 'existing_supplier_code', 'is_farmer', 'is_transporter', 'is_harvester'],
		limit_start: (page_number - 1) * page_length,
		limit_page_length: page_length,
		filters: {
		  'supplier_name': ['like', '%' + vendor_name + '%']
		},
  
	  },
	  callback: function(response) {
		var data = response.message;
  
		var help_content = `
		  <div class="table-responsive">
		<!--   <div class="table-responsive" style="width:100; height:450px; overflow:auto;">  -->
			<table class="table table-bordered">
			  <thead>
				<tr>
				  <th style="position: sticky;top: 0;background-color: white;">Vendor Code</th>
				  <th style="position: sticky;top: 0;background-color: white;">Vendor Name</th>
				  <th style="position: sticky;top: 0;background-color: white;">Village</th>
				  <th style="position: sticky;top: 0;background-color: white;">Circle</th>
				  <th style="position: sticky;top: 0;background-color: white;">Aadhaar No</th>
				  <th style="position: sticky;top: 0;background-color: white;">Service Type</th>
				
				  <th style="position: sticky;top: 0;background-color: white;">Status</th>
				</tr>
			  </thead>
			  <tbody>
		`;
  
		for (var i = 0; i < data.length; i++) {
		  var supplierName = data[i].supplier_name || '';
		  var recordId = data[i].name || '';
  
		  help_content += "<tr>";
		  help_content += `<td>${data[i].existing_supplier_code}</td>`;
		  help_content += `<td><a href="https://trainingerpvppl.erpdata.in/app/farmer-list/${recordId}">${supplierName}</a></td>`;
		  help_content += `<td>${data[i].village || ''}</td>`;
		  help_content += `<td>${data[i].circle_office || ''}</td>`;
		  help_content += `<td>${data[i].aadhaar_number || ''}</td>`;
		  if (data[i].is_farmer === 1 && data[i].is_transporter === 0 && data[i].is_harvester === 0) {
			help_content += `<td>${'FR' || ''}</td>`;
		  } 
		  if (data[i].is_farmer === 0 && data[i].is_transporter === 1 && data[i].is_harvester === 0) {
			help_content += `<td>${'TR' || ''}</td>`;
		  } 
		  if (data[i].is_farmer === 0 && data[i].is_transporter === 0 && data[i].is_harvester === 1) {
			help_content += `<td>${'HR' || ''}</td>`;
		  } 
		  if (data[i].is_farmer === 1 && data[i].is_transporter === 1 && data[i].is_harvester === 0) {
			help_content += `<td>${'FR,TR' || ''}</td>`;
		  }
		  if (data[i].is_farmer === 1 && data[i].is_transporter === 0 && data[i].is_harvester === 1) {
			help_content += `<td>${'FR,HR' || ''}</td>`;
		  } 
		  if (data[i].is_farmer === 0 && data[i].is_transporter === 1 && data[i].is_harvester === 1) {
			help_content += `<td>${'TR,HR' || ''}</td>`;
		  } 	   
		  if (data[i].is_farmer === 1 && data[i].is_transporter === 1 && data[i].is_harvester === 1) {
			help_content += `<td>${'FR,TR,HR' || ''}</td>`;
		  }
		  if (data[i].is_farmer === 0 && data[i].is_transporter === 0 && data[i].is_harvester === 0) {
			help_content += `<td>${'-' || ''}</td>`;
		  } 
		  help_content += `<td>${data[i].workflow_state || ''}</td>`;
  
		  help_content += "</tr>";
		}
  
		help_content += `
			  </tbody>
			</table>
		  </div>
		`;
  
		set_field_options("show_html", help_content);
	  }
	});
  }
  