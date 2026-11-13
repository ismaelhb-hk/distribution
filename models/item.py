# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Item(models.Model):
    _name = 'distribution.item'
    _description = 'Distribution Order Item'

    name = fields.Char(string='Description')

    quantity = fields.Integer(string='Quantity', default=1, required=True)

    price = fields.Float(string='Unit Price', required=True)


    # Relationships (Foreign Keys)
    order = fields.Many2one('distribution.order')

    product_id = fields.Many2one('distribution.product')

