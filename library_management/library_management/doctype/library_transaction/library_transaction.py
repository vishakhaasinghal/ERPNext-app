# Copyright (c) 2023, vishakha and contributors
# For license information, please see license.txt

# import frappe
#from frappe.model.document import Document

#class LibraryTransaction(Document):
#	pass




from __future__ import unicode_literals

import frappe
from frappe.model.document import Document

class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == 'Issue':
            self.validate_issue()
            # set the article status to be Issued
            article1 = frappe.get_doc('Article1', self.article1)
            article1.status = 'Issued'
            article1.save()

        elif self.type == 'Return':
            self.validate_return()
            # set the article status to be Available
            article1 = frappe.get_doc('Article1', self.article1)
            article1.status = 'Available'
            article1.save()

    def validate_issue(self):
        self.validate_membership()
        article1 = frappe.get_doc('Article1', self.article1)
        # article cannot be issued if it is already issued
        if article1.status == 'Issued':
            frappe.throw('Article is already issued by another member')

    def validate_return(self):
        article1 = frappe.get_doc('Article1', self.article1)
        # article cannot be returned if it is not issued first
        if article1.status == 'Available':
            frappe.throw('Article cannot be returned without being issued first')

    def validate_maximum_limit(self):
        max_articles = frappe.db.get_single_value('Library Settings', 'max_articles')
        count = frappe.db.count(
            'Library Transaction',
            {'library_member': self.library_member, 'type': 'Issue', 'docstatus': 1},
        )
        if count >= max_articles:
            frappe.throw('Maximum limit reached for issuing articles')

    def validate_membership(self):
        # check if a valid membership exist for this library member
        valid_membership = frappe.db.exists(
            'Library Membership',
            {
                'library_member': self.library_member,
                'docstatus': 1,
                'from_date': ('<', self.date),
                'to_date': ('>', self.date),
            },
        )
        if not valid_membership:
            frappe.throw('The member does not have a valid membership')