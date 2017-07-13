# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CompanyProfile(models.Model):
    _name = 'microcredit.company.profile'

    alias = fields.Char('Alias', unique=True)
    name = fields.Char('Name', unique=True)


class PurchaseOrder(models.Model):
    _name = 'microcredit.purchase.order'

    company_id = fields.Many2one('res.company', required=True, string='Distributor company')
    amount = fields.Float(string='Amount', digits=(14, 2), required=True)
    invoice_number = fields.Char('Invoice number')


class OperationType(models.Model):
    _name = 'microcredit.operation.type'

    alias = fields.Char('Alias', unique=True)
    description = fields.Char('Description')


class TrxParam(models.Model):
    _name = 'microcredit.trx.param'

    alias = fields.Char('Alias', unique=True)
    interest = fields.Float('Interest', digits=(4, 2))
    interest_on_arrears = fields.Float('Interest on arrears', digits=(4, 2))


class TrxStatus(models.Model):
    _name = 'microcredit.trx.status'

    code = fields.Char('Code')
    alias = fields.Char('Alias', unique=True)
    description = fields.Char('Description')
    approved = fields.Boolean('Approved')
    name = fields.Char(related='description', string='Name')


class TrxToken(models.Model):
    _name = 'microcredit.trx.token'

    name = fields.Char('Trx Token')
    expire_date = fields.Datetime('Expire date')
    active = fields.Boolean('Active', default=True)


class TrxCredit(models.Model):
    _name = 'microcredit.trx.credit'

    dealer_partner_id = fields.Many2one('res.partner', string='Dealer partner')
    operation_type_id = fields.Many2one('microcredit.operation.type', string='Operation type')
    purchase_order_id = fields.Many2one('microcredit.purchase.order', string='Purchase order')
    credit_entity_company_id = fields.Many2one('res.company', string='Credit entity company')
    trx_status_id = fields.Many2one('microcredit.trx.status', string='Transaction status')
    trx_param_id = fields.Many2one('microcredit.trx.param', string='Transaction parameter')
    pos_employee_partner_id = fields.Many2one('res.partner', string='Pos employee partner')
    reference = fields.Char('Reference')
    trx_revert = fields.Integer('Trx revert')
    trx_commission = fields.Integer('Trx commission')
    trx_extern = fields.Integer('Bank Transaction ID')
    amount = fields.Float(string='Amount', digits=(14, 2), required=True)
    commission = fields.Float(string='Commission', digits=(14, 2), required=True)
    source = fields.Char('Source')
    trx_token_id = fields.Many2one('microcredit.trx.token')
    user_device_id = fields.Many2one('microcredit.user.device')

    pos_company_id = fields.Many2one(related='pos_employee_partner_id.company_id', string='POS Company')
    distributor_company_id = fields.Many2one('res.company', related='purchase_order_id.company_id')
    dealer_partner_name = fields.Char(related='dealer_partner_id.name', string='Dealer')


class TrxPay(models.Model):
    _name = 'microcredit.trx.pay'

    collector_partner_id = fields.Many2one('res.partner', string='Collector partner')
    operation_type_id = fields.Many2one('microcredit.operation.type', string='Operation type')
    credit_entity_company_id = fields.Many2one('res.company', string='Credit entity company')
    trx_status_id = fields.Many2one('microcredit.trx.status', string='Transaction status')
    trx_param_id = fields.Many2one('microcredit.trx.param', string='Transaction parameter')
    company_id = fields.Many2one('res.company', string='POS Company')
    reference = fields.Char('Reference')
    trx_revert = fields.Integer('Trx revert')
    trx_extern = fields.Integer('Bank Transaction ID')
    amount = fields.Float(string='Amount', digits=(14, 2), required=True)
    interest = fields.Float(string='Interest', digits=(14, 2))
    trx_credit_ids = fields.Many2many('microcredit.trx.credit', relation='microcredit_debt')
    user_device_id = fields.Many2one('microcredit.user.device')

    collector_partner_name = fields.Char(related='collector_partner_id.name', string='Collector')


class ResponseCode(models.Model):
    _name = 'microcredit.response.code'

    code = fields.Char('Code')
    success = fields.Boolean('Success')
    description = fields.Char('Description')


class TrxCreditDetail(models.Model):
    _name = 'microcredit.trx.credit.detail'

    trx_credit_id = fields.Many2one('microcredit.trx.credit')
    trx_status_id = fields.Many2one('microcredit.trx.status', string='Transaction status')
    response_code_id = fields.Many2one('microcredit.response.code', string='Response code')
    date_request = fields.Datetime('Date request')
    date_response = fields.Datetime('Date response')
    description = fields.Char('Description')


class TrxPayDetail(models.Model):
    _name = 'microcredit.trx.pay.detail'

    trx_pay_id = fields.Many2one('microcredit.trx.pay')
    trx_status_id = fields.Many2one('microcredit.trx.status', string='Transaction status')
    response_code_id = fields.Many2one('microcredit.response.code', string='Response code')
    date_request = fields.Datetime('Date request')
    date_response = fields.Datetime('Date response')
    description = fields.Char('Description')


class MessageTemplate(models.Model):
    _name = 'microcredit.message.template'

    alias = fields.Char('Template alias', unique=True)
    template = fields.Char('Template')


class Sms(models.Model):
    _name = 'microcredit.sms'
    user_id = fields.Many2one('res.users', string='Target user')
    message_template = fields.Many2one('microcredit.message.template', string='Message template')
    message_type = fields.Char('Message type')
    target_type = fields.Char('Target type')
    delivered = fields.Boolean('Delivered')
    date_delivered = fields.Datetime('Date delivered')
    response_code = fields.Integer('Response code')
    message_id = fields.Char('Message ID')
    reference = fields.Char('Reference')


class SysSetting(models.Model):
    _name = 'microcredit.sys.setting'

    sys_key = fields.Char('Sys key', required=True)
    sys_value = fields.Char('Sys value')
    description = fields.Char('Description')
    active = fields.Boolean('Active')
