from __future__ import annotations

from ..applications import SiteForge
from .config import Config
from .server import Server


def run(app: SiteForge | str, *, host: str = "127.0.0.1", port: int = 8000) -> None:
    config = Config(app=app, host=host, port=port)
    server = Server(config)
    server.run()
