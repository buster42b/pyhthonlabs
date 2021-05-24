import main


def test_ilen_ok():
    result = main.ilen((x for x in range(30)))
    assert 30 == result


def test_flatten_ok():
    result = list(main.flatten([0, [1, 2, [2, 3], [2, 3]], 5]))
    assert result == [0, 1, 2, 2, 3, 2, 3, 5]


def test_distinct_ok():
    result = list(main.distinct([1, 2, 1, 1, 1, 2, 2, 3, 2, 1]))
    assert result == [1, 2, 3]


def test_groupby_ok():
    users = [{'gender': 'female', 'age': 23},
             {'gender': 'male', 'age': 20},
             {'gender': 'female', 'age': 21}]
    result = main.groupby('gender', users)
    assert result == {
        'female': [
            {'gender': 'female', 'age': 23},
            {'gender': 'female', 'age': 21}
        ],
        'male': [
            {'gender': 'male', 'age': 20}
        ]
    }


def test_chunks_ok():
    result = list(main.chunks(3, [0, 1, 2, 3, 4]))
    assert result == [(0, 1, 2), (3, 4, None)]


def test_first_ok():
    foo = (x for x in range(10))
    result = main.first(foo)
    assert result == 0


def test_last_ok():
    foo = (x for x in range(10))
    result = main.last(foo)
    assert result == 9
