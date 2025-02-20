import os
import time
import textwrap
from datetime import datetime


def menu():
    menu = """\n
    ================ MENU BANCÁRIO ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(textwrap.dedent(menu)).lower()

def data_registro():
    data_registro = datetime.now()
    data_formatada = data_registro.strftime("%d/%m/%Y %H:%M")   
    return data_formatada

def depositar(saldo, valor, extrato):
    retorno_depositar = ""
    if valor > 0:
        saldo += valor
        extrato = extrato + f"Depósito:\tR$ {valor:.2f} - {data_registro()}\n"
        retorno_depositar = "\nDepósito realizado com sucesso!" 
        print(retorno_depositar.center(5, "="))
    else:
        retorno_depositar = "\nOperação não realizada! Valor informado é inválido."
        print(retorno_depositar.center(5, "@"))

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f} - {data_registro()}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
       

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    mensagem_inicial = """
    \n ===== Seja bem-vindo(a) ao Banco Python! =====
    \n Limite: {}
    \n Saldo: {}
    """.format(limite, saldo)

    print(mensagem_inicial)
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato) 
            time.sleep(1.5)  
            os.system("cls")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            time.sleep(1.5)
            os.system("cls")

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
            input("Pressione Enter para retornar ao Menu")
            os.system("cls")
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            time.sleep(1.5)
            os.system("cls")

main()
