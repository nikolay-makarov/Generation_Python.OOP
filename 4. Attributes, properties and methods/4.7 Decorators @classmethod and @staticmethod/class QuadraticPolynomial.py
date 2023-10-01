"""Класс QuadraticPolynomial
Квадратный трехчлен — это многочлен вида ax**2+bx+c, где a≠0. Например:
x**2 + 1
x**2 − 5x + 6
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен. При создании экземпляра класс должен принимать
три аргумента в следующем порядке:
a — коэффициент aa квадратного трехчлена
b — коэффициент bb квадратного трехчлена
c — коэффициент cc квадратного трехчлена
Экземпляр класса QuadraticPolynomial должен иметь три атрибута:
a — коэффициент aa квадратного трехчлена
b — коэффициент bb квадратного трехчлена
c — коэффициент cc квадратного трехчлена
Класс QuadraticPolynomial должен иметь два метода класса:
from_iterable() — метод, принимающий в качестве аргумента итерируемый объект из трех элементов a, b и c,
которые представляют коэффициенты квадратного трехчлена, и возвращающий экземпляр класса QuadraticPolynomial,
созданный на основе переданных коэффициентов
from_str() — метод, принимающий в качестве аргумента строку, которая содержит коэффициенты a, b и c
квадратного трехчлена, записанные через пробел. Метод должен возвращать экземпляр класса QuadraticPolynomial,
созданный на основе переданных коэффициентов, предварительно преобразованных в экземпляры класса float
"""


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @classmethod
    def from_iterable(cls, iterable):
        return cls(*iterable)

    @classmethod
    def from_str(cls, my_list):
        numbers = map(float, my_list.split())
        return cls(*numbers)


polynom = QuadraticPolynomial(1, -5, 6)

print(polynom.a)  # 1
print(polynom.b)  # -5
print(polynom.c)  # 6


polynom2 = QuadraticPolynomial.from_iterable([2, 13, -1])

print(polynom2.a)  # 2
print(polynom2.b)  # 13
print(polynom2.c)  # -1

polynom3 = QuadraticPolynomial.from_str('-1.5 4 14.8')
print(polynom3.a)  # -1.5
print(polynom3.b)  # 4.0
print(polynom3.c)  # 14.8
print(polynom3.a + polynom3.b + polynom3.c)  # 17.3
