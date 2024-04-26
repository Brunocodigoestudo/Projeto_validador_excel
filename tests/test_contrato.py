import pytest
from datetime import datetime
from src.contrato import Vendas
from pydantic import ValidationError

# Testes com dados validos


def test_vendas_com_dados_validos():

    # Cria um dicionário de dados validos
    dados_validos = {
        "Email": "comprador@example.com",
        "Data": datetime.now(),
        "Valor": 100.50,
        "Produto": "Produto X",
        "Quantidade": 3,
        "Categoria": "categoria3",
    }

    # A sintaxe **dados_validos é uma forma de desempacotamento de dicionários em Python.
    # O que isso faz é passar os pares chave-valor no dicionário dados_validos como argumentos nomeados para o construtor da classe Vendas.

    Venda = Vendas(**dados_validos)

    assert Venda.Email == dados_validos["Email"]
    assert Venda.Data == dados_validos["Data"]
    assert Venda.Valor == dados_validos["Valor"]
    assert Venda.Produto == dados_validos["Produto"]
    assert Venda.Quantidade == dados_validos["Quantidade"]
    assert Venda.Categoria == dados_validos["Categoria"]

# Testes com dados inválidos


def test_vendas_com_dados_invalidos():
    dados_invalidos = {
        "email": "comprador",
        "data": "não é uma data",
        "valor": 100.50,
        "produto": "Produto Y",
        "quantidade": 1,
        "categoria": 493.50
    }

    with pytest.raises(ValidationError):
        Vendas(**dados_invalidos)

# Teste de validação de categoria


def test_validacao_categoria():
    dados = {
        "Email": "comprador@example.com",
        "Data": datetime.now(),
        "Valor": 100.50,
        "Produto": "Produto Y",
        "Quantidade": 1,
        "Categoria": "categoria inexistente",
    }

    with pytest.raises(ValidationError):
        Vendas(**dados)
