from random import randint
ls = []
i = 1
for i in range(1, 10):
    ls.append(randint(0, 100))
    i += 1
print(ls)

new_list = []

for j in range(len(ls)):
    if (j > 0) and (ls[j] > ls[j-1]):
        new_list.append(ls[j])

print(new_list)