   # -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _inherit = 'res.users'
    _description = fields.Char(default="Extended")
    
    orders = fields.One2many('distribution.order','order_id')

