from odoo import fields, models

# Company branding fields (name -> label). Empty value = keep Odoo/theme default.
THEME_COLOR_FIELDS = {
    'theme_primary_color': 'Primary Color',
    'theme_navbar_bg': 'Navbar Background',
    'theme_navbar_color': 'Navbar Text Color',
    'theme_appbar_bg': 'Sidebar Background',
    'theme_appbar_color': 'Sidebar Text Color',
    'theme_appbar_active': 'Sidebar Active/Hover Color',
}


class ResCompany(models.Model):
    _inherit = 'res.company'

    theme_favicon = fields.Binary('Favicon', attachment=True)
    theme_login_bg = fields.Binary('Login Background', attachment=True)
    theme_home_bg = fields.Binary('Home Menu Background (Dark Mode)', attachment=True)
    theme_home_bg_light = fields.Binary('Home Menu Background (Light Mode)', attachment=True)
    theme_home_overlay = fields.Boolean('Home Overlay', default=False)
    theme_home_blur = fields.Boolean('Home Blur', default=False)
    appbar_image = fields.Binary('Apps Menu Footer Image', attachment=True)
    theme_login_footer = fields.Char(
        'Login Footer Text',
        default='Powered by Odoo',
        help='Text shown at the bottom of the login page. Leave empty to keep the default "Powered by Odoo".',
    )

    # Module title colors
    theme_module_title_light = fields.Char('Module Title Color (Light Mode)', default='#1d1d1d')
    theme_module_title_dark = fields.Char('Module Title Color (Dark Mode)', default='#ffffff')
    theme_module_title_shadow = fields.Char('Module Title Shadow', default='rgba(255, 255, 255, 0.6)')

    # Brand colors
    theme_primary_color = fields.Char(THEME_COLOR_FIELDS['theme_primary_color'])
    theme_navbar_bg = fields.Char(THEME_COLOR_FIELDS['theme_navbar_bg'])
    theme_navbar_color = fields.Char(THEME_COLOR_FIELDS['theme_navbar_color'])
    theme_home_navbar_color = fields.Char(
        'Navbar Text on Home Menu',
        help='Text color of the top bar over the home menu background, in both modes. '
             'Leave empty for black in light mode and white in dark mode.',
    )
    theme_appbar_bg = fields.Char(THEME_COLOR_FIELDS['theme_appbar_bg'])
    theme_appbar_color = fields.Char(THEME_COLOR_FIELDS['theme_appbar_color'])
    theme_appbar_active = fields.Char(THEME_COLOR_FIELDS['theme_appbar_active'])

    # Buttons (columns already created by migrations 19.0.1.0.1/2)
    theme_btn_primary_bg = fields.Char('Primary Button Background')
    theme_btn_primary_text = fields.Char('Primary Button Text')
    theme_btn_primary_hover = fields.Char('Primary Button Hover')
    theme_btn_secondary_bg = fields.Char('Secondary Button Background')
    theme_btn_secondary_text = fields.Char('Secondary Button Text')
    theme_btn_secondary_hover = fields.Char('Secondary Button Hover')
