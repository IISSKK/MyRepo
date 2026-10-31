import re

class SecureAccount:
    def __init__(self, name, email,pin, initial_balance,):
        self.name = name
        self._email = email
        self.__pin = pin
        self.initial_balance = initial_balance


    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, new_email) -> None:
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, new_email):
            raise ValueError("Invalid email format")
        print(f'Имейл успешно изменен{self._email} -> {new_email}')
        self._email = new_email
    
    @property
    def balance(self):
        return self.initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            print(f'Пополнение на: {amount}, баланс: {self.initial_balance}')
    
    def withdraw(self,pin, amount):
        if pin != self.__pin:
            print('Неверный пин код, повторите попытку')
        if amount > self.initial_balance:
            print('Недостаточно средств')
            return

        self.initial_balance -= amount
        print(f'Списание: {amount}, баланс: {self.initial_balance}')


user = SecureAccount('Альбус дамблдор', 'aloetokola@gmail.com', initial_balance=1000000, pin=1234)
print(user.name)
print(user.email)
print(user.initial_balance)

user.email = 'aloetokola@gmail.com'
user.withdraw(1234, 10000)
user.deposit(10000)
user.withdraw(1234, 10000)

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, ):
        print('Hello')

class Payment1:
    def pay(self, ):
        print('BYE')

class MBank(Payment):
        def pay(self, ):
            print(f'[MBank], Вы используете этот банк')

class OBank(Payment):
    def pay(self, ):
        print(f'[MBank], Вы используете этот банк')
class Simbank(Payment):
    def pay(self, ):
        print(f'[Simbank], Вы используете этот банк')

class OptimaBank(Payment):
    def pay(self, ):
        print(f'[OptimaBank], Вы используете этот банк')

mbank = MBank
obank = OBank
optimabank = OptimaBank
simbanl = Simbank

mbank.pay()
obank.pay()
optimabank.pay()
simbanl.pay()

