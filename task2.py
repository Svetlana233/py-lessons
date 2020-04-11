# запрашиваем время в секундах
while True:
    what_time = input('Please enter time in seconds ')
    if what_time.isdigit():
        what_time = int(what_time)
        break
    else: print('You enter the wrong time. Try again')

# считаем часы, минуты, секyнды
hh = what_time // 3600
mm = what_time % 3600 // 60
ss = what_time % 60
print('{0:>02}:{1:>02}:{2:>02}'.format(hh,mm,ss))

