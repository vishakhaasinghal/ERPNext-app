# Copyright (c) 2023, vishakha singhal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.naming import getseries
from frappe.model.naming import make_autoname

class ProjectTask(Document):
    def autoname(self):
        # select a project name based on customer
        #prefix = '{project_id}-T'.format(self.project_id)
        prefix = "{}".format(self.project_id) + "-T-"
        self.name = prefix + getseries(prefix, 4)
        #frappe.msgprint(self.project_id)
        #self.name = make_autoname(self.project_id + "-T-" + ".####")
        self.task_id = self.name
        #frappe.msgprint(self.name)


    
    def before_save(self):
        self.validate_project_task()
        #frappe.msgprint('Vishakha')


    def validate_project_task(self):
        # check if a valid membership exist for this library member
        #finstartdate = frappe.db.get_single_value('ProjectFinance', 'finstartdate')
        #finenddate = frappe.db.get_single_value('ProjectFinance', 'finenddate')
        valid_project_task = frappe.db.exists(
            'Project',
            {
                'project_id': self.project_id,
                'docstatus': 1,
                'start_date': ('<', self.task_start_date),
                'expected_end_date': ('>', self.task_end_date)
            }
        )
        #frappe.msgprint(format(valid_project_task))
        if not valid_project_task:
            frappe.throw('The date is not in between the project date')

        #start_date = frappe.db.get_single_value('Project', 'start_date')
        #expected_end_date = frappe.db.get_single_value('Project', 'expected_end_date')


