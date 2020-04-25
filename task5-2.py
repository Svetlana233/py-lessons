my_file = open('text5-2.txt', 'r')
n = 0

for line in my_file:
    words = 0
    n += 1
    ls = line.split(' ')
    for itm in ls:
        words += 1
    print(n, 'string is', words, 'word(s)')

print('number of srings is', n)