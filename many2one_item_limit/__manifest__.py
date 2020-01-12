# -*- coding: utf-8 -*-
{
    'name': "Many2one Item Limit",

    'summary': """
        Set limit of Many2one fields items""",

    'description': """
        This module allows you to set the numbers of items that will appear in Many2one fields
    """,

    'author': "Mamitiana RAHARIJAONA",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_setup'],

    # always loaded
    'data': [
        'data/config_data.xml',
        'views/views.xml',
        'views/manyone_item_limit_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
