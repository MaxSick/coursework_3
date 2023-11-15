from src.utils import sort_and_filter, format_data


def test_sort_and_filter():
    """
    Тестируем функцию sort_and_filter
    :return:
    1. Возвращает список
    2. Возвращает список из 5 словарей
    """
    assert type(sort_and_filter()) == list
    assert len(sort_and_filter()) == 5


def test_format_data():
    """
    Тестируем функцию format_data на получение корректного формата
    """
    assert format_data("2018-12-20T16:43:26.929246") == "20.12.2018"
    assert format_data("2018-09-12T21:27:25.241689") == "12.09.2018"
    assert format_data("2019-12-07T06:17:14.634890") == "07.12.2019"
