# -*- coding: utf-8 -*-

from odoo import models, fields


class Customer(models.Model):
    _inherit = 'res.users'

    # Orders placed by the customer 
    order_ids = fields.One2many('distribution.order', 'customer_id', string='Orders')