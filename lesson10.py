class Device:
    def __init__(self,brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

        self.has_power = False

    def power(self) -> None:
        self.has_power = not self.has_power
        state = 'Включен' if self.has_power else 'Выключен'
        print(f'Устройство {self.brand} {self.model} Состаяние: {self.state}')

    def info(self) -> str:
        return f'{self.brand} {self.model} ЦЕНА: {self.price:.2f} сом'

class SmartPhone(Device):
    def __init__(self, brand, model, price, camera_mp, screen_size):
        super().__init__(brand, model, price)
        self.screen_size = screen_size
        self.camera_mp = camera_mp

    def get_info(self):
        base_info = super().info()
        return f'Смартфон: {base_info}, Экран: {self.screen_size}, Камера: {self.camera_mp}'

class Laptop(Device):
    def __init__(self, brand, model, price, cpu, gpu, ram):
        super().__init__(brand, model, price)
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram

    def get_info(self):
        return f'Ноутбук: {super().info()}, Процессор: {self.cpu}, Графический процессор: {self.gpu}, Оперативная память: {self.ram}'
    

phone = SmartPhone(brand = 'Samsung',
    model = 'Galaxy S21',
    price = 100000,
    screen_size= 12,
    camera_mp = 1080)
laptop = Laptop(
    brand ='Lenovo', 
    model = 'IdeaPad 330-15IKB', 
    price = 100000, 
    cpu = 'Intel Core i7',
    gpu = 'NVIDIA GeForce RTX 3050', ram = '8 ГБ')

print(phone.get_info())
print(laptop.get_info())

class Developer:
    def __init__(self, stack):
        self.stack = stack

    def stack_name(self):
        return self.stack, ': Рзработчик'

class BackEnd(Developer):
    def __init__(self, stack, db):
        super().__init__(stack)
        self.db = db

    def stack_name(self):
        return f'Стек: {self.stack} База данных : {self.db}'

class FrontEnd(Developer):
    def __init__(self, stack, site_element):
        super().__init__(stack)
        self.site_element = site_element

    def stack_name(self):
        return f'Стек: {self.stack} Элемент сайта{self.site_element}'

dev = Developer('Junior')
back = BackEnd('Python', 'MySQL')
front = FrontEnd('HTML', 'HTML/CSS')

razrabotchiki = [dev, back, front]

# for chelovek in razrabotchiki:
#     print(chelovek.stack_name())

# print(dev.stack_name())