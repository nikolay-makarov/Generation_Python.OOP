"""Класс Wordplay
Будем называть словом любую последовательность из одной или более латинских букв.
Реализуйте класс Wordplay, описывающий расширяемый набор слов.
При создании экземпляра класс должен принимать один аргумент:
- words — список, определяющий начальный набор слов. Если не передан, начальный набор слов считается пустым
Экземпляр класса Wordplay должен иметь один атрибут:
- words — список, содержащий набор слов.
Класс Wordplay должен иметь четыре метода экземпляра:
- add_word() — метод, принимающий в качестве аргумента слово и добавляющий его в набор.
Если слово уже есть в наборе, метод ничего не должен делать;
- words_with_length() — метод, принимающий в качестве аргумента натуральное число n
и возвращающий список слов из набора, длина которых равна n;
- only() — метод, принимающий произвольное количество аргументов — букв, и возвращающий все слова из набора,
которые включают в себя только переданные буквы;
- avoid() — метод, принимающий произвольное количество аргументов — букв,
и возвращающий все слова из списка words, которые не содержат ни одну из этих букв.
Примечание 1. Слова в списках, возвращаемых методами words_with_length(), only() и avoid(),
должны располагаться в том порядке, в котором они были добавлены.
Примечание 2. Экземпляр класса Wordplay не должен зависеть от списка, на основе которого он был создан.
Другими словами, если исходный список изменится, то экземпляр класса Wordplay измениться не должен.
"""


class Wordplay:
    def __init__(self, words: list[str] | None = None) -> None:
        if words is None:
            words = []
        self.words: list = words.copy()

    def add_word(self, word: str) -> None:
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int) -> list[str]:
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args: str):
        result = []
        for word in self.words:
            w = word
            for letter in args:
                w = w.replace(letter, '')
            if not w:
                result.append(word)
        return result

    def avoid(self, *args: str):
        result = []
        for word in self.words:
            is_avoid = True
            for letter in args:
                if letter in word:
                    is_avoid = False
                    break
            if is_avoid:
                result.append(word)
        return result


words = ['Лейбниц', 'Бэббидж', 'Нейман', 'Джобс', 'да_Винчи', 'Касперский']
wordplay = Wordplay(words)

words.extend(['Гуев', 'Харисов', 'Светкин'])
print(words)
print(wordplay.words)
