class Warehouse():
    name = ''
    my_dict = {'printer': 0, 'scanner': 0, 'copier': 0}

    def __init__(self, indoor, outdoor):
        self.indoor = indoor
        self.outdoor = outdoor


    def get_in(self):
        self.my_dict[self.name] = self.indoor
        return self.my_dict.items()

    def get_out(self, y):
        self.y = y



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

p = Printer(1000, 20, 15, 20, "white")
print(p.color)
print(p.total_price())
print(p.get_in())

s = Scanner(3000, 5, 40)
print(s.weight)
print(s.total_price())
c = Copier(1500, 10, 400)
print(c.performance)
print(c.total_price())

