# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Backend Exam Module",
    'version': '16.0.0.0.1',
    'summary': 'Back-end Practical Exam',
    'author': 'Ramiz Belim',
    'sequence': 10,
    'description': """ Batch-3, 2023 Back-end Practical Exam  """,
    'category': 'Accounting',
    'depends': ['sale_management','mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/quotation_bulk_upload_wizard_views.xml',
        'data/ir_cron_data.xml',
        'data/mail_template_data.xml',
        'views/sale_order_views.xml',
        'views/res_config_settings_views.xml'
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
