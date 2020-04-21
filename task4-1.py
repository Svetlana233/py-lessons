from sys import argv

employee_wage, hours, rate, premium = argv

def wage(t,s,p):
    try:
        return float(t) * float(s) + float(p)
    except ValueError:
        return print('wrong parameters')

print(wage(hours, rate, premium))