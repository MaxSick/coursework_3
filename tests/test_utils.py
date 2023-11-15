from src.utils import sort_and_filter


def test_sort_and_filter():
    """
    Тестируем функцию sort_and_filter
    :return:
    1. Возвращает список
    2. Возвращает список из 5 словарей
    """
    assert type(sort_and_filter()) == list
    assert len(sort_and_filter()) == 5