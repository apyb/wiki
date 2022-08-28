def template(app, docname: str, source: list[str]):
    content = source[0]
    if not content.startswith("!template"):
        return

    content = content.replace("!template", "", 1)
    print("*"*80)
    print(app.config.templates_context)
    rendered = app.builder.templates.render_string(content, app.config.templates_context)
    source[0] = rendered


def setup(app):
    app.add_config_value("templates_context", {}, "env")
    app.connect("source-read", template)
