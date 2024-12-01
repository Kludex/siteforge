from __future__ import annotations

import uvicorn

from siteforge.applications import SiteForge


def run(app: SiteForge | str, *, host: str = "127.0.0.1", port: int = 8000) -> None:
    uvicorn.run(app, host=host, port=port)
