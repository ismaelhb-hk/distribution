# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Order(models.Model):
    _name = 'distribution.order'
    _description = 'distribution.order'

# Identificador o referencia de la orden
    name = fields.Char(string='Referencia de Orden', required=True, copy=False, default=lambda self: 'New')


    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now, required=True)

    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    ], string='Estado', default='pendiente', required=True)

    total = fields.Float(string='Total', compute='_compute_total', store=True)

    metodo_pago = fields.Char(string='Método de Pago')

    direccion_envio = fields.Text(string='Dirección de Envío')

    # Clave foránea al cliente (si el cliente es un res.partner de Odoo o un modelo propio)
    id_cliente = fields.Many2one('res.partner', string='Cliente', required=True)

    # Conexión con los ítems (esto se conecta con el archivo que hará tu compañero del ítem)
    item_ids = fields.One2many('distribution.order.item', 'id_orden', string='Líneas de Pedido')

    @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
