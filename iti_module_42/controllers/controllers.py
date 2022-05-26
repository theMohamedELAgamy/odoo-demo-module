# -*- coding: utf-8 -*-
# from odoo import http


# class ItiModule42(http.Controller):
#     @http.route('/iti_module_42/iti_module_42', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/iti_module_42/iti_module_42/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('iti_module_42.listing', {
#             'root': '/iti_module_42/iti_module_42',
#             'objects': http.request.env['iti_module_42.iti_module_42'].search([]),
#         })

#     @http.route('/iti_module_42/iti_module_42/objects/<model("iti_module_42.iti_module_42"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iti_module_42.object', {
#             'object': obj
#         })
