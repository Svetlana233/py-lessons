def my_func(x, y):
    result = x ** y
    return result

def my_func2(x, y):
    result = x
    i = 1
    while i < abs(y):
        i += 1
        result *= x
    return 1 / result

while True:
    try:
        var1 = float(input("введите положительное действительное число "))
        var2 = int(input("введите целое отрицательное число "))
        if (var1 > 0) and (var2 < 0):
            break
        else:
            print("вы ввели некорректные числа")
            continue
    except ValueError:
        print("вы ввели некорректные числа")
        continue

print(my_func(var1, var2))
print(my_func2(var1, var2))
