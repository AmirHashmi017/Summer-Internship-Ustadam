# -*- coding: utf-8 -*-
{
    'name': "JobApplicationForm",

    'summary': "To apply for different jobs online",

    'description': """
Long description of module's purpose
    """,

    'author': "Amir Hashmi",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/job_application_actions.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/jobapplication_views.xml',
        'views/job_application_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

