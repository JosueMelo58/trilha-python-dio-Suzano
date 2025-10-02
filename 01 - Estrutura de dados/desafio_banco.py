import os
import time
import textwrap
from datetime import datetime

# Criando Menu

def menu():
    menu = """\n
    ================ MENU BANCÁRIO ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tListar usuários
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

#Novas funcionalidades---


def filtro_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("/n ========== Nova conta criada com sucesso! ==========")
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    
    else:
        print("\n ******** Para criar nova conta é necessário que o CPF seja de um usuário! Gentileza conferir. Processo encerrado! ********")
        return None

def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agência:/t{conta["agencia"]}
        C/C:/t{conta["numero_conta"]}    
        Titular:/t{conta["usuario"]["nome"]}
        CPF:/t{conta["usuario"]["CPF"]}
'''
        print("-"*50)
        print(textwrap.dedent(linha))

def novo_usuario(usuarios):
    cpf = input("Digite o CPF do novo usuário (somente números):").strip()
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("/n +++++ CPF já cadastrado como usuário no sistema! +++++")

    else:

        nome = input("Digite o nome completo do usuário:")
        data_nascimento = input("Digite a data de nascimento do usuário (formato dd-mm-aaaa):")  
        endereco = input("Digite o endereço do usuário (complemento com número, bairro, cidade/sigla estado)")  

        usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco})
        print("\n ------- Usuário cadastrado com sucesso! -------")

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f'''
        Nome:/t{usuario["nome"]}
        Data de Nascimento:/t{usuario["data_nascimento"]}
        CPF:/t{usuario["cpf"]}  
        Endereço:/t{usuario["endereco"]}
'''
        print("-"*50)
        print(textwrap.dedent(linha))


#----
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

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato) 
            time.sleep(1.5)  
            os.system("cls")

        elif opcao == "2":
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

        elif opcao == "3":
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
