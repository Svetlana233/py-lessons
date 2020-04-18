def sp_func(s):
    l = s.split(' ')
    summary = 0
    is_symbol = False
    for itm in l:
        try:
            summary += int(itm)
        except ValueError:
            is_symbol = True
            return (summary, is_symbol)
    return (summary, is_symbol)

def my_func(result = 0):
    l = input('введите числа через пробел ')
    a = sp_func(l)
    result += a[0]
    print(result)
    if a[1] is False:
        my_func(result)

my_func()
# i = 0
# result = 0
# while i == 0:
#     l = input('введите числа через пробел ')
#     a = sp_func(l)
#     result += a[0]
#     print(result)
#     if a[1] is False:
#         continue
#     else:
#         i += 1

