from PyInquirer import prompt
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"User creation - name: ",
    },
    {
        "type":"input",
        "name":"email",
        "message":"User creation - email: ",
    },
    {
        "type":"input",
        "name":"iban",
        "message":"User creation - IBAN: ",
    },
]

def add_user():
    infos = prompt(user_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    name = infos['name']
    email = infos['email']
    iban = infos['iban']
    # put into csv file
    with open('users.csv', 'a') as f:
        f.write(f'{name},{email},{iban}')
    print("User Added !")
    return True