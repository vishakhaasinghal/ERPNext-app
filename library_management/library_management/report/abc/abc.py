# Copyright (c) 2023, vishakha and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals

def execute(filters=None):
	columns, data = [], []
	return columns, data

	columns = [
        {
            'fieldname': 'account',
            'label': _('Account'),
            'fieldtype': 'Link',
            'options': 'Account'
        },
        {
            'fieldname': 'currency',
            'label': _('Currency'),
            'fieldtype': 'Link',
            'options': 'Currency'
        },
        {
            'fieldname': 'balance',
            'label': _('Balance'),
            'fieldtype': 'Currency',
            'options': 'currency'
        }
    ]

	data = [
        {
            'account': 'Application of Funds (Assets)',
            'currency': 'INR',
            'balance': '15182212.738'
        },
        {
            'account': 'Current Assets - GTPL',
            'currency': 'INR',
            'balance': '17117932.738'
        },
    
    ]
