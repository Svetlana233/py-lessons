my_file = open('text5-2.txt', 'r')
n = 0

for line in my_file:
    n += 1
    ls = len(line.split(' '))
    print(n, 'string =', ls, 'word(s)')

print('number of srings is', n)
my_file.close()