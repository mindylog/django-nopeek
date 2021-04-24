"""Utilities"""

from typing import Callable, Union

from django.utils.module_loading import import_string


def import_callable(path_or_callable: Union[Callable, str]) -> Callable:
    """Import callable

    Args:
        path_or_callable (Union[Callable, str]): callable object or path string

    Returns:
        Callable: callable
    """
    if hasattr(path_or_callable, "__call__"):
        return path_or_callable
    elif isinstance(path_or_callable, str):
        try:
            return import_string(path_or_callable)
        except ImportError as e:
            message = f"Could not import {path_or_callable}. {e.__class__.__name__}: {e}."
            raise ImportError(message)
    else:
        message = f"Passed parameter {path_or_callable} is not callable or string."
        raise TypeError(message)
