from utils import sort_and_filter, format_data, card_format


if __name__ == '__main__':
    for i in sort_and_filter():
        print(f'''{format_data(i['date'])} {i['description']}
{card_format(i.get('from', 'Внесение средств'))} -> {card_format(i['to'])}
{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']} \n''')
