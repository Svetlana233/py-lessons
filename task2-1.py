text = [1, -10, 2.5, 'Hello', False, None, (1, 2, 3), {4, 5, 6}]
print(list(text))

for itm in text:
    a = type(itm)
    print(itm, 'is a', a)
