import pytest 
from assistente.gerador import periodo_dia


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
