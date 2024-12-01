import argparse


def version_callback() -> None:
    """Show the version and exit."""
    import importlib.metadata
    import platform

    py_impl = platform.python_implementation()
    py_version = platform.python_version()
    system = platform.system()
    version = importlib.metadata.version("siteforge")

    print(f"Running Logfire {version} with {py_impl} {py_version} on {system}.")


def parse_run(args: argparse.Namespace) -> None:
    from siteforge._server import run

    run(args.app, host=args.host, port=args.port)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="SiteForge", description="SiteForge command line interface.", epilog="SiteForge is a web framework."
    )
    parser.add_argument("--version", action="store_true", help="show the version and exit")

    subparsers = parser.add_subparsers(title="commands", metavar="")

    cmd_run = subparsers.add_parser("run", help=parse_run.__doc__)
    cmd_run.set_defaults(func=parse_run)
    cmd_run.add_argument("app", help="The application to run.")
    cmd_run.add_argument("--host", default="127.0.0.1", help="Bind socket to this host.")
    cmd_run.add_argument("--port", type=int, default=8000, help="Bind socket to this port.")

    namespace = parser.parse_args()

    if namespace.version:
        version_callback()
    else:
        namespace.func(namespace)


if __name__ == "__main__":
    main()
