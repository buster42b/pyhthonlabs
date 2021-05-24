import pytest
import main


def test_potentially_unsafe_func_ok():
    result = main.potentially_unsafe_func('name')
    assert result == 'test'


def test_sum_of_values_ok():
    result = main.sum_of_values((1, 3, 5))
    assert result == 9


def test_sum_of_values_raises():
    with pytest.raises(ValueError):
        main.sum_of_values((1, 3, 5, 9))


def test_show_message_ok():
    main.show_message('test')


def test_process_text_ok():
    result = main.process_text('the French'
                               ' revolution resulted in 3 concepts: '
                               'freedom,equality,fraternity')
    assert result == 'ThE FrencH RevolutioN ' \
                     'ResulteD IN 3 Concepts  ' \
                     'Freedom Equality FraternitY'


def test_process_text_ok_2():
    result = main.another_process('the French '
                                  'revolution resulted in 3 concepts: '
                                  'freedom,equality,fraternity')
    assert result == 'ThE FrencH RevolutioN ' \
                     'ResulteD IN 3 ConceptS ' \
                     'FreedoM EqualitY FraternitY'
