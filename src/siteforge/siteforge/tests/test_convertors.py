from datetime import datetime
from typing import Iterator

import pytest

from siteforge.convertors import Convertor, register_url_convertor
from siteforge.requests import Request
from siteforge.responses import JSONResponse
from siteforge.routing import Route, Router
from siteforge.tests.types import TestClientFactory
from starlette import convertors


@pytest.fixture(scope="module", autouse=True)
def refresh_convertor_types() -> Iterator[None]:
    convert_types = convertors.CONVERTOR_TYPES.copy()
    yield
    convertors.CONVERTOR_TYPES = convert_types


class DateTimeConvertor(Convertor[datetime]):
    regex = "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(.[0-9]+)?"

    def convert(self, value: str) -> datetime:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")

    def to_string(self, value: datetime) -> str:
        return value.strftime("%Y-%m-%dT%H:%M:%S")


@pytest.fixture(scope="function")
def app() -> Router:
    register_url_convertor("datetime", DateTimeConvertor())

    def datetime_convertor(request: Request) -> JSONResponse:
        param = request.path_params["param"]
        assert isinstance(param, datetime)
        return JSONResponse({"datetime": param.strftime("%Y-%m-%dT%H:%M:%S")})

    return Router(routes=[Route("/datetime/{param:datetime}", endpoint=datetime_convertor, name="datetime-convertor")])


def test_datetime_convertor(test_client_factory: TestClientFactory, app: Router) -> None:
    client = test_client_factory(app)
    response = client.get("/datetime/2020-01-01T00:00:00")
    assert response.json() == {"datetime": "2020-01-01T00:00:00"}

    assert (
        app.url_path_for("datetime-convertor", param=datetime(1996, 1, 22, 23, 0, 0)) == "/datetime/1996-01-22T23:00:00"
    )


@pytest.mark.parametrize("param, status_code", [("1.0", 200), ("1-0", 404)])
def test_default_float_convertor(test_client_factory: TestClientFactory, param: str, status_code: int) -> None:
    def float_convertor(request: Request) -> JSONResponse:
        param = request.path_params["param"]
        assert isinstance(param, float)
        return JSONResponse({"float": param})

    app = Router(routes=[Route("/{param:float}", endpoint=float_convertor)])

    client = test_client_factory(app)
    response = client.get(f"/{param}")
    assert response.status_code == status_code
