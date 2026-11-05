# -*- coding: utf-8 -*-
# from odoo import http


# class Distribution(http.Controller):
#     @http.route('/distribution/distribution', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/distribution/distribution/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('distribution.listing', {
#             'root': '/distribution/distribution',
#             'objects': http.request.env['distribution.distribution'].search([]),
#         })

#     @http.route('/distribution/distribution/objects/<model("distribution.distribution"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('distribution.object', {
#             'object': obj
#         })
