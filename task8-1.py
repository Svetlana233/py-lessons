class Date():
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def parse_int(cls, date):
        new_date = date.split('-')
        try:
            return [int(el) for el in new_date]
        except ValueError:
            print('Invalid date!')

    @staticmethod
    def check_date(date):
        new_date = Date.parse_int(date)
        st = []
        is_correct = [False, False, False]
        d = {30: [1, 3, 5, 7, 8, 10, 12, 4, 6, 9, 11],
             31: [1, 3, 5, 7, 8, 10, 12]}
        if 0 <= new_date[2]:
            is_correct.pop(2)
            is_correct.insert(2, True)
        else:
            print('Date is not correct')

        if 1 <= new_date[1] <= 12:
             is_correct.pop(1)
             is_correct.insert(1, True)
        else:
            print('You enter the wrong month')

        if is_correct[1] is True:
            day = new_date[0]
            if day == 30:
                v = d.get(day)
                if v.index(new_date[1]) in v:
                    is_correct.pop(0)
                    is_correct.insert(0, True)
                else:
                    print('You enter the wrong d')
            elif day == 31:
                v = d.get(day)
                if v.index(new_date[1]) in v:
                    is_correct.pop(0)
                    is_correct.insert(0, True)
                else:
                    print('You enter the wrong dd')
            elif day > 31:
                print('You enter the wrong ddd')
            else:
                is_correct.pop(0)
                is_correct.insert(0, True)
        else:
            print(is_correct)

mc = Date('30-04-ttt')
mc.parse_int('30-04-ttt')
mc.check_date('31-06-2000')

# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.