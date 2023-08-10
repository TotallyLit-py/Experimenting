from .totallylit.app.app_and_page import App, Page  # noqa: F401
from .totallylit.decorators.page import (
    page_decorator_factory as __page_decorator_factory,
)
from .totallylit.layout.layout import LayoutRenderer


def __setup_app() -> App:
    import inspect
    import os

    from .totallylit.app.info import AppInfo
    from .totallylit.impl.app import TotallyLitApp

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
    return TotallyLitApp(app_info)


# TODO NOTE: this is going to need decorators on it, specifically @app.header
# and @app.title, so WRAP THIS.
app_and_page: App = __setup_app()

page = __page_decorator_factory(app_and_page)


def header():
    from .totallylit.layout.header import render_header

    render_header(app_and_page.info.get_header_path())


def footer():
    from .totallylit.layout.footer import render_footer

    render_footer(app_and_page.info.get_footer_path())


layout = LayoutRenderer(header, footer)
