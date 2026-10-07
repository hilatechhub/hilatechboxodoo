from odoo import fields, models


class HilatechThemeSettings(models.Model):
    _name = 'hilatech.theme.settings'
    _description = 'Theme Settings'

    footer_text = fields.Char('Footer Text', default='Powered by Odoo', help='Text shown at bottom of login page')
