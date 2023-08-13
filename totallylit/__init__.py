# TODO switch things over to `from totallylit` if there's any chance they'll come from elsewhere

from totallylit.memoryx import (
    get_default_memory_service_instance as __memory_service_thingy,
)

from .app import AppContext as __AppContext
from .decorators import page_decorator_factory as __page_decorator_factory
from .impl import TotallyLitAppContext as __TotallyLitAppContext
from .version import VERSION  # noqa: F401

context: __AppContext = __TotallyLitAppContext.create_new_context()
page = __page_decorator_factory(context.app)
memory = __memory_service_thingy.memory

# SWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEET
#
# Let's set it up so that this file JUST loads extensions and you can
# register your OWN variables as `totallylit.X`
#
# if False:
#     global test_var
#     test_var: int = 42


def init() -> None:
    context.app.reset()
    context.app.reset()
    context.app.reset()
    context.app.reset()
