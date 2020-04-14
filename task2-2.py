my_list = ["a", "b", "c", 1, 3]
a = len(my_list) - 1
for i in range(a):
    print(i)
    if i % 2 == 0 and i < a:
        print(my_list[i])
        buf = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = buf
print(my_list)
