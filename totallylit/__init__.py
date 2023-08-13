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

__pyi_content: str = """
"""


def init() -> None:
    context.app.reset()
    context.app.reset()
    context.app.reset()
    context.app.reset()


def print_globals_from_extension(extension_pattern, module_path):
    import importlib
    import re

    import pkg_resources

    global __pyi_content

    for dist in pkg_resources.working_set:
        if re.match(extension_pattern, dist.key):
            try:
                # Import the specific module
                module = importlib.import_module(module_path)

                # Print the global variables
                print(f"Global variables from {dist.key}:")
                for key, value in module.__dict__.items():
                    if not key.startswith("__"):
                        print(f"  {key}: {value}")
                        globals()[key] = value
                        __pyi_content += f"{key}: {type(value).__name__}\n"
            except ModuleNotFoundError:
                print(f"Couldn't find module {module_path} in {dist.key}")


extension_pattern = r"totallylit-.*"
module_path = "totallylit.extensions.foo"
print_globals_from_extension(extension_pattern, module_path)

with open(__file__ + "i", "w") as f:
    f.write(__pyi_content)
