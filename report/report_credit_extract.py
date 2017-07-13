# -*- coding: utf-8 -*-
from odoo.report import report_sxw
from odoo.exceptions import UserError
from dateutil.parser import parse
import time


# class CreditExtracts(report_sxw.rml_parse):
#     def __init__(self, cr, uid, name, context):
#         super(CreditExtracts, self).__init__(cr, uid, name, context)


class CreditExtractWizard(models.AbstractModel):
    # _name='report.credit.extract.wizard.qweb'
    # _inherit='report.abstract_report'
    # _template='microcredit_portal.credit.extract.wizard.qweb'
    # _wrapped_report_class = CreditExtracts

    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_id'))
        sales_records = []
        credits = self.env['microcredit.trx.credit'].search([('dealer_partner_id', 'in', docs.partner_ids)])
        if docs.date_from and docs.date_to:
            for credit in credits:
                if parse(docs.date_from) <= parse(credit.create_date) and parse(docs.date_to) >= parse(
                        credit.create_date):
                    sales_records.append(credit)
                else:
                    raise UserError("Please enter duration")

        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': docs,
            'time': time,
            'orders': sales_records
        }
        return self.env['report'].render('microcredit_portal.credit_extract', docargs)