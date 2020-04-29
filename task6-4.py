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
            print("скорость превышена")

# class SportCar(Car):

class WorkCar(Car):
    def show_speed_wcar(self, speed):
        self.speed = speed
        if self.speed > 40:
            print("скорость превышена")

class PoliceCar(Car):
    def police(self):
        if self.is_police is True:
            print("Полицейская машина")


car1 = PoliceCar(90, 'red', 'ferary', True)
car2 = WorkCar(90, 'red', 'jipp', True)
car3 = PoliceCar(90, 'red', 'ferary', True)
car4 = PoliceCar(90, 'red', 'ferary', True)
car5 = TownCar(90, 'red', 'ferary', True)
print(car1.turn('направо'))
print(car1.go())
print(car1.police())
print(car5.show_speed_tcar())

# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.