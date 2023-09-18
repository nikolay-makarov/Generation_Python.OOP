"""Класс Rectangle
Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен принимать
два аргумента в следующем порядке:
length — длина прямоугольника
width — ширина прямоугольника
Экземпляр класса Rectangle должен иметь два атрибута:
length — длина прямоугольника
width — ширина прямоугольника
Класс Rectangle должен иметь два свойства:
perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
area — свойство, доступное только для чтения, возвращающее площадь прямоугольника
"""


class Rectangle:
    def __init__(self, length: int | float, width: int | float) -> None:
        self.length = length
        self.width = width

    def get_perimeter(self) -> int | float:
        return self.length * 2 + self.width * 2

    def get_area(self) -> int | float:
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)


rectangle = Rectangle(4, 5)

print(rectangle.length)     # 4
print(rectangle.width)      # 5
print(rectangle.perimeter)  # 18
print(rectangle.area)       # 20

rectangle2 = Rectangle(4, 5)

rectangle2.length = 2
rectangle2.width = 3
print(rectangle2.length)     # 2
print(rectangle2.width)      # 3
print(rectangle2.perimeter)  # 10
print(rectangle2.area)       # 6
