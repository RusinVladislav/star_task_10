def get_data(data):
    """Получает текстовый файл с данными и возвращает словарь, где ключ - порядковый номер, значение - данные"""

    with open(data, 'r', encoding='utf-8') as file:
        res = {int(s.split(' ')[0]): s.strip() for s in file.readlines()}
    return res


def get_user_by_pk(user_data, pk):
    """Получает словарь с данными и возвращает значения по переданному ключу"""

    return user_data.get(pk)
