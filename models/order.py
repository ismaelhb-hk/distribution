# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Order(models.Model):
    _name = 'distribution.order'
    _description = 'Distribution Order'

    # Order identifier or reference
    name = fields.Char(string='Order Reference', required=True, copy=False)

    date = fields.Datetime(string='Date', default=fields.Datetime.now, required=True)

    status = fields.Char(string='Status', default='pending', required=True)

    total = fields.Float(string='Total', compute='_compute_total')

    pay_method = fields.Char(string='Payment Method')

    address = fields.Text(string='Shipping Address')


    # Relationships (Foreign Keys)
    customer_id = fields.Many2one('res.users', string='Customer', required=True)
    administrator_ids = fields.Many2many('res.users', string='Administrators')
    item_ids = fields.One2many('distribution.item', 'order', string='Order Items')

    @api.depends('item_ids.price', 'item_ids.quantity')
#    def _compute_total(self):
#        for record in self:
#            record.total = sum(item.price * item.quantity for item in record.item_ids)