from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _post_logout(cls):
        super()._post_logout()
        request.future_response.set_cookie('color_scheme', max_age=0)

    def color_scheme(self):
        cookie_scheme = request.httprequest.cookies.get('color_scheme')
        scheme = cookie_scheme if cookie_scheme else super().color_scheme()
        if user := request.env.user:
            if user._is_public():
                return super().color_scheme()
            if user_scheme := user.res_users_settings_id.color_scheme:
                if user_scheme in ('light', 'dark'):
                    return user_scheme
        return scheme

    def session_info(self):
        result = super().session_info()
        if not self.env.user._is_public():
            # res.users.log gets one row per login (current one included)
            result['hl_login_count'] = self.env['res.users.log'].sudo().search_count(
                [('create_uid', '=', self.env.user.id)]
            )
        if self.env.user._is_internal():
            for company in self.env.user.company_ids.with_context(bin_size=True):
                result['user_companies']['allowed_companies'][company.id].update({
                    'has_appsbar_image': bool(company.appbar_image),
                })
        return result
