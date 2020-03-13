# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'fcumple',
    'version': '1.0',
    'author': ['Santiago Preiato'],
    'category': 'Tools',
    'summary': 'Fecha Cumpleaños Cliente',
    'website': 'https://www.sgpgestion.com.ar',
    'description': """
Fecha Cumpleaños
======================
Con este módulo mostraremos Fecha Cumpleaños
    """,
    'depends': ['base'],
    'data': [
        'fcumple_view.xml',
    ],
    'installable': True,
    'auto_install': True,
}
