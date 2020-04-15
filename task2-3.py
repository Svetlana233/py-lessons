while True:
    month = input('Please enter a month from 1 to 12 ')
    if month.isdigit() and 1 <= int(month) <= 12:
        month = int(month)
        break
    else:
        print('You enter the wrong number. Try again')

# вариант список
seasons = [
    'winter', 'winter', 'spring', 'spring', 'spring', 'summer',
    'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter'
    ]
print(seasons[month - 1])

# вариант словарь
d = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter'
    }
print(d[month])
