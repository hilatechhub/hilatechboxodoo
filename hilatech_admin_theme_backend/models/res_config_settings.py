from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    theme_favicon = fields.Binary('Favicon', related='company_id.theme_favicon', readonly=False)
    theme_login_bg = fields.Binary('Login Background', related='company_id.theme_login_bg', readonly=False)
    theme_home_bg = fields.Binary('Home Background', related='company_id.theme_home_bg', readonly=False)
    theme_home_overlay = fields.Boolean('Home Overlay', related='company_id.theme_home_overlay', readonly=False)
    theme_home_blur = fields.Boolean('Home Blur', related='company_id.theme_home_blur', readonly=False)

    # Module title color settings
    theme_module_title_light = fields.Char('Module Title Color (Light Mode)', related='company_id.theme_module_title_light', readonly=False)
    theme_module_title_dark = fields.Char('Module Title Color (Dark Mode)', related='company_id.theme_module_title_dark', readonly=False)
    theme_module_title_shadow = fields.Char('Module Title Shadow', related='company_id.theme_module_title_shadow', readonly=False)

    # Brand colors, sidebar image and buttons
    appbar_image = fields.Binary(related='company_id.appbar_image', readonly=False)
    theme_primary_color = fields.Char(related='company_id.theme_primary_color', readonly=False)
    theme_navbar_bg = fields.Char(related='company_id.theme_navbar_bg', readonly=False)
    theme_navbar_color = fields.Char(related='company_id.theme_navbar_color', readonly=False)
    theme_appbar_bg = fields.Char(related='company_id.theme_appbar_bg', readonly=False)
    theme_appbar_color = fields.Char(related='company_id.theme_appbar_color', readonly=False)
    theme_appbar_active = fields.Char(related='company_id.theme_appbar_active', readonly=False)
    theme_btn_primary_bg = fields.Char(related='company_id.theme_btn_primary_bg', readonly=False)
    theme_btn_primary_text = fields.Char(related='company_id.theme_btn_primary_text', readonly=False)
    theme_btn_primary_hover = fields.Char(related='company_id.theme_btn_primary_hover', readonly=False)
    theme_btn_secondary_bg = fields.Char(related='company_id.theme_btn_secondary_bg', readonly=False)
    theme_btn_secondary_text = fields.Char(related='company_id.theme_btn_secondary_text', readonly=False)
    theme_btn_secondary_hover = fields.Char(related='company_id.theme_btn_secondary_hover', readonly=False)
    theme_home_navbar_color = fields.Char(related='company_id.theme_home_navbar_color', readonly=False)
    theme_home_bg_light = fields.Binary(related='company_id.theme_home_bg_light', readonly=False)
    theme_login_footer = fields.Char(related='company_id.theme_login_footer', readonly=False)
