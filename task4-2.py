from random import randint
ls = []
ls = [randint(1, 10) for el in range(1, 15)]
print(ls)

new_list = []

for j in range(len(ls)):
    if (j > 0) and (ls[j] > ls[j-1]):
        new_list.append(ls[j])

print(new_list)