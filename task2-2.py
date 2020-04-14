my_list = list(input('Please enter a list '))

print(list(my_list))
a = len(my_list) - 1
for i in range(a):
    if i % 2 == 0 and i < a:
        buf = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = buf
print(my_list)
