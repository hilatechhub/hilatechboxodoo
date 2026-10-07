def post_init_hook(cr, registry):
    """Create missing columns in res_company table after module installation."""

    # Column definitions with their defaults
    columns = {
        'theme_module_title_light': "VARCHAR DEFAULT '#1d1d1d'",
        'theme_module_title_dark': "VARCHAR DEFAULT '#ffffff'",
        'theme_module_title_shadow': "VARCHAR DEFAULT 'rgba(255, 255, 255, 0.6)'",
        'theme_btn_primary_bg': "VARCHAR DEFAULT '#0d6efd'",
        'theme_btn_primary_text': "VARCHAR DEFAULT '#ffffff'",
        'theme_btn_primary_hover': "VARCHAR DEFAULT '#0b5ed7'",
        'theme_btn_secondary_bg': "VARCHAR DEFAULT '#6c757d'",
        'theme_btn_secondary_text': "VARCHAR DEFAULT '#ffffff'",
        'theme_btn_secondary_hover': "VARCHAR DEFAULT '#5c636a'",
    }

    # Create columns if they don't exist
    for column_name, column_def in columns.items():
        try:
            cr.execute(f"""
                ALTER TABLE res_company
                ADD COLUMN IF NOT EXISTS {column_name} {column_def};
            """)
        except Exception as e:
            # Column might already exist, ignore error
            pass

    cr.commit()
