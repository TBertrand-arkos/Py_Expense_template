from secrets import choice
from PyInquirer import prompt

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices":[
            # choice.split(',',1)[0] for choice in open('users.csv').read().splitlines()
            choice for choice in open('users.csv').read().splitlines()
        ]
    },
    {
        "type":"checkbox",
        "name":"involved_users",
        "message":"New Expense - Involved Users: ",
        "choices":[
            {"name": choice} for choice in open('users.csv').read().splitlines()
        ]
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    amount = infos['amount']
    label = infos['label']
    spender = infos['spender'].split(',',1)[0]
    involved_users = infos['involved_users']
    amount_per_user = float(amount) / (len(involved_users)+1)
    # put into csv file
    with open('expenses.csv', 'a') as f:
            f.write(f'spender,{spender},{str(amount_per_user)},{label}\n')
    for user in involved_users:
        user = user.split(',',1)[0]
        with open('expenses.csv', 'a') as f:
            f.write(f'involved,{user},{str(amount_per_user)},{label},{spender}\n')
    print("Expense Added !")
    return True


