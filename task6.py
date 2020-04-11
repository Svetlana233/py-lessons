# запрашиваем показатели отчетности у пользователя
while True:
    result = input('Please enter result for the first day ')
    if result.isdigit():
        result = int(result)
        break
    else:
        print('You enter the wrong number. Try again')
while True:
    total = input('Please enter total sum of km ')
    if total.isdigit():
        total = int(total)
        break
    else:
        print('You enter the wrong number. Try again')

# расчет
day = 1
while result < total:
    print('{0}-й день {1} км.'.format(day, format(result, '.2f')))
    result = result * 1.1
    day = day + 1
print('{0}-й день {1} км.'.format(day, format(result, '.2f')))
print('на {}-й день спортсмен достиг результата — не менее {} км.'.format(day, total))
