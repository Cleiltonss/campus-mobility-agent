from assistente.ingestao import cortar_documento
import pytest


TEXTO = """# Regulamento de teste

Vigente a partir de 2027.

## 1. Primeira seção

Texto da primeira seção.

## 2. Segunda seção

Texto da segunda seção.
"""

TEXTO_5_SECOES = """# Guia de teste

Atualizado em 2026.

## A. Seção um

Texto um.

## B. Seção dois

Texto dois.

## C. Seção três

Texto três.

## D. Seção quatro

Texto quatro.

## E. Seção cinco

Texto cinco.
"""


def test_cortar_documento():
    resultado = cortar_documento("regras_teste", TEXTO)

    assert len(resultado) == 3
    assert "# Regulamento de teste" in resultado[0]["texto"]
    assert "## 1. Primeira seção" in resultado[1]["texto"]
    assert "## 2. Segunda seção" in resultado[2]["texto"]


@pytest.mark.parametrize("palavra, esperado", [
    (TEXTO, 3),
    (TEXTO_5_SECOES, 6)
])
def test_tamanho(palavra, esperado):
    resultado = cortar_documento("regras_teste", palavra)
    assert len(resultado) == esperado

