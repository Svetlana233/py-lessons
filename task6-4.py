class Car():
    speed = 0
    color = ''
    name = ''
    is_police = [True, False]

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return print("Машина поехала")
    def stop(self):
        return print("Машина остановилась")
    def turn(self, direction):
        return print("Машина повернула", direction)
    def show_speed(self):
       return print(self.speed)

class TownCar(Car):
    def show_speed_tcar(self, speed):
        self.speed = speed
        if self.speed > 60:
            print("Скорость превышена")

# class SportCar(Car):

class WorkCar(Car):
    def show_speed_wcar(self, speed):
        self.speed = speed
        if self.speed > 40:
            print("Скорость превышена")

class PoliceCar(Car):
    def police(self):
        if self.is_police is True:
            print("Полицейская машина")
        else:
            print("Не полицейская машина")


car1 = PoliceCar(90, 'white', 'Audi', True)
car2 = WorkCar(50, 'red', 'BMW', True)
car3 = PoliceCar(90, 'green', 'Mini', False)
car4 = WorkCar(30, 'black', 'Mercsedes', True)
car5 = TownCar(90, 'grey', 'Volvo', True)
print(car1.__init__(90, 'white', 'Audi', True), car1.police(), car1.go(), car1.turn('направо'))
print(car2.__init__(50, 'red', 'BMW', True), car2.stop(), car2.show_speed_wcar())
print(car3.__init__(90, 'green', 'Mini', False), car3.police())
print(car4.__init__(30, 'black', 'Mercsedes', True), car4.show_speed_wcar())
print(car5.__init__(90, 'grey', 'Volvo', True), car5.show_speed_tcar())

# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.