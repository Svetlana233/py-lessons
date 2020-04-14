my_list = [7, 6, 5, 5, 3, 2]
while True:
    rating = input('Please enter a rating ')
    if rating.isdigit():
        rating = int(rating)
        break
    else:
        print('You enter the wrong number. Try again')

my_list.append(rating)
print(my_list)

my_list.sort()
my_list.reverse()
print(my_list)

