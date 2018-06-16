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
            'value': 1000,
            'admin': False
        },
        '0001-03': {
            'password': '123456',
            'name': 'Maria',
            'value': 2000,
            'admin': False
        },
        '0001-04': {
            'password': '123456',
            'name': 'Anderson',
            'value': 2000,
            'admin': True
        },
    }

    money_slips = {
        '20': 500,
        '50': 500,
        '100': 500,
    }

    if account_typed in account_list and password_typed == account_list[account_typed]['password']:
        clear = 'cls'if os.name == 'nt' else' clear'
        os.system(clear)

        print("*********************************************")
        print("***************Caixa Eletrônico**************")
        print("*********************************************")

        if account_list[account_typed]['name']:
            print('Seja bem Vindo! %s' % account_list[account_typed]['name'])

        print("1 - Saldo")
        if account_list[account_typed]['admin']:
            print("10 - Incluir Cédula")
        option_typed = input('Escolha uma opção acima: ')
        if option_typed == '1':
            print('Seu Saldo é %s' % account_list[account_typed]['value'])
        elif option_typed == '10' and account_list[account_typed]['admin']:
            amount_typed = input('Digite a quantidade de cédula: ')
            money_bill_typed = input('Digite a cédula a ser incluida: ')
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
    else:
        print('Conta Inválida')

    input('Pressione <ENTER> para continuar...')
    clear = 'cls'if os.name == 'nt' else' clear'
    os.system(clear)
