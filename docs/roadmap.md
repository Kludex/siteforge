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
- [ ] Add benchmarks.
- [ ] Remove anyio, but still support trio.
- [ ] Rust multipart package.
- [ ] Remove support for ASGI 2.

## ForgeServer

- [ ] HTTP/2 support.
- [ ] HTTP/3 support.
- [ ] WebSockets sans-io support.
- [ ] Create Rust HTTP parser, and use it.
- [ ] Wait for first body response to send headers.
- [ ] Remove support for ASGI 2.
