class Car():
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return "Машина поехала"
    def stop(self):
        return "Машина остановилась"
    def turn(self, direction):
        return "Машина повернула " + direction
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed > 60:
            return "Скорость превышена"

class SportCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if int(self.speed) > 160:
            return "Скорость превышена"

class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if int(self.speed) > 40:
            return "Скорость превышена"

class PoliceCar(Car):
    def police(self):
        if self.is_police is True:
            return "Полицейская машина"
        else:
            return "Не полицейская машина"


car1 = PoliceCar(90, 'white', 'Audi', True)
car2 = WorkCar(50, 'red', 'BMW')
car3 = PoliceCar(90, 'green', 'Mini', True)
car4 = WorkCar(30, 'black', 'Mercsedes')
car5 = TownCar(90, 'grey', 'Volvo')
print(car1.show_speed(), car1.police(), car1.go(), car1.turn('направо'))
print(car2.show_speed(60), car2.stop())
print(car3.show_speed(), car3.police())
print(car4.show_speed(70))
print(car5.show_speed(90))

# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
# .
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).

# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, # который должен показывать текущую скорость автомобиля.
#
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.