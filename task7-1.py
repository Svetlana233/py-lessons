class Matrix():
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        s = ''
        for ls in self.lists:
            l = [str(a) for a in ls]
            st = ''
            for el in l:
                st += "{:>10}".format(el)
            s += st + '\n'
        return s

    def __add__(self, other):
        i = 0
        total = []
        for ls in self.lists:
            result = []
            j = 0
            for el in ls:
                result.append(el + other.lists[i][j])
                j += 1
            total.append(result)
            i += 1
        return Matrix(total)

m1 = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
print(m1)
m2 = Matrix([[11, 0, 13], [113, 114, 5], [1000, 7, 8]])
print(m2)
c = m1 + m2
print(c)

