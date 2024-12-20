from __future__ import annotations

import functools
from typing import Any, Literal

import pytest

from asgi_client import TestClient
from siteforge.tests.types import TestClientFactory


@pytest.fixture
def anyio_backend() -> Literal["asyncio"]:
    return "asyncio"


@pytest.fixture
def test_client_factory(
    anyio_backend_name: Literal["asyncio"], anyio_backend_options: dict[str, Any]
) -> TestClientFactory:
    # anyio_backend_name defined by:
    # https://anyio.readthedocs.io/en/stable/testing.html#specifying-the-backends-to-run-on
    return functools.partial(TestClient, backend=anyio_backend_name, backend_options=anyio_backend_options)
