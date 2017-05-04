# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    subsidiary = fields.Char('Subsidiary')
