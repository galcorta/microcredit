# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MicrocreditUserDevice(models.Model):
    _name = 'microcredit.user.device'

    name = fields.Char(related='msisdn', string='Name')
    msisdn = fields.Char('Mobile phone', unique=True)
    imei = fields.Char('IMEI')
    device_type = fields.Selection([
        ('POS_MACHINE', 'POS MACHINE'),
        ('MOBILE_PHONE', 'MOBILE PHONE'),
    ], 'Device type', default='POS_MACHINE')
    released = fields.Boolean('Released', default=True)
    active = fields.Boolean('Active', required=True, default=True)

    _sql_constraints = [
        ('msisdn_uniq', 'unique(msisdn)', 'The phone number must be unique per device!'),
    ]
