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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    amount = infos['amount']
    label = infos['label']
    spender = infos['spender']
    # put into csv file
    with open('expense.csv', 'a') as f:
        f.write(f'{amount},{label},{spender}')
    print("Expense Added !")
    return True


