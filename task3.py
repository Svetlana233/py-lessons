# запрашиваем число
while True:
    number = input('Please enter an integer number ')
    if number.isdigit():
        number = int(number)
        break
    else:
        print('You enter the wrong number. Try again')

number1 = str(number)
number2 = number1 * 2
number3 = number1 * 3
result = int(number1) + int(number2) + int(number3)
print(number1,'+',number2,'+',number3,'=',result)
