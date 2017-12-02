#!/usr/bin/env python3
Matriz = []
for i in range(1,6):
    conta = []
    conta.append(int(input('Informe o numero da conta %d: '%i)))
    conta.append(int(input('Informe o saldo da conta %d: '%i)))
    Matriz.append(conta)

codigo = None

while(codigo != '5'):
    codigo = input('\tFaca uma escolha entre as seguintes opcoes:\n\
                   1. Efetuar um deposito em uma conta \n\
                   2. Efetuar um saque de uma conta \n\
                   3. Consultar o saldo de uma conta \n\
                   4. Consultar o saldo em geral \n\
                   5. Finalizar o programa\n')
    if codigo == '1':
        nr_conta = input('Digite o numero da conta: ')
        for i in range(1, len(Matriz)+1):
            conta = Matriz.pop()
            if nr_conta == conta[0]:
                deposito = int(input('Digite o valor do deposito: '))
                conta[1] = conta[1] + deposito
                Matriz.append(conta)
        # do something
#    elif codigo == '2':
#        # do something
#    elif codigo == '3':
#        # do something
#    elif codigo == '4':
#        # do something
#    elif codigo == '5':
#        # do something

for conta in Matriz:
    print('A conta %d tem saldo %d'%(conta[0],conta[1]))
