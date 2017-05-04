# -*- coding: utf-8 -*-
{
    'name': "Micro Credit Portal",

    'summary': """
        Micro Credit portal administration""",

    'description': """
        Portal for Micro Credit project administration.
    """,

    'author': "MenuMovil",
    'website': "http://www.menumovil.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Other',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'l10n_py_toponyms'],

    # always loaded
    'data': [
        'views/credit_extract_report.xml',
        'security/microcredit_portal_security.xml',
        'data/microcredit_portal_data.xml',
        'views/microcredit_portal_view.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/res_users_view.xml',
        'security/ir.model.access.csv',
        'microcredit_portal_report.xml',
        'views/trx_credit_view.xml',
        'views/trx_pay_view.xml',
        'views/res_bank_view.xml',
        'wizard/report_credit_extract_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'auto_install': False,

}
