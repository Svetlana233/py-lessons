def func():
    try:
        a = float(input("введите первое число "))
        b = float(input("введите второе число "))
    except ValueError:
        return
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return

result = func()
if result != None:
    print("%.2f" % result)
else:
    print(result)