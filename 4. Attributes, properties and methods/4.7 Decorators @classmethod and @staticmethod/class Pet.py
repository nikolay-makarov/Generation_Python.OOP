"""Класс Pet.
Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:
name — имя домашнего животного
Экземпляр класса Pet должен иметь один атрибут:
name — имя домашнего животного
Класс Pet должен иметь три метода класса:
first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet.
Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet.
Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet
"""
from typing import Optional


class Pet:
    pets: list['Pet'] = []

    def __init__(self, name: str) -> None:
        self.name = name
        Pet.pets.append(self)

    @classmethod
    def first_pet(cls) -> Optional['Pet']:
        if not Pet.num_of_pets():
            return None
        return cls.pets[0]

    @classmethod
    def last_pet(cls) -> Optional['Pet']:
        if not Pet.num_of_pets():
            return None
        return cls.pets[-1]

    @classmethod
    def num_of_pets(cls) -> int:
        return len(cls.pets)


print(Pet.first_pet())      # None
print(Pet.last_pet())       # None
print(Pet.num_of_pets())    # 0

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)  # Ratchet
print(Pet.last_pet().name)   # Rivet
print(Pet.num_of_pets())     # 3
