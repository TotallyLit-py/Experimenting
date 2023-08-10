def execute_module(
    filepath: str, entry_point_fn: str = None, module_name: str = "module"
):
    """
    Execute a module from a file.
    Can optionally specify an entry point function.
    """

    import importlib.util

    if spec := importlib.util.spec_from_file_location(module_name, filepath):
        try:
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
                if entry_point_fn and hasattr(module, entry_point_fn):
                    try:
                        getattr(module, entry_point_fn)()
                    except Exception as e:
                        print(f"Could not invoke {filepath}: {e}")
                        return
            except ImportError:
                print(f"Could not import {filepath}")
                return
            except Exception as e:
                print(f"Could not import {filepath}: {e}")
                return
        except ImportError:
            print(f"Could not import {filepath}")
            return
