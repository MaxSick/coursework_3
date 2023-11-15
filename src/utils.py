import json, datetime, re


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


def format_data(date):
    """
    Переформатирует написание даты
    :param date: %Y-%m-%dT%H:%M:%S.%f
    :return: %d.%m.%Y
    """
    date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f') # получили и разложили дату имеющегося формата
    return date_time_obj.date().strftime("%d.%m.%Y") # собрали дату в нужной нам последовательности


def card_format(text):
    """
    Принимает значения счетов "from" и "to" для форматирования
    :return: строку со скрытыми данными счетов
    """
    word_list = text.split()
    correct_text = []

    for word in word_list:
        if word.isalpha():
            correct_text.append(word)
        if word.isnumeric():
            if len(word) == 16:
                a = word.replace(word[6:-4], "******")
                correct_text.append(" ".join(re.findall(r'\S\S\S\S', a)))
            else:
                correct_text.append("**" + word[-4:])
    return " ".join(correct_text)
