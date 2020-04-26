my_file = open("text.txt", "w")
str_list = input('Enter some text ')
new_list = str_list.split(' ')

for itm in new_list:
    my_file.write(itm + '\n')

my_file.close()
