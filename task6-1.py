import time

class TrafficLight:
    __tl_color = ''

    def on_tl(self):
        while True:
            self.__tl_color = 'red'
            print(self.__tl_color)
            time.sleep(7)
            self.__tl_color = 'yellow'
            print(self.__tl_color)
            time.sleep(2)
            self.__tl_color = 'green'
            print(self.__tl_color)
            time.sleep(5)

trl1 = TrafficLight()
trl1.on_tl()
