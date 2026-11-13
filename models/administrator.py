# -*- coding: utf-8 -*-

from odoo import models, fields


class Administrator(models.Model):
    _inherit = 'res.users'

    # Orders managed by the administrator
    managed_order_ids = fields.Many2many('distribution.order', string='Managed Orders')