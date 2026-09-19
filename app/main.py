from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cash_result = {}

    @functools.wraps(func)
    def wrapper(*args: tuple) -> Callable:
        if args in cash_result:
            print("Getting from cache")
            return cash_result[args]
        print("Calculating new result")
        result = func(*args)
        cash_result[args] = result
        return result
    return wrapper
