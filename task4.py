# запрашиваем число
while True:
    number = input('Please enter a number from 0 ')
    if  number.isdigit():
        number = int(number)
        break
    else: print('You enter the wrong number. Try again')
# print(number)

# ищем максимальную цифру
a = number
maximum = 0
b = 0
while number > 0:
    b = number % 10
    if maximum <= b:
        maximum = b
    number = (number - b) / 10

print('Maximum number in', a, 'is',int(maximum))

