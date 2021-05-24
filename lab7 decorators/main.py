from datetime import datetime
from random import random
from time import sleep
from string import punctuation
from collections.abc import Callable


def calc_duration(func: Callable) -> Callable:
    def decorated():
        time_start = datetime.now()
        func()
        print(f'Time spent: '
              f'{(datetime.now() - time_start).microseconds / 1000} ms')

    return decorated


@calc_duration
def long_executing_task():  # func(*args, **kwargs) ==== long_executing_task
    for index in range(3):
        print(f'Iteration {index}')
        sleep(random())


def suppress_errors(exceptions: tuple):
    def decorator(func: Callable) -> Callable:
        def decorated(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as err:
                print(f'Error: {err}')

        return decorated

    return decorator


@suppress_errors((
        KeyError,
        ValueError,
))
def potentially_unsafe_func(key: str):
    print(f'Get data by the key {key}')
    data = {'name': 'test', 'age': 30}
    return data[key]


def result_between(value_min, value_max):
    def decorator(func: Callable) -> Callable:
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if result < value_min or result > value_max:
                raise ValueError
            return result

        return decorated

    return decorator


def len_more_than(s_len):
    def decorator(func: Callable) -> Callable:
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            if len(result) < s_len:
                raise ValueError
            return result

        return decorated

    return decorator


@result_between(0, 10)
def sum_of_values(numbers):
    return sum(numbers)


@len_more_than(10)
def show_message(message: str) -> str:
    return f'Hi, you sent: {message}'


def replace_commas(func: Callable) -> Callable:
    def decorated(text: str) -> str:
        for char in punctuation:
            text = text.replace(char, ' ')
        return func(text)

    return decorated


def capitalize(s):
    s, result = s.title(), ""
    for word in s.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


def words_title(func: Callable) -> Callable:
    def decorated(text: str) -> str:
        return func(capitalize(text))

    return decorated


@words_title
@replace_commas
def process_text(text: str) -> str:
    return text.replace(':', ',')


@replace_commas
@words_title
def another_process(text: str) -> str:
    return text.replace(':', ',')


def cache_result(func: Callable) -> Callable:
    cache = {}

    def decorated(*args, **kwargs):
        key = args.__str__() + kwargs.__str__()
        print(f'Cache key: {key}')
        if key in cache:
            print("Got from cache")
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return decorated


@cache_result
def some_func(last_name, first_name, age):
    return f'Hi {last_name} {first_name}, you are {age} years old'
