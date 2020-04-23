from itertools import count, cycle
ls = []
for i in count(10):
    if i > 15:
        break
    else:
        ls.append(i)
print(ls)
c = 0
for el in cycle(ls):
    if c > 20:
        break
    print(el)
    c += 1

