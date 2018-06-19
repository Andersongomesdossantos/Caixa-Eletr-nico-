import getpass
import os

account_list = {
    '0001-02': {
        'password': '12345',
        'name': 'José',
        'value': 100,
        'admin': False
    },
    '0001-03': {
        'password': '123456',
        'name': 'Maria',
        'value': 50,
        'admin': False
    },
    '0001-04': {
        'password': '123456',
        'name': 'Anderson',
        'value': 1000,
        'admin': True
    },
}

money_slips = {
    '20': 5,
    '50': 5,
    '100': 5,
}

while True:
    print("*********************************************")
    print("***************Caixa Eletrônico**************")
    print("*********************************************")

    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')
    print(account_typed)

    if account_typed in account_list and password_typed == account_list[account_typed]['password']:
        clear = 'cls'if os.name == 'nt' else' clear'
        os.system(clear)

        print("*********************************************")
        print("***************Caixa Eletrônico**************")
        print("*********************************************")

        if account_list[account_typed]['name']:
            print('Seja bem Vindo! %s' % account_list[account_typed]['name'])

        print("1 - Saldo")
        print("2 - saque")
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
        elif option_typed == '2':
            value_typed = input('Digite o valor a ser sacado: ')

            money_slips_user = {}
            value_int = int(value_typed)

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100

            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50

            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20

            if value_int != 0:
                print("O caixa não tem cédula disponível para este valor")
            else:
                print('Pegue as notas: ')
                print(money_slips_user)
    else:
        print('Conta Inválida')

    input('Pressione <ENTER> para continuar...')
    clear = 'cls'if os.name == 'nt' else' clear'
    os.system(clear)
