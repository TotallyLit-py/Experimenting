from .app import App


def __setup_app():
    import inspect
    import os

    from .app.info import AppInfo

    # Get the calling file, skipping TotallyLit and importlib stack frames
    calling_filename: str = None
    for frame in range(2, 20):
        try:
            calling_filename = inspect.stack()[frame].filename
            if calling_filename.endswith("app.py"):
                break
        except IndexError:
            break

    if calling_filename is None:
        raise RuntimeError("Could not find the calling file for TotallyLit app")

    app_info = AppInfo(os.path.dirname(calling_filename))
    return App(app_info)


app: App = __setup_app()


def header():
    from .layout.header import render_header

    render_header(app.info.get_header_path())


def footer():
    from .layout.footer import render_footer

    render_footer(app.info.get_footer_path())
