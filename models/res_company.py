# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _get_company(self):
        return self.env.user.company_id

    business_name = fields.Char(related='partner_id.business_name')
    code = fields.Char('Code')
    company_profile_id = fields.Many2one('microcredit.company.profile', required=True, string='Company profile')
    parent_id = fields.Many2one('res.company', 'Parent Company', index=True, default=_get_company)
    active = fields.Boolean('Active', default=True)
    status = fields.Char('Status', default='A')
    company_ids = fields.Many2many('res.company',
                                   relation='res_company_company_rel',
                                   column1='cid',
                                   column2='company_id')
    company_profile_alias = fields.Char(related='company_profile_id.alias', string='Company profile alias')
    ws_user = fields.Char('Web service user')
    ws_password = fields.Char('Web service password')
    commission_percent = fields.Float(string='Commission percent', digits=(2, 2))

