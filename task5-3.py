my_file = open('text5-3.txt', 'r')
summ = 0
cnt = 0
print('people who has the salary below 20000:')
for line in my_file:
    ls = list(line.split())
    summ += int(ls[1])
    cnt += 1
    if int(ls[1]) < 20000:
        print(ls[0])

print('average salary is', summ/cnt)