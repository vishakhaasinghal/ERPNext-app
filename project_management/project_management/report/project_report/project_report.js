// Copyright (c) 2023, vishakha singhal and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Project Report"] = {
	"filters": [
		{
			"fieldname" : "project_id",
			"label": __('Project Id'),
			"fieldtype": 'Link',
            "options": 'Project'
		},
		{
			"fieldname" : "title_of_the_project",
			"label": __('Project Title'),
			"fieldtype": 'Data'
		},
		{
			"fieldname" : "start_date",
			"label": __('Project Start Date'),
			"fieldtype": 'Date'
		},
		{
			"fieldname" : "expected_end_date",
			"label": __('Project Expected Date'),
			"fieldtype": 'Date'
		},
		{
			"fieldname" : "project_status",
			"label": __('Project Status'),
			"fieldtype": 'Data'
        //    "options": 'New\nWIP\nunder QA\nCompleted'
		},
		{
			"fieldname" : "user",
			"label": __('Total Count of Resources working in the project'),
			"fieldtype": 'Data'
			//"fieldtype": 'Link',
            //"options": 'ProjectTask'
		}
		


	]
};
