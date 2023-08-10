from typing import Type as __Type

from ..app import App


class PageDecorator:
    __app: App = None
    _static_app: App = None

    def __init__(self, app: App):
        self.__app = app

    def __call__(cls, title: str = None, icon: str = None, order: int = 0):
        if callable(title):
            cls._static_app.add_page_from_function(title)

        def decorator(func):
            cls._static_app.add_page_from_function(func, title, icon, order)
            return func

        return decorator


__page_decorator_class_counter: int = 0


def __create_page_decorator_class(app: App) -> __Type[PageDecorator]:
    global __page_decorator_class_counter
    __page_decorator_class_counter += 1
    page_decorator_class = type(
        f"PageDecorator_{__page_decorator_class_counter}", (PageDecorator,), {}
    )
    page_decorator_class._static_app = app
    return page_decorator_class


def page_decorator_factory(app: App) -> PageDecorator:
    return __create_page_decorator_class(app)(app)
