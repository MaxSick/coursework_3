import json


def sort_and_filter():
    """
    Читает json файл с данными,
    фильтруем по статусу выполнения "EXECUTED",
    сортируем в обратном порядке по дате,
    возвращаем список из пяти последних операций
    :return: Список словарей из последних пяти операций.
    """
    with open('operations.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
        operations = json.load(f)  # загнали все, что получилось в переменную
    filter_operations = [x for x in operations if x != {} and x['state'] == "EXECUTED"]  # отфильтровали по EXECUTED
    sorted_list = sorted(filter_operations, key=lambda x: x['date'], reverse=True)  # отсортировали всё по датам
    return sorted_list[:5]
