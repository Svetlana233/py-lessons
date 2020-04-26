import re
my_dict = {}

def get_sum(a):
    temp = re.findall(r'\d+', a)
    ls = [int(el) for el in temp]
    return sum(ls)

with open('text5-6.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        frst_el = line.split(':')[0]
        my_dict[frst_el] = get_sum(line)
print(my_dict)