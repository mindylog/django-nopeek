"""Utilities"""

from importlib import import_module
from typing import Callable, Union


def import_callable(path_or_callable: Union[Callable, str]) -> Callable:
    """Import callable

    Args:
        path_or_callable (Union[Callable, str]): callable object or path string

    Returns:
        Callable: callable
    """
    if hasattr(path_or_callable, "__call__"):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, str)
        package, attr = path_or_callable.rsplit(".", 1)
        return getattr(import_module(package), attr)
