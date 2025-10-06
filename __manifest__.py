# -*- coding: utf-8 -*-
{
    'name': "Address Autocomplete Widget",

    'summary': "Google Map Address Autocomplete Widget",

    'description': """
        Enhances Odoo address fields with real-time Google Maps address suggestions, improving data entry accuracy and speed.
        Retrieves detailed address components and geocodes addresses.
        Features draggable map pin for precise location adjustment with automatic reverse geocoding.
        Requires a Google Maps API key.
    """,

     'author': "Dhrushil Butani",
    'maintainer': 'Dhrushil Butani',
    'category': 'Extra Tools',
    'version': '17.0.1.1',

    'depends': ['base','base_setup'],

    # always loaded
    'data': [
        'views/res_config_settings_view.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "address_autocomplete_gmap_widget/static/src/css/address_autocomplete.css",
            "address_autocomplete_gmap_widget/static/src/js/address_autocomplete.js",
            "address_autocomplete_gmap_widget/static/src/xml/address_autocomplete.xml",
        ]
    },

    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

