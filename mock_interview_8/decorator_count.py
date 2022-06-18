def count_calls(func):
    def inner(*argc, **argv):
        inner.counter += 1
        print(inner.counter)
        return func(*argc, **argv)
    inner.counter = 0
    return inner


# def count_calls(func):
#     @functools.wraps(func)
#     def wrapper_count_calls(*args, **kwargs):
#         wrapper_count_calls.num_calls += 1
#         print(f"{wrapper_count_calls.num_calls} вызов функции {func.__name__!r}")
#         return func(*args, **kwargs)
#     wrapper_count_calls.num_calls = 0
#     return wrapper_count_calls


@count_calls
def sum(a, b):
    return a + b


@count_calls
def sub(a, b):
    return a + b


sum(1, 2)

sum(1, 2)
sum(1, 2)

sub(1, 2)
