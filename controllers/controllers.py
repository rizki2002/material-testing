# -*- coding: utf-8 -*-
# from odoo import http


# class Testprogram(http.Controller):
#     @http.route('/testprogram/testprogram/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testprogram/testprogram/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testprogram.listing', {
#             'root': '/testprogram/testprogram',
#             'objects': http.request.env['testprogram.testprogram'].search([]),
#         })

#     @http.route('/testprogram/testprogram/objects/<model("testprogram.testprogram"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testprogram.object', {
#             'object': obj
#         })
