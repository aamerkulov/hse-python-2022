from typing import Dict

from .exception import NoSuchPositionError

POSITIONS: Dict[str, int] = {
    'CEO': 0,
    'manager': 1,
    'developer': 2,
    'tester': 3,
}


def get_position_level(position_name: str) -> int:
    """
    Функция возвращает уровень позиции по ее названию. 
    Если должности нет в базе поднимается исключение `NoSuchPositionError(position_name)`
    """
    try:
        return POSITIONS[position_name]
    except KeyError as exp:
        raise NoSuchPositionError(position_name) from exp


class Employee:
    """
    Класс - сотрудник

    Возможности:
    1. Реализована возможность сравнения двух сотрудников в зависимости от занимаемой должности - метод __eq__
    2. Возможность получить зарплату через метод get_salary
    """
    name: str
    position: str
    _salary: int

    def __init__(self, name: str, position: str, salary: int):
        """
        Задача: реализовать конструктор класса, чтобы все тесты проходили
        """
        if isinstance(name,str) and isinstance(position,str) and isinstance(salary,int):
            self.name = name
            self.position = position
            self._salary = salary
        else:
            raise ValueError




    def get_salary(self) -> int:
        """
        Метод возвращает зарплату сотрудника.
        """

        return self._salary

    def __eq__(self, other: object) -> bool:
        """
        Задача: реализовать метод сравнение двух сотрудников, чтобы все тесты проходили.

        Сравнение происходит по уровню позиции см. `get_position_level`.
        Если что-то идет не так - бросаются исключения. Смотрим что происходит в тестах.
        """
        if isinstance(other,Employee) and isinstance(self, Employee):
            print("-----")
            print(self)
            print(other)
            print(self.position)
            print(other.position)
            print(isinstance(other,Employee))
            print(isinstance(self, Employee))
            print(self.position in POSITIONS)
            print(other.position in POSITIONS)
            print("-----")
            if self.position not in POSITIONS or other.position not in POSITIONS:
                raise ValueError
            else:
                print("=====")
                print(self.position)
                print(other.position)
                print("=====")
                p1 = get_position_level(self.position)
                p2 = get_position_level(other.position)
                if p1 == p2:
                    return True

        else:
            print("+++++")
            print(isinstance(other, Employee))
            print(isinstance(self, Employee))
            print("+++++")
            raise TypeError
            print(self.position)
            raise NoSuchPositionError(self.position) or NoSuchPositionError(other.position)
            print(NoSuchPositionError)
    def __str__(self):
        """
        Задача: реализовать строковое представление объекта.
        Пример вывода: 'name: Ivan position manager'
        """

        result = "name: "+self.name+" position: "+self.position
        return result
    def __hash__(self):
        return id(self)


class Developer(Employee):
    """
    Сотрудник - разработчик
    """

    language: str
    position: str = 'developer'

    def __init__(self, name: str, salary: int, language: str):
        """
        Задача: реализовать конструктор класса, используя конструктор родителя
        """

        self.name = name
        self._salary = salary
        self.language = language


class Manager(Employee):
    """
    Сотрудник - менеджер
    """

    position: str = 'manager'

    def __init__(self, name: str, salary: int):
        """
        Задача: реализовать конструктор класса, используя конструктор родителя
        """

        self.name = name
        self._salary = salary
