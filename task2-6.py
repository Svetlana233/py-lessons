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
    name = input('Name of the product ')
    while True:
        price = input('Product`s price ')
        if price.isdigit():
            price = int(price)
            break
        else:
            print('You enter the wrong number. Try again')
    while True:
        num = input('Product`s quantity ')
        if q.isdigit():
            q = int(q)
            break
        else:
            print('You enter the wrong number. Try again')
    meas = input('ед измерения продукта ')
    good_list.append((i + 1, {'name': name, 'price': price, 'quantity': q, 'measure': meas}))
    i += 1

name_list = []
price_list = []
quantity_list = []
measure_list = []

for good in good_list:
    i = good[1]
    name_list.append(i["name"])
    price_list.append(i["price"])
    quantity_list.append(i["quantity"])
    measure_list.append(i["measure"])

print(good_list)
print({
'название': name_list,
'цена': price_list,
'количество': quantity_list,
'ед': measure_list
})
