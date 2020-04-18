def my_func(x, y, z):
    c = x + y + z - min(x, y, z)
    return c

while True:
    try:
        x = int(input("введите первое число "))
        y = int(input("введите второе число "))
        z = int(input("введите третье число "))
        break
    except ValueError:
        print("вы ввели неверное значение. попробуйте еще раз")
        continue

print(my_func(x, y, z))
