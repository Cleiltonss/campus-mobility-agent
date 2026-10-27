import pytest 
from assistente.gerador import periodo_dia, linhas_dim_hora, linhas_dim_modal, MODAIS


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
    

def test_linhas_dim_modal():
    resultado = linhas_dim_modal()
    assert len(resultado) == 8
    assert all (resultado[modal_id]["modal_id"] == modal_id and resultado[modal_id]["nome_modal"] == MODAIS[modal_id] for modal_id in range(8)) 