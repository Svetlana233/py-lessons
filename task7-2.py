class Clothes():

    def __init__(self,  v=0, h=0):
        self.v = v
        self.h = h

class Suit(Clothes):

    @property
    def total_cloth(self):
        return 2 * self.h + 0.3

class Coat(Clothes):

    @property
    def total_cloth(self):
        return self.v/6.5 + 0.5

s = Suit(h=5)
c = Coat(v=26)

print(s.total_cloth, c.total_cloth)