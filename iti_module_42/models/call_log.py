# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api

class Package(models.Model):
    _name='iti.package'
    _description='Call packeges'

    name=fields.Char()
    price=fields.Float()
    type=fields.Selection(selection=[
        ('unit','Unit'),
        ('flex','Flex')
    ],default='unit')




class CallLog(models.Model):
    _name = 'iti.call.log'
    _description = 'iti_module_42.iti_module_42'
    _rec_name='timestamp'
    customer=fields.Char()
    timestamp=fields.Datetime()
    from_number=fields.Char(string='From')
    to_number=fields.Char(string='To')
    duration=fields.Integer()
    price=fields.Float(compute='_compute_price',store='true')
    notes=fields.Text()
    package_id=fields.Many2one(comodel_name='iti.package')



    @api.depends('duration','package_id')
    def _compute_price(self):
        for rec in self  :
            rec.price=(rec.duration/60.0) * rec.package_id.price


    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
