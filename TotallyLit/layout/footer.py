def render_footer(filepath: str, render_function_name: str = "render"):
    from ..util import execute_module

    execute_module(filepath, render_function_name)
