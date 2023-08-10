import dataclasses as __dataclasses

from ..app import AppContext


@__dataclasses.dataclass
class TotallyLitAppContext(AppContext):
    def init(self):
        pass

    def setup_context(self):
        pass

    def reset_context(self):
        pass

    def create_new_context(
        user_application_folder: str = None,
    ) -> "TotallyLitAppContext":
        import os

        from ..app import AppInfo
        from ..util import get_calling_filename
        from .app import TotallyLitApp

        # This assumes that create_new_context() is called from a TotallyLit module
        # which is imported directly from the user's application!
        # - util get_calling_filename frame
        # - create_new_context frame
        # - TotallyLit module frame
        # - user's application frame
        if not user_application_folder:
            if calling_filename := get_calling_filename(4):
                user_application_folder = os.path.dirname(calling_filename)

        return TotallyLitAppContext(
            TotallyLitApp(AppInfo(root_folder=user_application_folder))
        )
