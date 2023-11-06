# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Autonsi Standard 2',
    'version': '15.0.1.0.0',
    "category": "Themes/Backend",
    'live_test_url': 'https://youtu.be/IhI7TpOAAKg',
    'sequence': 1,
    'summary': """
       Standard

    """,
    'author': 'NEWAY Solutions',
    'maintainer': 'NEWAY Solutions',
    'price': '150.0',
    'currency': 'EUR',
    'website': 'https://neway-solutions.com',
    'license': 'OPL-1',
    'images': [
        'static/description/wallpaper.png'
    ],
    'depends': [
        'web', "hr_skills", "base", "stock", "mrp"
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/employee.xml',
        'views/supplier.xml',
        'views/line.xml',
        'views/mold.xml',
        'views/common.xml',
        'views/product.xml',
        'views/location.xml',
        'views/blade.xml',
        'views/bom.xml',
    ],

}
