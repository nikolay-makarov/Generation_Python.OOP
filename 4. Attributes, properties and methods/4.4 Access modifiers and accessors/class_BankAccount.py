"""Класс BankAccount
Реализуйте класс BankAccount, описывающий банковский счет.
При создании экземпляра класс должен принимать один аргумент:
balance — баланс счета, по умолчанию имеет значение 0.
Экземпляр класса BankAccount должен иметь один атрибут:
_balance — баланс счета
Класс BankAccount должен иметь четыре метода экземпляра:
- get_balance() — метод, возвращающий актуальный баланс счета,
- deposit() — метод, принимающий в качестве аргумента число amount и увеличивающий баланс счета на amount,
- withdraw() — метод, принимающий в качестве аргумента число amount и уменьшающий баланс счета на amount.
Если amount превышает количество средств на балансе счета, должно быть возбуждено исключение ValueError с сообщением:
На счете недостаточно средств
- transfer() — метод, принимающий в качестве аргументов банковский счет account и число amount.
Метод должен уменьшать баланс текущего счета на amount и увеличивать баланс счета account на amount.
Если amount превышает количество средств на балансе текущего счета, должно быть возбуждено исключение ValueError
с сообщением: На счете недостаточно средств
"""


class BankAccount:

    def __init__(self, balance: int | float = 0) -> None:
        self._balance = balance

    def get_balance(self) -> int | float:
        return self._balance

    def deposit(self, amount: int | float) -> None:
        self._balance += amount

    def withdraw(self, amount: int | float) -> None:
        if amount > self.get_balance():
            raise ValueError('На счете недостаточно средств')
        self._balance -= amount

    def transfer(self, account: 'BankAccount', amount: int | float) -> None:
        self.withdraw(amount)
        account.deposit(amount)


account1 = BankAccount(100)
account2 = BankAccount(200)

try:
    account1.transfer(account2, 150)  # На счете недостаточно средств
except ValueError as e:
    print(e)

account = BankAccount()

print(account.get_balance())  # 0
account.deposit(100)
print(account.get_balance())  # 100
account.withdraw(50)
print(account.get_balance())  # 50
