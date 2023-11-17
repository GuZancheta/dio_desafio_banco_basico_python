menu = '''
Escolha a operação:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

:
'''

saldo = 0.00
limite = 500
extrato = ""
qtd_saques = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == '1':
        deposito = int(input('Digite o valor que deseja depositar: '))
        if deposito > 0:
            saldo += deposito
            extrato += f'Depósito: R${deposito:.2f}\n'
            print('Depósito realizado com sucesso.')
        else:
            print('Valor inválido para depósito')
    
    elif opcao == '2':
        if qtd_saques < LIMITE_SAQUE:
            valor_saque = int(input('Digite o valor que deseja sacar: '))
            if valor_saque <= 0:
                print('Valor de saque inválido.')
            elif valor_saque > limite:
                print('Valor solicitado maior que o limite por saque.')
            elif valor_saque > saldo:
                print('Saldo insuficiente.')
            else:
                qtd_saques += 1
                saldo -= valor_saque
                extrato += f'Saque: R${valor_saque:.2f}\n'
                print('Saque realizado com sucesso.')

        else:
            print('Limite de Saques excedido.')

    elif opcao == '3':
        print('\n\nExtrato: \n')
        print(extrato)
        print(f'Saldo atual: R${saldo:.2f}\n')


    elif opcao == '0':
        break

    else:
        print('Opção inválida!')