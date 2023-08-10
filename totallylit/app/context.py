import abc as __abc
import dataclasses as __dataclasses

from .app import App


@__dataclasses.dataclass
class AppContext(__abc.ABC):
    import abc as __abc

    app: App

    @__abc.abstractmethod
    def init() -> None:
        pass

    @__abc.abstractmethod
    def setup_context() -> None:
        pass

    @__abc.abstractmethod
    def reset_context() -> None:
        pass
        pass
