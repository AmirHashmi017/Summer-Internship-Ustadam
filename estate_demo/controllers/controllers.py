# -*- coding: utf-8 -*-
# from odoo import http


# class ./addonsSincsol/estateDemo(http.Controller):
#     @http.route('/./addons_sincsol/estate_demo/./addons_sincsol/estate_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./addons_sincsol/estate_demo/./addons_sincsol/estate_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./addons_sincsol/estate_demo.listing', {
#             'root': '/./addons_sincsol/estate_demo/./addons_sincsol/estate_demo',
#             'objects': http.request.env['./addons_sincsol/estate_demo../addons_sincsol/estate_demo'].search([]),
#         })

#     @http.route('/./addons_sincsol/estate_demo/./addons_sincsol/estate_demo/objects/<model("./addons_sincsol/estate_demo../addons_sincsol/estate_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./addons_sincsol/estate_demo.object', {
#             'object': obj
#         })

