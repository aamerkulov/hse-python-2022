import random
from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    greeting = 'Hello '+name
    return greeting


def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """

    amount = random.randint(10000, 100000000)
    amount = amount/100
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    f = 0
    if len(phone_number) == 12 and phone_number[0] == '+' and phone_number[1] == '7':
        f = 1
    for i in list(range(2, 11, 1)):
        if ord(phone_number[i]) < 48 or ord(phone_number[i]) > 57:
            f = 0
        if f == 1:
            result = True
        else:
            result = False

    return result


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :param transfer_amount: сумма перевода
    :return: буленовское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    if float(current_amount) >= float(transfer_amount):
        result = True
    else:
        result = False
    return result


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :param uncultured_words: список запрещенных слов
    :return: текст, соответсвующий правилам
    """
    k = 0
    result=""
    while ord(text[k]) == 32:
        k += 1
    asci=ord(text[k])
    if asci >= 97 and asci <= 122:
        asci -= 32
    result += chr(asci)
    k += 1
    while k < len(text):
        asci = ord(text[k])
        if asci >= 65 and asci <= 90:
            asci += 32
            result += chr(asci)
        elif asci == 34 or asci == 39:
            result += ""
        else:
            result += chr(asci)
        k += 1
    k = len(result)-1
    while ord(result[k]) == 32:
        k -= 1
    result=result[:k+1]

    n=len(uncultured_words)
    num=[0 for i in range(n)]
    print(result, "+", k,n,num[0],num[1])
    for i in range(0,n):
        num[i] = result.find(uncultured_words[i])
        print(num[i],uncultured_words[i],i)
        for j in range(num[i],num[i]+len(uncultured_words[i])):
            if num[i]>=0:
                result=result[:j]+"#"+result[j+1:]

    print(result,"+",k,num[0],num[1])
    return result


def create_request_for_loan(user_info: str) -> str:
    """
    Генерирует заявку на кредит на основе входящей строки.
    Формат входящий строки:
    
    Иванов,Петр,Сергеевич,01.01.1991,10000
    
    Что должны вернуть на ее основе:
    
    Фамилия: Иванов
    Имя: Петр
    Отчество: Сергеевич
    Дата рождения: 01.01.1991
    Запрошенная сумма: 10000
    
    :param user_info: строка с информацией о клиенте
    :return: текст кредитной заявки
    """

    k = 0
    fam = ""
    name = ""
    otc = ""
    date = ""
    sum = ""
    while ord(user_info[k]) != 44:
        fam += user_info[k]
        k += 1
    k += 1
    while ord(user_info[k]) != 44:
        name += user_info[k]
        k += 1
    k += 1
    while ord(user_info[k]) != 44:
        otc += user_info[k]
        k += 1
    k += 1
    while ord(user_info[k]) != 44:
        date += user_info[k]
        k += 1
    k += 1
    while k != len(user_info):
        sum += user_info[k]
        k += 1
    result="Фамилия: "+fam+"\n"+"Имя: "+name+"\n"+"Отчество: "+otc+"\n"+"Дата рождения: "+date+"\n"+"Запрошенная сумма: "+sum
    return result
