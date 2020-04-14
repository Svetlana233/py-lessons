while True:
    goods = input('How many goods? ')
    if goods.isdigit():
        goods = int(goods)
        break
    else:
        print('You enter the wrong number. Try again')

good_list = []
i = 0
while i < goods:
    name = input('название продукта ')
    price = input('цена продукта ')
    price = int(price)
    num = input('количество продукта ')
    num = int(num)
    meas = input('ед измерения продукта ')
    good_list.append((i + 1, {'name': name, 'price': price, 'number': num, 'measure': meas}))
    i += 1
# good_dict = {}
name_list = []
price_list = []
number_list = []
measure_list = []

for good in good_list:
    i = good[1]
    name_list.append(i["name"])
    price_list.append(i["price"])
    number_list.append(i["number"])
    measure_list.append(i["measure"])

print(good_list)
print({
'название': name_list,
'цена': price_list,
'количество': number_list,
'ед': measure_list
})
