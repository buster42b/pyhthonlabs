from collections.abc import Iterable

# получение размера генератора
def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return sum(1 for _ in iterable)

# переделка многоуровневого массива в одноуровневый
def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]
    """

    for i in iterable:
        if isinstance(i, (list, set, frozenset, tuple)):
            yield from flatten(i)
        elif isinstance(i, (int, str, float, bool)):
            yield i
        else:
            raise ValueError("unexpected type token")

# убирает повторы
def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    mas = []
    for x in iterable:
        if x not in mas:
            mas.append(x)
            yield x

# группировка словарей
def groupby(key, iterable: Iterable):
    """
    >>> users = [{'gender': 'female', 'age': 23},{'gender': 'male', 'age': 20},{'gender': 'female', 'age': 21}] # noqa: E501
    >>> groupby('gender', users)
    {'female': [{'gender': 'female', 'age': 23}, {'gender': 'female', 'age': 21}], 'male': [{'gender': 'male', 'age': 20}]} # noqa: E501
    """
    groupBy - setordefault
    res = {}
    for x in iterable:
        if x[key] not in res:
            res[x[key]] = []
        res[x[key]].append(x)
    return res

# разбивка
def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 2), (3, 4, None)]
    """

    if not isinstance(size, int):
        raise TypeError()
    if size <= 0:
        raise ValueError()
    
    res = []
    for x in iterable:
        res.append(x)
        if len(res) == size:
            yield tuple(res)
            res = []
    if len(res) > 0:
        res.append(None)
        yield tuple(res)

# первый элемент
def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> print(first(range(0)))
    None
    """
    return next(iter(iterable), None)

# последний элемент
def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> print(last(range(0)))
    None
    """
    item = None
    for item in iterable:
        pass
    return item
