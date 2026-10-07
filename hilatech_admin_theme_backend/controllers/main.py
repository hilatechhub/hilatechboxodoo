import base64
from odoo import http
from odoo.http import request
from odoo.tools.mimetypes import guess_mimetype


class HilatechTheme(http.Controller):

    @staticmethod
    def _is_dark():
        return request.env['ir.http'].color_scheme() == 'dark'

    @staticmethod
    def _image_response(data, default_mimetype='image/jpeg'):
        """Serve a base64 image with its real mimetype; revalidate so a new upload shows up at once."""
        raw = base64.b64decode(data)
        mimetype = guess_mimetype(raw, default=default_mimetype)
        return request.make_response(raw, [
            ('Content-Type', mimetype),
            ('Cache-Control', 'no-cache'),
        ])

    @http.route('/hilatech/theme/login_bg', type='http', auth='public', csrf=False)
    def login_bg(self):
        c = request.env.company.sudo()
        if c.theme_login_bg:
            return self._image_response(c.theme_login_bg)
        return request.not_found()

    @http.route('/hilatech/theme/home_bg', type='http', auth='user', csrf=False)
    def home_bg(self):
        c = request.env.company.sudo()
        data = c.theme_home_bg if self._is_dark() else c.theme_home_bg_light
        if data:
            return self._image_response(data)
        return request.not_found()

    @http.route('/hilatech/theme/favicon', type='http', auth='public', csrf=False)
    def favicon(self):
        c = request.env.company.sudo()
        if c.theme_favicon:
            return self._image_response(c.theme_favicon, 'image/x-icon')
        return request.redirect('/web/static/img/favicon.ico')

    @http.route('/hilatech/theme/module_colors.css', type='http', auth='public', csrf=False)
    def module_colors_css(self):
        c = request.env.company.sudo()

        # Titles follow the Odoo color scheme (not the OS one): black in light, white in dark
        if self._is_dark():
            title = c.theme_module_title_dark or '#ffffff'
            shadow = 'rgba(0, 0, 0, 0.5)'
        else:
            title = c.theme_module_title_light or '#1d1d1d'
            shadow = c.theme_module_title_shadow or 'rgba(255, 255, 255, 0.6)'

        css = f"""
/* Dynamic Module Title Colors */
.o_home_menu .o_app .o_caption {{
    color: {title} !important;
    text-shadow: 0 1px 2px {shadow};
}}
"""
        css += self._brand_css(c)
        return request.make_response(css, [('Content-Type', 'text/css; charset=utf-8')])

    @staticmethod
    def _brand_css(company):
        """CSS for the optional brand colors; a color left empty emits nothing."""
        rules = []

        def add(selector, **props):
            body = ''.join(f'{k.replace("_", "-")}: {v} !important;' for k, v in props.items() if v)
            if body:
                rules.append(f'{selector} {{ {body} }}')

        def var(name, value):
            return f'--{name}: {value};' if value else ''

        root_vars = ''.join([
            var('hl-appbar-bg', company.theme_appbar_bg),
            var('hl-appbar-color', company.theme_appbar_color),
            var('hl-appbar-active', company.theme_appbar_active or company.theme_primary_color),
            var('bs-primary', company.theme_primary_color),
            var('NavBar-menuToggle-color', company.theme_primary_color),
        ])
        if root_vars:
            rules.append(f':root, body {{ {root_vars} }}')
        add('.o_main_navbar', background_color=company.theme_navbar_bg, color=company.theme_navbar_color)
        add('.o_main_navbar .o_menu_brand, .o_main_navbar .o_nav_entry, .o_main_navbar .dropdown-toggle, '
            '.o_main_navbar .o_menu_systray .o-dropdown > button', color=company.theme_navbar_color)
        home_color = company.theme_home_navbar_color
        if home_color:
            sel = 'body.o_home_menu_background .o_main_navbar'
            add(f'{sel}, {sel} .o_menu_systray, {sel} .o_menu_systray .o-dropdown > button, '
                f'{sel} .o_menu_systray .o_nav_entry, {sel} .o_menu_systray i, {sel} .o_menu_systray span:not(.badge), '
                f'{sel} .o_user_menu, {sel} .o_menu_toggle, {sel} .o_menu_brand', color=home_color)
        add('.btn-primary', background_color=company.theme_btn_primary_bg or company.theme_primary_color,
            border_color=company.theme_btn_primary_bg or company.theme_primary_color,
            color=company.theme_btn_primary_text)
        add('.btn-primary:hover, .btn-primary:focus', background_color=company.theme_btn_primary_hover,
            border_color=company.theme_btn_primary_hover)
        add('.btn-secondary', background_color=company.theme_btn_secondary_bg,
            border_color=company.theme_btn_secondary_bg, color=company.theme_btn_secondary_text)
        add('.btn-secondary:hover, .btn-secondary:focus', background_color=company.theme_btn_secondary_hover,
            border_color=company.theme_btn_secondary_hover)
        if not rules:
            return ''
        return '\n/* Brand colors */\n' + '\n'.join(rules) + '\n'
