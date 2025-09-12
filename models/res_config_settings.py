from odoo import models,fields,api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_map_api_key = fields.Char(string="Google Map API Key",config_parameter="google_api_key")
