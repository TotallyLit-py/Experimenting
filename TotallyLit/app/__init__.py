from dataclasses import dataclass
from pathlib import Path

from .info import AppInfo


@dataclass
class App:
    info: AppInfo

    def from_folder(folder: Path):
        return App(AppInfo(folder))
