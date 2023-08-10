import abc as __abc
import dataclasses as __dataclasses

# Abstract base classes for App and Page
# (mostly to more easily reference them from everywhere without circular references)
#
# See __app and __page for concrete implementations
#
# These are together in the same file because one referencs the other
# but really these should be imported from `TotallyLit`


@__dataclasses.dataclass
class App(__abc.ABC):
    import abc as __abc

    from .info import AppInfo

    info: AppInfo
    title: str = None
    icon: str = None

    @property
    @__abc.abstractmethod
    def pages(self) -> list["Page"]:
        pass

    @__abc.abstractmethod
    def get_page(self, name: str) -> "Page":
        pass

    @__abc.abstractmethod
    def add_page(
        self, name: str, title: str = None, icon: str = None, order: int = 0
    ) -> "Page":
        pass

    @__abc.abstractmethod
    def remove_page(self, name: str) -> None:
        pass

    @__abc.abstractmethod
    def add_page_from_function(
        self, function: callable, title: str = None, icon: str = None, order: int = 0
    ) -> "Page":
        pass

    @__abc.abstractmethod
    def reset(self) -> None:
        pass


@__dataclasses.dataclass
class Page(__abc.ABC):
    import abc as __abc
    import pathlib as __pathlib

    app: App
    name: str
    title: str = None
    icon: str = None
    order: int = 0
    function: callable = None
    file_path: __pathlib.Path = None
