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

    @api.multi
    def check_report(self):
        data = {}
        data['form'] = self.read(['partner_ids', 'date_from', 'date_to'])[0]
        return self._print_report(data)

    def _print_report(self, data):
        data['form'].update(self.read(['partner_ids', 'date_from', 'date_to'])[0])
        return self.env['report'].get_action(self, 'microcredit_portal.credit_extract', data=data)

    # @api.multi
    # def report_credit_extract_pdf(self):
    #     # self.ensure_one()
    #     data = {}
    #     data['ids'] = self.env.context.get('active_ids', [])
    #     data['model'] = self.env.context.get('active_model', 'ir.ui.menu')
    #     data['form'] = self.read(['date_from', 'date_to', 'partner_ids'])[0]
    #     used_context = self._build_contexts(data)
    #     data['form']['used_context'] = dict(used_context, lang=self.env.context.get('lang', 'en_US'))
    #     return self.env['report'].with_context(landscape=True)\
    #         .get_action(self, 'microcredit_portal.report_credit_extract_wizard', data=data)
