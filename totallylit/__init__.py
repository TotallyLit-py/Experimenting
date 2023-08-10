from .app import AppContext as __AppContext
from .decorators import page_decorator_factory as __page_decorator_factory
from .impl import TotallyLitApp as __TotallyLitApp
from .impl import TotallyLitAppContext as __TotallyLitAppContext
from .version import VERSION  # noqa: F401

context: __AppContext = __TotallyLitAppContext.create_new_context()
page = __page_decorator_factory(context.app)


def init() -> None:
    context.app.reset()
