// Copyright (c) 2023, vishakha singhal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project', {
	// refresh: function(frm) {
		refresh: function(frm) {
			frm.add_custom_button('Create Project Task', () => {
				frappe.new_doc('ProjectTask', {
					project: frm.doc.name
				})
			})
		
	}
});
