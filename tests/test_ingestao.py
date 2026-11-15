from assistente.ingestao import cortar_documento

TEXTO = """# Regulamento de teste

Vigente a partir de 2027.

## 1. Primeira seção

Texto da primeira seção.

## 2. Segunda seção

Texto da segunda seção.
"""


def test_cortar_documento():
    resultado = cortar_documento("regras_teste", TEXTO)

    assert len(resultado) == 3
    assert "# Regulamento de teste" in resultado[0]["texto"]
    assert "## 1. Primeira seção" in resultado[1]["texto"]
    assert "## 2. Segunda seção" in resultado[2]["texto"]