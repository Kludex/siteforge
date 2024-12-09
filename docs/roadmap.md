## SiteForge

- [ ] AsyncAPI support.
- [ ] WebSockets documentation.
- [ ] Own `TestClient` with both flavors: `async` and `sync`.
- [ ] Generate clients for other languages via CLI.
- [ ] Support lifespan on child apps.
- [ ] Add `uvicorn` as only server.
- [ ] Runtime warning when sending back an exception that is not documented.
- [ ] More plugable background tasks API.
- [ ] OpenTelemetry support.
    - [ ] Add `system.uptime` metric (https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/31627).
- [ ] Automatic cache on `GET` and `HEAD` methods (https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).
- [ ] Add `HEAD` method on `GET` routes.
- [ ] Health endpoint.
    - [ ] Don't print access logs on health endpoint.
- [ ] Add own routing system.
- [ ] Add benchmarks (https://github.com/CodSpeedHQ).
- [ ] Remove anyio, but still support trio.
- [ ] Rust multipart package.
- [X] Remove support for ASGI 2.
- [ ] Multiple response output format depending on the `Accept` header.
- [ ] Add other decompression middlewares (zstd, brotli, etc.)

## ForgeServer

- [ ] HTTP/2 support.
- [ ] HTTP/3 support.
- [ ] WebSockets sans-io support.
- [ ] Create Rust HTTP parser, and use it.
- [ ] Wait for first body response to send headers.
- [X] Remove support for ASGI 2.
- [ ] Add new logging system.
- [ ] Move reload and multiprocess to the `Server` class.

## Infra

- [ ] Run tests only when source code imported had changes.
- [X] Set development VERSION to `0.0.0`, and publish on every PR to `pypi.test`.

## Documentation

- [ ] Add comments and reactions.
