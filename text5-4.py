import shutil
my_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
    }

my_file = open('text5-4.txt', 'r', encoding='UTF-8')
new_file = open('new_file5-4.txt', 'w', encoding='UTF-8')

for line in my_file:
    ls = line.split()
    ls[0] = my_dict[ls[0]]
    new_file.write(' '.join(ls) + '\n')

my_file.close()
new_file.close()