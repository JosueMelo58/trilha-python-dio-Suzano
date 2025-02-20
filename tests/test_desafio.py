import pytest
from desafio_banco import sacar

def test_sacar_valor_valido():
    saldo = 1000
    valor = 500
    extrato = ""
    limite = 1000
    numero_saques = 0
    limite_saques = 3

    saldo_final, extrato_final = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=limite_saques
    )

    assert saldo_final == 500
    assert "Saque:\t\tR$ 500.00\n" in extrato_final

def test_sacar_saldo_insuficiente():
    saldo = 100
    valor = 500
    extrato = ""
    limite = 1000
    numero_saques = 0
    limite_saques = 3

    saldo_final, extrato_final = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=limite_saques
    )

    assert saldo_final == 100
    assert extrato_final == ""

def test_sacar_excede_limite():
    saldo = 2000
    valor = 1500
    extrato = ""
    limite = 1000
    numero_saques = 0
    limite_saques = 3

    saldo_final, extrato_final = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=limite_saques
    )

    assert saldo_final == 2000
    assert extrato_final == ""

def test_sacar_excede_numero_saques():
    saldo = 1000
    valor = 100
    extrato = ""
    limite = 1000
    numero_saques = 3
    limite_saques = 3

    saldo_final, extrato_final = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=limite_saques
    )

    assert saldo_final == 1000
    assert extrato_final == ""

def test_sacar_valor_negativo():
    saldo = 1000
    valor = -100
    extrato = ""
    limite = 1000
    numero_saques = 0
    limite_saques = 3

    saldo_final, extrato_final = sacar(
        saldo=saldo,
        valor=valor,
        extrato=extrato,
        limite=limite,
        numero_saques=numero_saques,
        limite_saques=limite_saques
    )

    assert saldo_final == 1000
    assert extrato_final == ""
