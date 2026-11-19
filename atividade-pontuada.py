import os
import sys
os.system('cls')

saldo = 500
extrato = []

# CRIANDO SENHA DE ACESSO.
def senha_menu():
    while True:
        print('''
==============================
    LOGIN - CONTA BANCARIA
==============================
    ''')
        nome = 'ROBSON'
        numero_conta = 2026
        senha = 00
        nome_usuario = input('Digite o nome de usuario: ').upper()
        login_conta = int(input('Digite o número da conta: '))
        senha_conta = int(input('Digite a senha da conta: '))
        if login_conta == numero_conta and senha_conta == senha and nome_usuario == nome:
            print(f'Bem vindo a sua conta bancaria Robson!')
            input('Toque "enter" para continuar...')
            os.system('cls')
            break
        else:
            print('Alguma das informações está errada.')
            print('Tente novamente.')
            input('Toque "enter" para continuar...')
            os.system('cls')


# MOSTRANDO MENU.
def mostra_menu():
    os.system('cls')
    print("""
\n= BANCO COFRINHO =
1 - Ver Saldo
2 - Depositar
3 - Sacar
4 - Ver Extrato
0 - Sair """)

# MOSTRANDO SALDO.
def mostrar_saldo():
    print(f"\n= EXBINDO SALDO =")
    print(f"Saldo disponivel: {saldo:.2f}")

# DEPOSITANDO SALDO.
def depositando_saldo(saldo):
    while True:
        deposito = float(input('Digite o valor que deseja depositar: '))
        if deposito <= 0:
            print('O valor de deposito não pode ser zero nem negativo.')
            print('Insira um valor valido.')
            input('Toque "enter" para continuar...')
            os.system('cls')
        else:
            saldo += deposito
            print(f'Deposito de R${deposito} adicionado com sucesso!')
            extrato.append(f'Depósito: R${deposito:.2f}')
            input('Toque "enter" para continuar...')
            os.system('cls')
            break
    return saldo

# SACANDO SALDO.
def sacando_saldo(saldo):
    while True:
        retirar = float(input('Digite a quantidade que deseja sacar: '))
        if retirar <= 0:
            print('O valor de saque não pode ser 0 e nem valor negativo.')
            input('Toque "enter" para continuar...')
            os.system('cls')
        elif retirar > saldo:
            print('O valor de saque não pode ser maior que o saldo disponivel.')
            print(f'Seu saldo atual é de R${saldo}.')
            input('Toque "enter" para continuar...')
        elif retirar > 1000:
            print('O limite de saque é de R$1000 reais')
            input('Toque "enter" para continuar...')
        else:
            saldo = saldo - retirar
            print(f'Saque de R${retirar} realizado com sucesso!')
            extrato.append(f'Saque: R${retirar:.2f}')
            input('Toque "enter" para continuar...')
            os.system('cls')
            break
    return saldo

# EXIBINDO EXTRATO.
def exibindo_extrato():
    print('\n= EXIBINDO EXTRATO =')
    if len(f'{extrato}') == 0:
        print('Não foram realizadas movimentações.')
    else:
        for movimentacao in extrato:
            print(f'{movimentacao}')
    print('-----------------------------')
    print(f'Saldo atual: R${saldo:.2f}')
    print('=============================')
    input('Toque "enter" para continuar...')

# SAINDO DO PROGRAMA.
def saindo_programa():
    print('\nSaindo do programa...')
    sys.exit()

while True:
    senha_menu()
    mostra_menu()
    opcao = int(input("\nEscolha uma opcão: "))
    if opcao >= 5:
        print('Opção inválida')
        input('Toque "enter" para continuar...')
        continue
    match opcao:
        case 1:
            mostrar_saldo()
            input('Toque "enter" para continuar...')
        case 2:
            saldo = depositando_saldo(saldo)
        case 3:
            saldo = sacando_saldo(saldo)
        case 4:
            exibindo_extrato()
        case 0:
            saindo_programa()