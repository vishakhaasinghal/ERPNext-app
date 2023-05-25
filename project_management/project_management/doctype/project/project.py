# Copyright (c) 2023, vishakha singhal and contributors
# For license information, please see license.txt

#from __future__ import unicode_literals
import frappe

from frappe.model.document import Document
from frappe.model.naming import getseries
from frappe.model.naming import make_autoname
from frappe.utils import getdate

#import frappe

class Project(Document):
	#pass
	def before_save(self):
		self.validate_project()
		self.project_id = self.name
		#frappe.msgprint('vis' + format(self.project_id))
		#frappe.msgprint('vis1',self.name)
	
	
	def on_submit(self):
		self.validate_project()
	#	self.project_id = self.name

		#frappe.msgprint('vishakha',self.project_id,self.name)

	def validate_project(self):
		# check if a valid membership exist for this library member
		finstartdate = frappe.db.get_single_value('ProjectFinancial', 'finstartdate')
		finenddate = frappe.db.get_single_value('ProjectFinancial', 'finenddate')
		if (getdate(self.start_date) > finstartdate) & (getdate(self.start_date) < finenddate):
			pass
		else:
			frappe.throw('The date is not in between financial year date')
	pass
	