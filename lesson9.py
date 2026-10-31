# class Cat:
#     def __init__(self, name: str, color: str):
#         self.name = name
#         self.color = color

#     def meow(self):
#         print(f'{self.name} Мяу-Мяу') 

# cat1 = Cat(name = 'Барсик', color = 'Рыжий')
# print(cat1.name, cat1.color)

# cat1.meow()

# cat2 = Cat(name = 'Черный', color = 'Белый')
# print(cat2.name, cat2.color)


# class PiggyBank:
#     def __init__(self, owner):
#         self.owner = owner
#         self.coins = 0

#     def add_money(self, amount: int):
#         if amount > 0:
#             self.coins += amount
#             print(f'В копилку  {self.owner} добавлено {amount} монет, теперь у вас {self.coins} монет')
#         else:
#             print('Некорректный ввод')

#     def remove_money(self) -> int:
#         saved = self.coins
#         self.coins = 0
#         print(f'Вы разбили копилку {self.owner} там было {saved} монет')
#         return saved

# mr_piggy = PiggyBank('Мурзик')
# mr_piggy.add_money(100)
# mr_piggy.add_money(500)
# mr_piggy.add_money(10000)



# cash = mr_piggy.remove_money()
# print(f'У нас на руках теперь: {cash} монет')
# print(f'остаток в копилке: {mr_piggy.coins} монет')


