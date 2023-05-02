// Copyright (c) 2023, vishakha and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["abc"] = {
	"filters": [
		{
		"fieldname":"v_name",
		"label": Vname,
		"fieldtype": "data",
		//"options": "Company",
		"default": frappe.defaults.get_user_default("abc")
		}

	]
};
