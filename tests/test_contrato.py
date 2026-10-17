# import pytest
# from pydantic import ValidationError
# from escola.turma import Turma

# def test_turma_lotada_e_recusada():
#     with pytest.raises(ValidationError):
#         Turma(vagas=30, matriculados=31)

import pytest
from pydantic import ValidationError
from assistente.contrato import Viagem

def test_viagem_impossivel():
    with pytest.raises(ValidationError):
        Viagem(
                hora_saida_id=13,
                hora_chegada_id=11, 
                data_saida_id=20270112, 
                data_chegada_id=20270111
                )

def test_viagem_possivel():
    Viagem(
            hora_saida_id=7,
            hora_chegada_id=8, 
            data_saida_id=20261210, 
            data_chegada_id=20261210
            )
    