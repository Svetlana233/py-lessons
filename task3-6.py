import re

# функция проверки на маленькие латинские буквы
def is_valid(a):
    prog = re.compile(r'^[a-z]+$')
    return prog.match(a)

# функция замены первой буквы на заглавную
def word_func(w):
    return w.title()

while True:
    word = input('введите слово маленькими латинскими буквами ')
    if is_valid(word):
        print(word_func(word))
        break
    else:
        continue

# функция преобразования для списка
def lst_func():
    ls = str(input('введите слова маленькими латинскими буквами '))
    if is_valid(ls.replace(' ','')):
        l = ls.split(' ')
        for ind in range(len(l)):
            l[ind] = word_func(l[ind])
        print(' '.join(l))

    else:
        lst_func()

lst_func()

