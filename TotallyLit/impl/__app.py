from dataclasses import dataclass

from ..app import App as __App


@dataclass
class TotallyLitApp(__App):
    from dataclasses import field

    from ..app import Page
    from ..app.info import AppInfo

    _pages_by_name: dict[str, Page] = field(default_factory=dict)

    info: AppInfo = None

    @property
    def pages(self) -> list[Page]:
        return sorted(self._pages_by_name.values(), key=lambda p: p.order)

    def get_page(self, name: str) -> Page:
        return self._pages_by_name[name]

    def add_page(
        self, name: str, title: str = None, icon: str = None, order: int = 0
    ) -> Page:
        from ..impl.__page import TotallyLitPage

        page = TotallyLitPage(name, title, icon, order)
        self._pages_by_name[name] = page
        return page

    def remove_page(self, name: str) -> None:
        del self._pages_by_name[name]

    def add_page_from_function(
        self, function: callable, title: str = None, icon: str = None, order: int = 0
    ) -> Page:
        from ..impl.__page import TotallyLitPage

        page = TotallyLitPage.from_function(self, function, title, icon, order)
        self._pages_by_name[page.name] = page
        return page

    def reset(self) -> None:
        self._pages_by_name = dict()
