from pathlib import Path
from typing import Dict, Any, List, Optional


def count_words(text: str) -> Dict[str, int]:
    """
    Функция для подсчета слов в тексте.

    При подсчете слов - все знаки препинания игнорируются.
    Словом считается непрерывная последовательность длиной больше одного
    символа, состоящая из букв в диапазоне A-Z и a-z.
    Если в последовательности присутствует цифра - это не слово.

    Hello - слово
    Hello7 - не слово

    При подсчете слов регистр букв не имеет значения.

    Результат выполнения функции словарь, в котором:
    ключ - слово в нижнем регистре
    значение - количество вхождений слов в текст

    :param text: текст, для подсчета символов
    :return: словарь, в котором:
             ключ - слово в нижнем регистре
             значение - количество вхождений слов в текст
    """
    k = 0
    f = 0
    word = ""
    result = {}
    if text == "":
        result = {}
    else:
        while k != len(text):
            if (ord(text[k]) < 48) or (ord(text[k]) > 57) and (ord(text[k]) < 65) or (ord(text[k]) > 90) and (ord(text[k]) < 97) or (ord(text[k]) > 122):
                print(word)
                if f == 0:
                    if word in result:
                        result[word] += 1
                    else:
                        result[word] = 1
                    word = ""
                    f = 1
                if k != (len(text)-1) and (ord(text[k+1]) >= 65 and ord(text[k+1]) <= 90 or ord(text[k+1]) >= 97 and ord(text[k+1]) <= 122):
                    f = 0
            elif (ord(text[k]) >= 65 and ord(text[k]) <= 90 or ord(text[k]) >= 97 and ord(text[k]) <= 122) and f == 0:
                sign = text[k]
                if ord(text[k]) >= 65 and ord(text[k]) <= 90:
                    sign = chr(ord(text[k])+32)
                word += sign
                if k == len(text)-1:
                    if word in result:
                        result[word] += 1
                    else:
                        result[word] = 1
                    word = ""
            elif ord(text[k]) >= 48 and ord(text[k]) <= 57:
                f = 1
                word = ""
            k += 1
            print(word)
            print("++++++++",text[k-1], result)

    print("+++",result)
    return result


def exp_list(numbers: List[int], exp: int) -> List[int]:
    """
    Функция, которая возводит каждый элемент списка в заданную степень

    :param numbers: список, состоящий из натуральных чисел
    :param exp: в какую степень возвести числа в списке
    :return: список натуральных чисел
    """
    result = [0 for i in range(len(numbers))]
    for i in range(0, len(numbers)):
        print(numbers[i],exp)
        result[i] = numbers[i] ** exp

    return result


def get_cashback(operations: List[Dict[str, Any]], special_category: List[str]) -> float:
    """
    Функция для расчета кешбека по операциям.
    За покупки в обычных категориях возвращается 1% от стоимости покупки
    За покупки в special_category начисляют 5% от стоимости покупки

    :param operations: список словарей, содержащих поля
           amount - сумма операции
           category - категория покупки
    :param special_category: список категорий повышенного кешбека
    :return: размер кешбека
    """

    res = 0
    for x in operations:
        if x['category'] in special_category:
            res += x['amount'] * 0.05
        else:
            res += x['amount'] * 0.01
    return res


def get_path_to_file() -> Optional[Path]:
    """
    Находит корректный путь до тестового файла.

    Если запускать тесты из pycharm - начальная папка - tests
    Если запускать файлы через make tests - начальная папка - корень проекта

    :return: путь до тестового файла tasks.csv
    """
    if Path().resolve().name == 'tests':
        base_path = Path().resolve().parent
    else:
        base_path = Path().resolve()
    return base_path / 'tasks' / 'practice3' / 'tasks.csv'


def csv_reader(header: str) -> int:
    """
    Функция считывает csv файл и подсчитывает количество
    уникальных элементов в столбце.
    Столбец выбирается на основе имени заголовка,
    переданного в переменной header.

    Обратите внимание на структуру файла!
    Первая строка - строка с заголовками.
    Остальные строки - строки с данными.

    Файл для анализа: tasks.csv
    Для того чтобы файл корректно открывался в тестах:
    для получения пути до файла - используйте функцию get_path_to_file
    которая определена перед функцией.

    CSV анализируем с помощью встроенной библиотеки csv

    :param header: название заголовка
    :return: количество уникальных элементов в столбце
    """
    import csv
    sl=[[0 for i in range(10)] for j in range(10)]
    dict={}
    f = get_path_to_file()
    print(f)
    csvfile=open(f,'r',newline='')
    obj=csv.reader(csvfile)
    k = 0
    for row in obj:
        for i in range(4):
            sl[k][i] = row[i]
        k += 1
    k = 0
    while sl[0][k] != header:
        k+=1
    for i in range(1,10,1):
          if sl[i][k] != 0:
             if sl[i][k] in dict:
                  dict[sl[i][k]] += 1
             else:
                 dict[sl[i][k]] = 1
    print(sl)
    print(dict)
    result = len(dict)
    return result
