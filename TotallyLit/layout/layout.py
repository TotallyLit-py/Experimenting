class LayoutRenderer:
    header: callable
    footer: callable

    def __init__(self, header: callable, footer: callable):
        self.header = header
        self.footer = footer

    def __enter__(self):
        self.header()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.footer()
