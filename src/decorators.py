from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Декоратор логирует вызов функции и её результат в файл
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple, **kwargs: dict) -> Any:
            the_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                status = f"{the_date} {func.__name__} ok"

            except Exception as error:
                result = None
                status = f"{the_date} {func.__name__} error: {error}. Inputs: {args}, {kwargs}"

            if filename:
                with open(f"../data/{filename}", "a", encoding="utf-8") as file:
                    file.write(f"{status};\n")
            else:
                print(status)
            return result

        return inner

    return wrapper
