# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Kernet: Custom reports for Elon',
    'version': "14.0.1.0.1",
    'author': "Kernet Internet y Nuevas Tecnologías",
    'website': "http://www.kernet.es",
    'category': 'Personalizaciones Kernet',
    'depends': [
        'account',
    ],

    'data': [
        'data/mail_template_data.xml',
        'reports/report_invoice_document.xml',
        'reports/account_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
