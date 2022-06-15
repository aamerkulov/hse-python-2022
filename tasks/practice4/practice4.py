from typing import Any, Optional


def search_phone(content: Any, name: str) -> Optional[str]:
    """
    Функция поиска номера телефона пользователя в структуре данных.

    Алгоритм работы следующий:
    1) принимаем на вход структуру content, состоящую из словарей,
    списков и строковых ключей в списке
    2) внутри структуры может быть запись следующего формата:
    {
        'name': 'user_name',
        'phone': 'user_phone',
    }

    3) необходимо пройтись по всей структуре
    4) если встречаем словарь, в котором ключ name совпадает с
    аргументом функции name - берем из этого словаря поле phone
    и возвращаем этот телефон из функции
    5) если поле name с таким значением не найдено - возвращаем из
    функции None

    Может пригодиться:

    1) Чтобы проверить, является ли объект списком используйте функцию:
    isinstance(some_object, list)
    если some_object список - результат будет True
    если some_object не список - False

    2) Чтобы проверить, является ли объект словарем используйте функцию:
    isinstance(some_object, dict)


    :param content: словарь или список, внутрь которого вложены объекты. Внутри
                      может скрываться номер телефона пользователя
    :param name: имя пользователя, у которого будем искать номер телефона
    :return: номер телефона пользователя или None
    """

    def f_list(key: list) -> str:
            print("-----",len(key))
            if len(key) != 0:
                for i in range(len(key)):
                    is_list = isinstance(key[i], list)
                    is_dict = isinstance(key[i], dict)
                    print("-----", is_list)
                    if is_list == True:
                        result = f_list(key[i])

                    if is_dict == True:
                        print("===")
                        result = f_dict(key[i])

                return result


    def f_dict(key: dict) -> str:
        if len(key) != 0:
            if 'name' in key:
                print("+++++++")
                if key['name'] == name:
                    print("+++++++")
                    if 'phone' in key:
                        print("+++++++",name)
                        result = key['phone']
                        print(result)
                        return result


            else:
                print(":::::::")
                for i in key:
                    is_list = isinstance(key[i], list)
                    is_dict = isinstance(key[i], dict)
                    if is_list == True:
                        result = f_list(key[i])
                        return result
                    if is_dict == True:
                        result = f_dict(key[i])
                        return result



    result = ""
    print(isinstance(content,list))
    print(isinstance(content,dict))
    is_list = isinstance(content,list)
    is_dict = isinstance(content,dict)
    if is_list == True:
        result = f_list(content)
    else:
        result = f_dict(content)
    print(result)
    for key in content:
        print(key)
    if result == "":
        result = "None"

    return result
