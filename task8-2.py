# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

num1 = input("Enter 1st number ")
num2 = input("Enter 2nd number ")

try:
    result = int(num1) / int(num2)
except ValueError:
    print("You enter not a number, try again")
except ZeroDivisionError:
    print("You cannot be divided by zero, enter another number")
except OwnError as err:
    print(err)
else:
    print(f"The result of division is: {result}")