from typing import Callable, TypeVar


T = TypeVar("T")
def find(iterable: list[T], fnc: Callable[[T], bool]) -> T | None:
    for obj in iterable:
        if fnc(obj):
            return obj
    return None