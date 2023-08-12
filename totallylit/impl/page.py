from ..app import App, Page


class TotallyLitPage(Page):
    def from_function(
        app: App,
        function: callable,
        title: str = None,
        icon: str = None,
        order: int = 0,
        name: str = None,
    ):
        name = name or (name := function.__name__)
        title = (
            title if title else " ".join(part.capitalize() for part in name.split("_"))
        )
        return TotallyLitPage(
            app, name, function=function, title=title, icon=icon, order=order
        )
