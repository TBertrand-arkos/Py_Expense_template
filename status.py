from re import U
from PyInquirer import prompt
import re

continue_questions = [
    {
        "type":"confirm",
        "name":"confirm",
        "message":"Do you wish to edit some debts ?",
    },
]

edit_debts = [
    {
        "type":"list",
        "name":"spender",
        "message":"Pay you debts - select the Users: ",
        "choices":[
            {"name": choice} for choice in open('users.csv').read().splitlines()
        ]
    },
    {
        "type":"list",
        "name":"involved_users",
        "message":"Pay you debts - select the Users: ",
        "choices":[
            {"name": choice} for choice in open('users.csv').read().splitlines()
        ]
    },
    {
        "type":"input",
        "name":"amount",
        "message":"Pay you debts - Amount: ",
        'validate': lambda x: bool(re.match(r'^[0-9]+$',x)) or "Please enter a valid amount"
    },
]

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

    infos_continue = prompt(continue_questions)
    if(infos_continue['confirm']): 
        infos_edit = prompt(edit_debts)
        spender = infos_edit['spender'].split(',',1)[0]
        involved_users = infos_edit['involved_users'].split(',',1)[0]
        amount = infos_edit['amount'] * -1
        if(amount != ''):
            with open('expenses.csv', 'a') as f:
                f.write(f'involved,{involved_users},{str(amount)},payment,{spender}\n')
    return True