from re import U
from PyInquirer import prompt

def status():
    users = dict()
    with open('users.csv') as f:
        lines = f.read().splitlines()
        for line in lines:
           users[line.split(',',1)[0]] = {'owns': {}}

    with open('expenses.csv') as f:
        lines = f.read().splitlines()
        for line in lines:
            if(line.split(',')[0] == 'involved'):
                amount = line.split(',')[2]
                user = line.split(',')[1]
                spender = line.split(',')[4]
                if(spender in users[user]['owns']):
                    users[user]['owns'][spender] += float(amount)
                else:
                    users[user]['owns'][spender] = float(amount)

    for user in users:
        owns = users[user]['owns']
        if(len(owns) > 0):
            print(f"{user}:")
            for own in owns:
                print(f"\t owes {own} {owns[own]:.2f}€")
        else:
            print(f"{user} owes nothing")
    return True