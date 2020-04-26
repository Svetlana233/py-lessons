from random import randint
my_file = open('text5-5.txt', 'w')
sum = 0
st = []
ls = [randint(0, 5) for el in range(0, 10)]
for el in ls:
    sum += el
    st.append(str(el))

my_file.write(' '.join(st))

print(sum)