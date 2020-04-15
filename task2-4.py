# запрос текста
my_list = input('Please enter a list ')

# формирование списка
new_list = my_list.split(' ')
print(new_list)

# итоговый вывод результата
s = len(new_list)
print(s)
for itm in range(s):
    print('{0}  {1}'.format(itm + 1, new_list[itm][0:10]))
