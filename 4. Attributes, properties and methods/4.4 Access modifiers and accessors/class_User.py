"""Класс User
Реализуйте класс User, описывающий интернет-пользователя.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:
- name — имя пользователя. Если name не является непустой строкой, состоящей только из букв,
должно быть возбуждено исключение ValueError с текстом: Некорректное имя.
- age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110],
должно быть возбуждено исключение ValueError с текстом: Некорректный возраст.
Экземпляр класса User должен иметь два атрибута:
_name — имя пользователя
_age — возраст пользователя
Класс User должен иметь четыре метода экземпляра:
get_name() — метод, возвращающий имя пользователя
set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name.
Если new_name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение
ValueError с текстом:
Некорректное имя
get_age() — метод, возвращающий возраст пользователя
set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age.
Если new_age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение
ValueError с текстом: Некорректный возраст
"""


class User:
    def __init__(self, name: str, age: int) -> None:
        self._name = None
        self.set_name(name)
        self._age = None
        self.set_age(age)

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        if not isinstance(new_name, str) or not new_name.isalpha():
            raise ValueError('Некорректное имя')
        self._name = new_name

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int) -> None:
        if not isinstance(new_age, int) or not (0 <= new_age <= 110):
            raise ValueError('Некорректный возраст')
        self._age = new_age


user = User('Гвидо', 67)

user.set_name('Николай')
user.set_age(46)

print(user.get_name())  # Николай
print(user.get_age())  # 46
