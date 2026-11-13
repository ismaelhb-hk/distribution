# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    
    _name = 'distribution.product'
    _description = 'distribution.product'

    name = fields.Char()
    price = fields.Float()
    stock = fields.Integer()
    category = fields.Char()
    description = fields.Text()
    brand = fields.Char()

    items = fields.One2many('distribution.item', 'product_id')
