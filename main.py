import getpass
import os

while True:
    print("*********************************************")
    print("***************Caixa Eletrônico**************")
    print("*********************************************")

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')
    print(account_typed)

    #Agência, Senha, Nome, Valor
    account_list = {
        '0001-02': {
            'password': '12345',
            'name': 'José',
            'value': 1000
        },
        '0001-03': {
            'password': '123456',
            'name': 'Maria',
            'value': 2000
        }
    }
    if account_typed in account_list and password_typed == account_list[account_typed]['password']:
        os.system('cls'if os.name == 'nt' else' clear')
        print("*********************************************")
        print("***************Caixa Eletrônico**************")
        print("*********************************************")
        print("1 - Saldo")
        option_typed = input('Escolha uma opção acima: ')
        if option_typed == '1':
            print('Seu Saldo é %s' % account_list[account_typed]['value'])
    else:
        print('Conta Inválida')

    input('Pressione <ENTER> para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')
