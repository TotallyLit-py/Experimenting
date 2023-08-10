import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppInfo:
    root_folder: Path
    pages_folder: Path = Path("pages")
    views_folder: Path = Path("views")
    layout_folder: Path = views_folder / Path("layout")
    header_file_path: Path = layout_folder / Path("header.py")
    footer_file_path: Path = layout_folder / Path("footer.py")

    def get_root_path(self) -> Path:
        try:
            path = Path(self.root_folder).resolve()
            if not os.path.isdir(path):
                raise NotADirectoryError(f"Root path is not a directory: {path}")
            return path
        except FileNotFoundError:
            raise FileNotFoundError(f"Root path does not exist: {self.root_folder}")

    def get_app_path(self, path: Path) -> Path:
        full_path = path if path.is_absolute() else self.get_root_path() / path
        try:
            return full_path.resolve()
        except FileNotFoundError:
            raise FileNotFoundError(f"Path does not exist: {full_path}")

    def get_views_path(self):
        return self.get_app_path(self.views_folder)

    def get_pages_path(self):
        return self.get_app_path(self.pages_folder)

    def get_layout_path(self):
        return self.get_app_path(self.layout_folder)

    def get_header_path(self):
        return self.get_app_path(self.header_file_path)

    def get_footer_path(self):
        return self.get_app_path(self.footer_file_path)
