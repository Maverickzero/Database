#!/usr/bin/python3

Matriz = {}
while(len(Matriz) < 5):
    conta = ''
    conta = input('Informe o numero da conta: ')
    try:
        int(conta)
    except ValueError:
        print('Erro criando conta, você digitou numeros?')
        continue
    if conta in Matriz:
        print('Conta já existe, tente de novo. ')
        continue
    try:
        Matriz[conta] = int(input('Informe o saldo da conta: '))
    except ValueError:
        print('Erro conferindo o valor, você digitou numeros?')
del conta

codigo = None
while(codigo != '5'):
    print('Faca uma escolha entre as seguintes opcoes:',
          '1. Efetuar um deposito em uma conta',
          '2. Efetuar um saque de uma conta',
          '3. Consultar o saldo de uma conta',
          '4. Consultar o saldo em geral',
          '5. Finalizar o programa',
          sep='\n')
    codigo = input('Sua Escolha: ')
    if codigo == '1':
        nr_conta = input('Digite o numero da conta: ')
        if nr_conta in Matriz:
            try:
                deposito = int(input('Digite a quantidade do depósito: '))
            except ValueError:
                print('Erro conferindo o valor, você digitou numeros?')
            Matriz[nr_conta] = Matriz[nr_conta] + deposito
            print('O novo saldo da conta é %d' % Matriz[nr_conta])
        else:
            print('Conta inexistente, tente de novo.')
    elif codigo == '2':
        nr_conta = input('Digite o numero da conta: ')
        if nr_conta in Matriz:
            try:
                saque = int(input('Digite a quantidade do saque: '))
            except ValueError:
                print('Erro conferindo o valor, você digitou numeros?')
            if saque < Matriz[nr_conta]:
                Matriz[nr_conta] = Matriz[nr_conta] - saque
                print('O novo saldo da conta é %d' % Matriz[nr_conta])
            else:
                print('Conta nao tem saldo o suficiente para o saque.')
        else:
            print('Conta inexistente, tente de novo.')
    elif codigo == '3':
        nr_conta = input('Digite o numero da conta: ')
        if nr_conta in Matriz:
            print('O saldo da conta %s é %d.' % (nr_conta, Matriz[nr_conta]))
        else:
            print('Conta inexistente, tente de novo.')
    elif codigo == '4':
        total = 0
        for conta in Matriz:
            total = total + Matriz[conta]
        print('O saldo geral é %d.' % total)
    elif codigo == '5':
        continue
    else:
        print('Codigo inexistente, tente de novo.')

