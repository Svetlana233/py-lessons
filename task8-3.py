class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
s = []
a = True
while a == True:
    num1 = input("Enter number ")
    try:
        result = int(num1)
        s.append(num1)
    except ValueError:
        print("You enter not a number")
    except OwnError as err:
        print(err)
    if num1 == 'stop':
        a = False

print(s)