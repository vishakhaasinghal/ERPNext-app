# Copyright (c) 2023, vishakha singhal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
#from frappe import __


def execute(filters=None):
    if not filters: filters = {}
    data , columns = [], []
    columns = get_columns()
    data = get_cs_data(filters)

    return columns, data

def get_columns():
    return[
        {
            'fieldname' : "project_id",
            "label": ('Project Id'),
            'fieldtype' : 'Data',
            'width' : 150
        },
        {
            "fieldname" : "title_of_the_project",
            "label": ('Project Title'),
            "fieldtype": 'Data',
            'width' : 150
        },
        {
            "fieldname" : "start_date",
            "label": ('Project Start Date'),
            "fieldtype": 'Date',
            'width' : 150
        },
        {
            "fieldname" : "expected_end_date",
            "label": ('Project Expected Date'),
            "fieldtype": 'Date',
            'width' : 150
        },
        {
            "fieldname" : "project_status",
            "label": ('Project Status'),
            "fieldtype": 'Data',
            'width' : 150
        },
        {
            "fieldname" : "user",
            "label": ('Total Count of Resources working in the project'),
            "fieldtype": 'Data',
            #"fieldtype": 'Link',
            #"options": 'ProjectTask',
            'width' : 150
        }

    ]
    

# def get_cs_data(filters):
    #conditions = get_conditions(filters)
    #data = frappe.get_all(
    #	doctype= 'Project',
    #	fields= ['project_id', 'title_of_the_project', 'start_date', 'expected_end_date','project_status'],
    #	filters= conditions
    #)
    # data = frappe.db.sql("""select TP.project_id, TP.title_of_the_project, TP.start_date, TP.expected_end_date, TP.project_status, count(distinct TPR.user) 
    # 					from tabProject TP left outer join tabProjectResource TPR on TP.project_id = TPR.project_id group by project_id ;""" , filters , as_dict= 1)
    

    


    
# def get_cs_data(filters):
#     where_clause = ""
#     if filters.get('project_status'):
#         where_clause = "WHERE TP.project_status = '{0}'".format(filters['project_status'])
    
#     data = frappe.db.sql("""
#         SELECT TP.project_id, TP.title_of_the_project, TP.start_date, TP.expected_end_date, TP.project_status, 
#                COUNT(DISTINCT TPR.user)
#         FROM tabProject TP
#         LEFT OUTER JOIN tabProjectResource TPR ON TP.project_id = TPR.project_id
#         {0}
#         GROUP BY TP.project_id;
#         """.format(where_clause), as_dict=1)
    
#     return data

# def get_cs_data(filters):
#     where_conditions = []
#     if filters.get('project_id'):
#         where_conditions.append("TP.project_id = '{0}'".format(filters['project_id']))
    
#     if filters.get('title_of_the_project'):
#         where_conditions.append("TP.title_of_the_project LIKE '%{0}%'".format(filters['title_of_the_project']))

#     if filters.get('start_date'):
#         where_conditions.append("TP.start_date = '{0}'".format(filters['start_date']))

#     if filters.get('expected_end_date'):
#         where_conditions.append("TP.expected_end_date = '{0}'".format(filters['expected_end_date']))


#     if filters.get('project_status'):
#         where_conditions.append("TP.project_status = '{0}'".format(filters['project_status']))

#     where_clause = "WHERE " + " AND ".join(where_conditions) if where_conditions else ""

#     data = frappe.db.sql("""
#         SELECT TP.project_id, TP.title_of_the_project, TP.start_date, TP.expected_end_date, TP.project_status, 
#                COUNT(DISTINCT TPR.user)
#         FROM tabProject TP
#         LEFT OUTER JOIN tabProjectResource TPR ON TP.project_id = TPR.project_id
#         {0}
#         GROUP BY TP.project_id;
#         """.format(where_clause), as_dict=1)

#     return data


def get_cs_data(filters):
    where_conditions = []
    having_conditions = []

    if filters.get('project_id'):
        where_conditions.append("TP.project_id = '{0}'".format(filters['project_id']))

    if filters.get('title_of_the_project'):
        where_conditions.append("TP.title_of_the_project LIKE '%{0}%'".format(filters['title_of_the_project']))

    if filters.get('start_date'):
        where_conditions.append("TP.start_date = '{0}'".format(filters['start_date']))

    if filters.get('expected_end_date'):
        where_conditions.append("TP.expected_end_date = '{0}'".format(filters['expected_end_date']))

    if filters.get('project_status'):
        where_conditions.append("TP.project_status = '{0}'".format(filters['project_status']))

    if filters.get('user'):
        having_conditions.append("COUNT(DISTINCT TPTU.assigned_to) = {0}".format(filters['user']))

    where_clause = "WHERE " + " AND ".join(where_conditions) if where_conditions else ""
    having_clause = "HAVING " + " AND ".join(having_conditions) if having_conditions else ""

    data = frappe.db.sql("""
        SELECT TP.project_id, TP.title_of_the_project, TP.start_date, TP.expected_end_date, TP.project_status, 
               COUNT(DISTINCT TPTU.assigned_to) AS user
        FROM tabProject TP
        INNER JOIN tabProjectTask TPT ON TP.project_id = TPT.project_id
        INNER JOIN tabProjectTaskUser TPTU ON TPT.task_id = TPTU.parent AND TPTU.parenttype = 'ProjectTask'
        {0}
        GROUP BY TP.project_id
        {1};
        """.format(where_clause, having_clause), as_dict=1)

    return data



