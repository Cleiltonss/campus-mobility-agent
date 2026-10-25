import pytest 
from assistente.gerador import periodo_dia, linhas_dim_hora


def test_periodo_dia():
    resultado = periodo_dia(
                            hora_id=6
    )
    assert resultado == "manhã"

def test_periodo_dia_impossivel():
    with pytest.raises(ValueError):
        periodo_dia(
                    hora_id=99
        )


def test_linhas_dim_hora():
    resultado = linhas_dim_hora()
    assert len(resultado) == 24
    assert all(resultado[i]["hora_id"] == i and resultado[i]["periodo_dia"] == periodo_dia(i) for i in range (24))
    
