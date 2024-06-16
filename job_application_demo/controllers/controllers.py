# -*- coding: utf-8 -*-
# from odoo import http


# class ./addonsSincsol/jobApplicationDemo(http.Controller):
#     @http.route('/./addons_sincsol/job_application_demo/./addons_sincsol/job_application_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./addons_sincsol/job_application_demo/./addons_sincsol/job_application_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./addons_sincsol/job_application_demo.listing', {
#             'root': '/./addons_sincsol/job_application_demo/./addons_sincsol/job_application_demo',
#             'objects': http.request.env['./addons_sincsol/job_application_demo../addons_sincsol/job_application_demo'].search([]),
#         })

#     @http.route('/./addons_sincsol/job_application_demo/./addons_sincsol/job_application_demo/objects/<model("./addons_sincsol/job_application_demo../addons_sincsol/job_application_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./addons_sincsol/job_application_demo.object', {
#             'object': obj
#         })

