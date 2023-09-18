"""Класс Postman.
Реализуйте класс Postman, описывающий почтальона. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Postman должен иметь один атрибут:
- delivery_data — изначально пустой список адресов, по которым следует доставить письма.
Экземпляр класса Postman должен иметь три метода экземпляра:
- add_delivery() — метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов
эти данные в виде кортежа: (<улица>, <дом>, <квартира>);
- get_houses_for_street() — метод, принимающий в качестве аргумента улицу и возвращающий список
всех домов на этой улице, в которые требуется доставить письма;
- get_flats_for_house() — метод, принимающий в качестве аргументов улицу и дом и возвращающий список
всех квартир в этом доме, в которые требуется доставить письма.
"""


class Postman:
    def __init__(self) -> None:
        self.delivery_data: list = []

    def add_delivery(self, street: str, house: int, flat: int) -> None:
        self.delivery_data.append((street, house, flat))

    def get_houses_for_street(self, delivery_street: str) -> list[int]:
        result: list = []
        for street, house, _ in self.delivery_data:
            if house not in result and street == delivery_street:
                result.append(house)
        return result

    def get_flats_for_house(self, delivery_street, delivery_house) -> list[int]:
        result: list = []
        for street, house, flat in self.delivery_data:
            if flat not in result and street == delivery_street and house == delivery_house:
                result.append(flat)
        return result


postman1 = Postman()

print(postman1.delivery_data)  # []
print(postman1.get_houses_for_street('3-я ул. Строителей'))  # []
print(postman1.get_flats_for_house('3-я ул. Строителей', 25))  # []


postman2 = Postman()

postman2.add_delivery('Советская', 151, 74)
postman2.add_delivery('Советская', 151, 75)
postman2.add_delivery('Советская', 90, 2)
postman2.add_delivery('Советская', 151, 74)

print(postman2.get_houses_for_street('Советская'))  # [151, 90]
print(postman2.get_flats_for_house('Советская', 151))  # [74, 75]
