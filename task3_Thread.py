import concurrent.futures
import threading
import time


class Repeat:
    def __init__(self, value=1):
        self.value = value


def repeatable_decorator(repeat_count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(repeat_count):
                func(*args, **kwargs)
        return wrapper
    return decorator


def execute_with_repeats(func, repeat_count):
    @repeatable_decorator(repeat_count)
    def wrapper():
        func()

    return wrapper


class CustomThreadPoolExecutor(concurrent.futures.ThreadPoolExecutor):
    def submit_with_repeats(self, func, repeat_count, *args, **kwargs):
        decorated_func = execute_with_repeats(func, repeat_count)
        return super().submit(decorated_func, *args, **kwargs)


def repeatable_task():
    print("Executing repeated task")


def main():
    with CustomThreadPoolExecutor(max_workers=5) as executor:
        future = executor.submit_with_repeats(repeatable_task, repeat_count=3)

        concurrent.futures.wait([future])


if __name__ == "__main__":
    main()
