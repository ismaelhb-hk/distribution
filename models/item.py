# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Item(models.Model):
    _name = 'distribution.item'
    _description = 'distribution.item'

    name = fields.Char()
    quantity = fields.Integer()
    price = fields.Float()
    
   product = fields.Many2one('distribution.product')
   order = fields.Many2one('distribution.order')
   
