# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Warehouse():
    pass

class Equipment():
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

class Printer(Equipment):
    def __init__(self, price, quantity, color):
        super().__init__(price, quantity)
        self.color = color

class Scanner(Equipment):
    def __init__(self, price, quantity, weight):
        super().__init__(price, quantity)
        self.weight = weight

class Copier(Equipment):
    def __init__(self, price, quantity, performance):
        super().__init__(price, quantity)
        self.performance = performance

p = Printer(1000, 20, "white")
print(p.color)
print(p.total_price())
s = Scanner(3000, 5, 40)
print(s.weight)
print(s.total_price())
c = Copier(1500, 10, 400)
print(c.performance)
print(c.total_price())
