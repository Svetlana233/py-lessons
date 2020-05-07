class Warehouse():
    name = ''
    my_dict = {'printer': 0, 'scanner': 0, 'copier': 0}
    sub_dict = {'printer': 0, 'scanner': 0, 'copier': 0}

    def __init__(self, indoor, outdoor):
        self.indoor = indoor
        self.outdoor = outdoor

# пополнение склада:
    def get_in(self):
        self.my_dict[self.name] = self.indoor
        return self.my_dict.items()

# передача техники в департамент:
    def get_out(self):
        self.sub_dict[self.name] = self.outdoor
        return self.sub_dict.items()

class Equipment():
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return self.price * self.quantity

class Printer(Equipment, Warehouse):
    name = 'printer'
    def __init__(self, price, quantity, indoor, outdoor, color):
        super().__init__(price, quantity)
        Warehouse.__init__(self, indoor, outdoor)
        self.color = color

class Scanner(Equipment, Warehouse):
    name = 'scanner'
    def __init__(self, price, quantity, indoor, outdoor, weight):
        super().__init__(price, quantity)
        Warehouse.__init__(self, indoor, outdoor)
        self.weight = weight

class Copier(Equipment, Warehouse):
    name = 'copier'
    def __init__(self, price, quantity, indoor, outdoor, performance):
        super().__init__(price, quantity)
        Warehouse.__init__(self, indoor, outdoor)
        self.performance = performance

p = Printer(1000, 20, 15, 10, "white")
print('The color of printers is', p.color)
print('Total price for all printers', p.total_price(), 'Rub')
print('Current stock status: ', p.get_in())
print('At the disposal of the finance department:', p.get_out())
print('________________________________________________________________________________')
s = Scanner(3000, 5, 3, 1, 40)
print('weight of scanner:', s.weight, 'kg')
print('Total price for all scanners', s.total_price(), 'Rub')
print('Current stock status: ', s.get_in())
print('At the disposal of the finance department:', s.get_out())
print('________________________________________________________________________________')
c = Copier(1500, 10, 5, 4, 400)
print('Performance of the copier is ', c.performance, 'sheets per minute')
print('Total price for all copiers', c.total_price(), 'Rub')
print('Current stock status: ', c.get_in())
print('At the disposal of the finance department:', c.get_out())