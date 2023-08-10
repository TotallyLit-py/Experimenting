from abc import ABC as __ABC
from dataclasses import dataclass

# Abstract base classes for App and Page
# (mostly to more easily reference them from everywhere without circular references)
#
# See __app and __page for concrete implementations
#
# These are together in the same file because one referencs the other
# but really these should be imported from `TotallyLit`


# Forward declaration
class Page(__ABC):
    pass


@dataclass
class App(__ABC):
    from abc import abstractmethod

    from .info import AppInfo

    info: AppInfo

    @abstractmethod
    def pages(self) -> list[Page]:
        pass

    @abstractmethod
    def get_page(self, name: str) -> Page:
        pass

    @abstractmethod
    def add_page(
        self, name: str, title: str = None, icon: str = None, order: int = 0
    ) -> Page:
        pass

    @abstractmethod
    def remove_page(self, name: str) -> None:
        pass

    @abstractmethod
    def add_page_from_function(
        self, function: callable, title: str = None, icon: str = None, order: int = 0
    ) -> Page:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass


@dataclass
class Page(__ABC):
    from abc import abstractmethod
    from pathlib import Path as Path

    app: App
    name: str
    title: str = None
    icon: str = None
    order: int = 0
    function: callable = None
    file_path: Path = None
