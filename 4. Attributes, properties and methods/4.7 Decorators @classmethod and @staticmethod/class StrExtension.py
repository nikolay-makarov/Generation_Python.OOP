"""Класс StrExtension.
Реализуйте класс StrExtension, описывающий набор функций для работы со строками.
При создании экземпляра класс не должен принимать никаких аргументов.
Класс StrExtension должен иметь три статических метода:
remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные латинские буквы
без учета регистра и возвращает полученный результат;
leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы,
не являющиеся латинскими буквами, и возвращает полученный результат;
replace_all() — метод, который принимает три строковых аргумента string, chars и char,
заменяет в строке string все символы из chars на char с учетом регистра и возвращает полученный результат.
Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.
Примечание 2. Латинские гласные буквы: a, e, i, o, u, y.
"""


class StrExtension:
    @classmethod
    def remove_vowels(cls, string: str) -> str:
        not_vowels_chars = [char for char in string if char.lower() not in ('a', 'e', 'i', 'o', 'u', 'y')]
        return ''.join(not_vowels_chars)

    @classmethod
    def leave_alpha(cls, string: str) -> str:
        alpha_chars = [char for char in string if char.isalpha()]
        return ''.join(alpha_chars)

    @classmethod
    def replace_all(cls, string: str, chars: str, char: str) -> str:
        result = [char if letter in chars else letter for letter in string]
        return ''.join(result)
        # for letter in chars:
        #     string = string.replace(letter, char)
        # return string


print(StrExtension.remove_vowels('Python'))      # Pthn
print(StrExtension.remove_vowels('Stepik'))      # Stpk

print(StrExtension.leave_alpha('Python111'))     # Python
print(StrExtension.leave_alpha('__Stepik__()'))  # Stepik

print(StrExtension.replace_all('Python', 'Ptn', '-'))   # -y-ho
print(StrExtension.replace_all('Stepik', 'stk', '#'))   # S#epi#
