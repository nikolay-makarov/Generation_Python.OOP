"""Класс Todo
Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Todo должен иметь один атрибут:
- things — изначально пустой список дел, которые нужно выполнить
Класс Todo должен иметь четыре метода экземпляра:
- add() — метод, принимающий название дела и его приоритет (целое число) и
добавляющий данное дело в список дел в виде кортежа: (<название дела>, <приоритет>)
- get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел,
имеющих приоритет n;
- get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
- get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет
"""


class Todo:
    def __init__(self) -> None:
        self.things: list = list()

    def add(self, name: str, priority: int) -> None:
        self.things.append((name, priority))

    def get_by_priority(self, number) -> list[str]:
        return [name for name, priority in self.things if priority == number]

    def get_low_priority(self) -> list[str]:
        if not self.things:
            return []
        min_priority = min((priority for _, priority in self.things))
        return [name for name, priority in self.things if priority == min_priority]

    def get_high_priority(self) -> list[str]:
        if not self.things:
            return []
        max_priority = max((priority for _, priority in self.things))
        return [name for name, priority in self.things if priority == max_priority]


todo = Todo()

todo.add('Проснуться', 3)
todo.add('Помыться', 2)
todo.add('Поесть', 2)

print(todo.get_by_priority(2))  # ['Помыться', 'Поесть']
