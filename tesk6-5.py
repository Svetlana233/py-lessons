class Stationery():
    title = ''

    def draw(self):
        print('запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('рисую ручкой')
class Pencil(Stationery):
    def draw(self):
        print('рисую карандашом')
class Handle(Stationery):
    def draw(self):
        print('рисую маркером')

a1 = Stationery()
a2 = Pen()
a3 = Pencil()
a4 = Handle()

a1.draw()
a2.draw()
a3.draw()
a4.draw()
