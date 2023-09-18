"""Класс Person
Реализуйте класс Person, описывающий человека.
При создании экземпляра класс должен принимать два аргумента в следующем порядке:
- name — имя человека
- surname — фамилия человека
Экземпляр класса Person должен иметь два атрибута:
- name — имя человека
- surname — фамилия человека
Класс Person должен иметь одно свойство:
- fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
<имя> <фамилия>
Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя.
Аналогично при изменении полного имени должны изменяться имя и фамилия.
Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def get_fullname(self) -> str:
        return f'{self.name} {self.surname}'

    def set_fullname(self, fullname: str):
        self.name, self.surname = fullname.split()

    fullname = property(get_fullname, set_fullname)


person = Person('Меган', 'Фокс')

print(person.name)      # Меган
print(person.surname)   # Фокс
print(person.fullname)  # Меган Фокс

person.name = 'Стефани'
print(person.fullname)  # Стефани Фокс

person2 = Person('Алан', 'Тьюринг')

person2.surname = 'Вирт'
print(person2.fullname)  # Алан Вирт

person3 = Person('Джон', 'Маккарти')

person3.fullname = 'Алан Тьюринг'
print(person3.name)     # Алан
print(person3.surname)  # Тьюринг
