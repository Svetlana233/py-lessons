def personel_func(name, last_name, year, city, email, phone):
    return print(f"{name} {last_name} {year} {city} {email} {phone}")

last_name = input("введите фамилию ")
name = input("введите имя ")
year = input("введите год рождения ")
city = input("введите город ")
email = input("введите email ")
phone = input("введите phone ")

personel_func(last_name=last_name, name=name, year=year, city=city, email=email, phone=phone)