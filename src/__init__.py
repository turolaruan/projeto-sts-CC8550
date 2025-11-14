"""Finance management application package."""

from importlib import metadata

__all__ = ["__version__"]


def __getattr__(name: str) -> str:
    """Expose the installed package version lazily."""

    if name == "__version__":
        try:
            return metadata.version("finance-manager")
        except metadata.PackageNotFoundError:
            return "0.0.0"
    raise AttributeError(name)
