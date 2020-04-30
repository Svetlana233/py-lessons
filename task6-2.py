class Road():
    _length = 0
    _width = 0
    _thickness = 5
    _weigt = 25

    def __init__(self, w, l):
        self._length = l
        self._width = w

    def get_mass(self):
        result = self._length * self._width * self._thickness * self._weigt
        return result

road1 = Road(20, 5000)

a = road1.get_mass()

print(a)



