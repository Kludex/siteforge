import importlib.metadata
import platform
from argparse import ArgumentParser


def version_callback() -> None:
    """Show the version and exit."""
    py_impl = platform.python_implementation()
    py_version = platform.python_version()
    system = platform.system()
    version = importlib.metadata.version("siteforge")

    print(f"Running Logfire {version} with {py_impl} {py_version} on {system}.")


def main() -> None:
    parser = ArgumentParser(
        prog="SiteForge", description="SiteForge command line interface.", epilog="SiteForge is a web framework."
    )
    parser.add_argument("--version", action="store_true", help="show the version and exit")

    namespace = parser.parse_args()

    if namespace.version:
        version_callback()


if __name__ == "__main__":
    main()
