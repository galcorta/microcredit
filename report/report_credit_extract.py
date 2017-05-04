# -*- coding: utf-8 -*-
from odoo.report import report_sxw


class CreditExtracts(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(ReportCreditExtracts, self).__init__(cr, uid, name, context)


class CreditExtractWizard(models.AbstractModel):
    _name='report.credit.extract.wizard.qweb'
    _inherit='report.abstract_report'
    _template='microcredit_portal.credit.extract.wizard.qweb'
    _wrapped_report_class = CreditExtracts