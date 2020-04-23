def my_func():
    for el in range(1, 16):
        yield el

a = 1
for el in my_func():
    a *= el

print(a)
