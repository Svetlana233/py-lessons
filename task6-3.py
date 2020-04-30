class Worker():
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus

class Position(Worker):
    def get_full_name(self):
        return '{} {}'.format(self.surname, self.name)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

worker1 = Position("Sveta", "SSS", "Manager", 100000, 50000)

print(worker1.get_full_name())
print(worker1.get_total_income())