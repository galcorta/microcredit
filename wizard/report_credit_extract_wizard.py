# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReportCreditExtractWizard(models.TransientModel):
    """
        Esta clase es para la generacion del reporte de extracto de creditos
    """
    _name = 'microcredit.report.credit.extract.wizard'
    _description = 'Reporte de extracto de creditos con un wizard'

    partner_ids = fields.Many2many('res.partner',
                                  'microcredit_report_credit_extract_wizard_partner_rel',
                                  'partner_id',
                                  'report_id',
                                  'Employees')
    date_from = fields.Datetime('Date from')
    date_to = fields.Datetime('Date to')


    def report_credit_extract_pdf(self, cr, uid, ids, data, context=None):
        if context is None:
            context = {}
