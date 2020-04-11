# запрашиваем показатели отчетности у пользователя
while True:
    rev = input('Please enter Revenue in USD ')
    if  rev.isdigit():
        rev = int(rev)
        break
    else: print('You enter the wrong number. Try again')

while True:
        cost = input('Please enter Costs in USD ')
        if cost.isdigit():
            cost = int(cost)
            break
        else:
            print('You enter the wrong number. Try again')

# проверяем результат работы компании
if rev > cost:
    profit = rev - cost
    print('Your company is operating with a profit', profit, 'USD')
    profitability = profit / rev
    print("Profitability is", format(profitability, '.2f'))
    while True:
        staff = input('Please enter number of staff ')
        if staff.isdigit():
            staff = int(staff)
            break
        else:
            print('You enter the wrong number. Try again')
    a = profit / staff
    print ('Profit per one employee is', int(a), 'USD')
elif rev == cost:
    print('Your company have no profit')
else:
    loss = rev - cost
    print('Your company is operating at a loss', loss, 'USD')

