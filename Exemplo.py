#!/usr/bin/python3

Matriz = {}
while(len(Matriz) < 5):
    conta = ''
    conta = input('Informe o numero da conta: ')
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
    codigo = input('Faca uma escolha entre as seguintes opcoes:\n\
                   1. Efetuar um deposito em uma conta \n\
                   2. Efetuar um saque de uma conta \n\
                   3. Consultar o saldo de uma conta \n\
                   4. Consultar o saldo em geral \n\
                   5. Finalizar o programa\n\
                   Sua Escolha: ')
    if codigo == '1':
        nr_conta = input('Digite o numero da conta: ')
        if nr_conta in Matriz:
            try:
                Matriz[nr_conta] = Matriz[nr_conta] + int(input('Digite a quantidade do depósito: '))
            except ValueError:
                print('Erro conferindo o valor, você digitou numeros?')
            print('O novo saldo da conta é %d'%Matriz[nr_conta])
        else:
            print('Conta inexistente, tente de novo.')
    elif codigo == '2':
        nr_conta = input('Digite o numero da conta: ')
        if nr_conta in Matriz:
            try:
                saque = int(input('Digite a quantidade do saque: '))
                if saque < Matriz[nr_conta]:
                    Matriz[nr_conta] = Matriz[nr_conta] - saque
                else:
                    print('Conta nao tem saldo o suficiente para o saque.')
            except ValueError:
                print('Erro conferindo o valor, você digitou numeros?')
            print('O novo saldo da conta é %d'%Matriz[nr_conta])
        else:
            print('Conta inexistente, tente de novo.')
    elif codigo == '3':
        nr_conta = input('Digite o numero da conta: ')
        if nr_conta in Matriz:
            print('O saldo da conta %s é %d.'%(nr_conta, Matriz[nr_conta]))
        else:
            print('Conta inexistente, tente de novo.')
    elif codigo == '4':
        total = 0
        for conta in Matriz:
            total = total + Matriz[conta]
        print('O saldo geral é %d.'%total)
