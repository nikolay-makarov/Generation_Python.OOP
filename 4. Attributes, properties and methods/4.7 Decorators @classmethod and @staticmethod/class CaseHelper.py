"""Класс CaseHelper 🌶️
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_)
и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.
Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов,
при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.
Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case.
При создании экземпляра класс не должен принимать никаких аргументов.
Класс CaseHelper должен иметь четыре статических метода:
is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана
в стиле Snake Case, или False в противном случае
is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True,
если переданная строка записана в стиле Upper Camel Case, или False в противном случае
to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case,
записывает ее в стиле Snake Case и возвращает полученный результат
to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case,
записывает ее в стиле Upper Camel Case и возвращает полученный результат
"""


class CaseHelper:
    @classmethod
    def is_snake(cls, string) -> bool:
        return not ('__' in string) and string.islower()

    @classmethod
    def is_upper_camel(cls, string: str) -> bool:
        return not ('_' in string) and string[0].isupper()

    @classmethod
    def to_snake(cls, string: str) -> str:
        result = [string[0].lower()]
        for char in string[1:]:
            if char.isupper():
                result.extend(['_', char.lower()])
            else:
                result.append(char)
        return ''.join(result)

    @classmethod
    def to_upper_camel(cls, string: str) -> str:
        result = string.split('_')
        return ''.join(map(str.capitalize, result))


print(CaseHelper.is_snake('beegeek'))   # True
print(CaseHelper.is_snake('bee_geek'))  # True
print(CaseHelper.is_snake('Beegeek'))   # False
print(CaseHelper.is_snake('BeeGeek'))   # False
print()

print(CaseHelper.is_upper_camel('beegeek'))     # False
print(CaseHelper.is_upper_camel('bee_geek'))    # False
print(CaseHelper.is_upper_camel('Beegeek'))     # True
print(CaseHelper.is_upper_camel('BeeGeek'))     # True
print()

print(CaseHelper.to_snake('Beegeek'))   # beegeek
print(CaseHelper.to_snake('BeeGeek'))   # bee_geek
print()

print(CaseHelper.to_upper_camel('beegeek'))     # Beegeek
print(CaseHelper.to_upper_camel('bee_geek'))    # BeeGeek
