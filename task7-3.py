class Cell():

    def __init__(self, count):
        self.count = count

    def __str__(self):
        return str(self.count)

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        a = self.count - other.count
        if a > 0:
            Cell(a)
        else:
            return 'Number of cells can`t be less 0'

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, row_count):
        cells = ''
        i = 0
        st_num = self.count // row_count
        last_num = self.count % row_count
        while i < st_num:
            cells += '*' * row_count  + '\n'
            i += 1
        cells += '*' * last_num
        return cells

c1 = Cell(15)
c2 = Cell(20)
a1 = c1 + c2
a2 = c1 / c2
a3 = c1 * c2
a4 = c1 - c2

print(a1)
print(a2)
print(a3)
print(a4)

print(c1.make_order(4))

print(a3.make_order(19))