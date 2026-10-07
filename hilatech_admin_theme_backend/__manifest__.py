{
    'name': 'Odoo 19 Backend Theme - Enterprise-Grade Look for Community',
    'summary': 'Odoo 19 Community theme: Enterprise-style home menu, apps sidebar, responsive '
               'design, dark mode, branded login page, custom favicon and your own colors and backgrounds.',
    'description': """
Odoo 19 Backend Theme - Enterprise-Grade Interface for Odoo Community
=====================================================================

Give Odoo 19 Community an Enterprise-style backend and apply your own brand identity,
without writing code.

Key features
------------
* Enterprise-style full-screen home menu: instant search, keyboard navigation,
  drag-and-drop ordering saved per user.
* Apps sidebar: Large, Small or Invisible, chosen by each user, with an optional footer logo.
* Fully responsive: burger menu on mobile, adapted list, kanban and pivot views.
* Light and dark mode, selected per user.
* Brand identity: primary color, top bar, sidebar, primary and secondary button colors.
* Branded login page: your own background picture, company logo and footer text (default: Powered by Odoo).
* Custom favicon, per company.
* Optional free companion module hilatech_db_selector_logo: your logo on the database selection page.
* Home menu backgrounds: separate pictures for light and dark mode, with overlay and blur.
* Smart welcome card: avatar, name, date, live clock and a greeting that adapts to the user and the time.
* Per-company branding: favicon, backgrounds, colors and sidebar logo.
* Translated in English, French, German and Spanish.

Self-contained: do not install ica_web_responsive or muk_web_appsbar alongside it.

Keywords: Odoo 19 theme, backend theme, Odoo Community theme, Enterprise-like theme,
responsive theme, dark mode, apps sidebar, home menu, white label, custom branding.

Support: support@hilatech.co - https://hilatech.co
    """,
    'version': '19.0.1.1.2',
    'category': 'Themes/Backend',
    'license': 'LGPL-3',
    'author': 'HILATECH',
    'website': 'https://hilatech.co',
    'support': 'support@hilatech.co',
    'icon': '/hilatech_admin_theme_backend/static/description/icon.png',
    'images': [
        'static/description/banner.png',
        'static/description/img/screenshot_home_light.png',
        'static/description/img/screenshot_home_dark.png',
        'static/description/img/screenshot_login.png',
        'static/description/img/screenshot_sidebar_light.png',
        'static/description/img/screenshot_sidebar_dark.png',
        'static/description/img/screenshot_settings_identity.png',
        'static/description/img/screenshot_settings_colors.png',
        'static/description/img/screenshot_mobile_home.png',
        'static/description/img/screenshot_mobile_app.png',
    ],
    'price': 25.0,
    'currency': 'USD',
    # Self-contained: embeds the responsive/home-menu work inspired by ica_web_responsive
    # (IdeaCode Academy) and the apps sidebar inspired by muk_web_appsbar (MuK IT), both LGPL-3.
    'depends': ['web', 'base_setup'],
    'data': [
        'views/res_config_settings_view.xml',
        'views/res_users_view.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('after', 'web/static/src/scss/primary_variables.scss', 'hilatech_admin_theme_backend/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'hilatech_admin_theme_backend/static/src/scss/primary_variables.scss'),
            'hilatech_admin_theme_backend/static/src/scss/appsbar_variables.scss',
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'hilatech_admin_theme_backend/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'hilatech_admin_theme_backend/static/src/scss/bootstrap_overridden.scss'),
            'hilatech_admin_theme_backend/static/src/scss/appsbar_mixins.scss',
        ],
        'web.assets_frontend': [
            'hilatech_admin_theme_backend/static/src/scss/login_layout.scss',
            'hilatech_admin_theme_backend/static/src/webclient/home_menu/home_menu_background.scss',
            'hilatech_admin_theme_backend/static/src/webclient/navbar/navbar.scss',
        ],
        'web.assets_backend': [
            'hilatech_admin_theme_backend/static/src/scss/login_layout.scss',
            'hilatech_admin_theme_backend/static/src/scss/module_titles.scss',
            'hilatech_admin_theme_backend/static/src/webclient/**/*.scss',
            'hilatech_admin_theme_backend/static/src/views/**/*.scss',

            'hilatech_admin_theme_backend/static/src/core/**/*',
            'hilatech_admin_theme_backend/static/src/webclient/**/*.js',
            ('after', 'web/static/src/views/list/list_renderer.xml', 'hilatech_admin_theme_backend/static/src/views/list/list_renderer_desktop.xml'),
            'hilatech_admin_theme_backend/static/src/webclient/**/*.xml',
            'hilatech_admin_theme_backend/static/src/views/**/*.js',
            'hilatech_admin_theme_backend/static/src/views/**/*.xml',
            ('remove', 'hilatech_admin_theme_backend/static/src/views/pivot/**'),

            # Don't include dark mode files in light mode
            ('remove', 'hilatech_admin_theme_backend/static/src/**/*.dark.scss'),
        ],
        'web.assets_backend_lazy': [
            'hilatech_admin_theme_backend/static/src/views/pivot/**',
        ],
        'web.assets_backend_lazy_dark': [
            ('include', 'web.dark_mode_variables'),
            ('before', 'hilatech_admin_theme_backend/static/src/scss/bootstrap_overridden.scss', 'hilatech_admin_theme_backend/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss', 'hilatech_admin_theme_backend/static/src/scss/bs_functions_overridden.dark.scss'),
        ],
        'web.assets_web': [
            ('replace', 'web/static/src/main.js', 'hilatech_admin_theme_backend/static/src/main.js'),
        ],
        # ========= Dark Mode =========
        'web.dark_mode_variables': [
            ('before', 'hilatech_admin_theme_backend/static/src/scss/primary_variables.scss', 'hilatech_admin_theme_backend/static/src/scss/primary_variables.dark.scss'),
            ('before', 'hilatech_admin_theme_backend/static/src/**/*.variables.scss', 'hilatech_admin_theme_backend/static/src/**/*.variables.dark.scss'),
            ('before', 'hilatech_admin_theme_backend/static/src/scss/secondary_variables.scss', 'hilatech_admin_theme_backend/static/src/scss/secondary_variables.dark.scss'),
            ('after', 'hilatech_admin_theme_backend/static/src/scss/appsbar_variables.scss', 'hilatech_admin_theme_backend/static/src/scss/appsbar_variables.dark.scss'),
        ],
        'web.assets_web_dark': [
            ('include', 'web.dark_mode_variables'),
            ('before', 'hilatech_admin_theme_backend/static/src/scss/bootstrap_overridden.scss', 'hilatech_admin_theme_backend/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss', 'hilatech_admin_theme_backend/static/src/scss/bs_functions_overridden.dark.scss'),
            'hilatech_admin_theme_backend/static/src/**/*.dark.scss',
        ],
    },
    'installable': True,
    'application': False,
}
