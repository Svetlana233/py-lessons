import json
my_firm = {}
my_prof = {}
my_loss = {}
profit_total = 0
i = 0
with open('text5-7.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        ls = line.split()
        profit = int(ls[2]) - int(ls[3])
        if profit >= 0:
            my_firm[ls[0]] = profit
            profit_total += profit
            i += 1
        else:
            my_loss[ls[0]] = profit
my_prof['average_profit'] = profit_total/i

with open('my_file.json', "w") as write_f:
    json.dump([my_firm, my_prof, my_loss], write_f)