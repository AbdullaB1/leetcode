import functools


def my_decorator(func):
    def wrapper():
        print("До вызова функции.")
        func()
        print("После вызова функции.")
    return wrapper


# https://proglib.io/p/vse-chto-nuzhno-znat-o-dekoratorah-python-2020-05-09
# универсальный шаблон декоратора
def decorator(func):
    # нужно для корректной идентификации функции, отображения __name__ и для использования help()
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Что-то делаем до
        value = func(*args, **kwargs)
        # Что-то делаем после
        return value
    return wrapper_decorator

# работает как если передать num_times, так и без параметров


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


def a(x): return x**2


@repeat
def say_whee():
    print("Ура!")


say_whee()
# декоратор через класс


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"{self.num_calls} вызов функции {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee_2():
    print("Ура!")


# say_whee_2()
