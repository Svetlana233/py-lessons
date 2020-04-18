def func(x, y):
    try:
        z = x / y
        return z
    except ZeroDivisionError:
        return

while True:
    try:
        a = float(input("введите первое число "))
        b = float(input("введите второе число "))
        break
    except ValueError:
        print("вы ввели неверное значение, попробуйте еще раз")
        continue

result = func(a, b)

if result != None:
    print("%.2f" % result)
else:
    print(result)