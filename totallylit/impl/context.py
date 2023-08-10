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
