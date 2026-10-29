import pytest
from assistente.gerador import periodo_dia, linhas_dim_hora, linhas_dim_modal, MODAIS

from collections import Counter
from assistente.contrato import Viagem
from assistente.gerador import ID_DO_MODAL, SEMESTRES, data_id, gerar_dados, linhas_dim_categoria, linhas_dim_data


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


def test_linhas_dim_categoria():
    assert linhas_dim_categoria() == [
        {"categoria_id": 0, "nome_categoria": "econômico"},
        {"categoria_id": 1, "nome_categoria": "conforto"},
        {"categoria_id": 2, "nome_categoria": "premium"},
    ]


def test_linhas_dim_data_cobre_o_ano():
    resultado = linhas_dim_data()
    assert len(resultado) == 365
    assert resultado[0]["data_id"] == 20260101
    assert resultado[-1]["data_id"] == 20261231


def test_linhas_dim_data_calendario():
    dia = {linha["data_id"]: linha for linha in linhas_dim_data()}
    assert (dia[20260315]["nome_dia"], dia[20260315]["ordem_dia"]) == ("domingo", 1)
    assert (dia[20260316]["nome_dia"], dia[20260316]["ordem_dia"]) == ("segunda", 2)
    assert (dia[20260321]["nome_dia"], dia[20260321]["ordem_dia"]) == ("sábado", 7)
    assert dia[20260316]["tem_aula"] == "Sim"  # segunda, no semestre
    assert dia[20260321]["tem_aula"] == "Não"  # sábado
    assert dia[20260421]["tem_aula"] == "Não"  # Tiradentes, uma terça
    assert dia[20260715]["tem_aula"] == "Não"  # quarta de férias


# população pequena e semente fixa: roda rápido e dá sempre os mesmos dados
@pytest.fixture(scope="module")
def dados():
    dados = gerar_dados(quantidade_alunos=150, semente=7)
    dados["fato_transportes"] = list(dados["fato_transportes"])
    return dados


CHAVE = {
    "dim_modal": "modal_id", "dim_categoria": "categoria_id", "dim_hora": "hora_id",
    "dim_local": "local_id", "dim_data": "data_id", "dim_usuario": "usuario_id",
}

FK = {
    "modal_id": "dim_modal", "categoria_id": "dim_categoria",
    "origem_id": "dim_local", "destino_id": "dim_local",
    "hora_saida_id": "dim_hora", "hora_chegada_id": "dim_hora",
    "data_saida_id": "dim_data", "data_chegada_id": "dim_data",
    "usuario_id": "dim_usuario",
}


def chaves(dados, tabela):
    return [linha[CHAVE[tabela]] for linha in dados[tabela]]


def test_chaves_das_dimensoes_sao_unicas(dados):
    for tabela in CHAVE:
        assert len(chaves(dados, tabela)) == len(set(chaves(dados, tabela))), tabela


def test_dim_local_sem_endereco_repetido(dados):
    enderecos = [(linha["endereco"], linha["bairro"], linha["cidade"]) for linha in dados["dim_local"]]
    assert len(enderecos) == len(set(enderecos))


def test_cada_aluno_tem_uma_versao_atual(dados):
    atuais = Counter(linha["aluno_id"] for linha in dados["dim_usuario"] if linha["atual"])
    assert len(atuais) == 150
    assert set(atuais.values()) == {1}


def test_fato_so_aponta_para_linhas_que_existem(dados):
    for coluna, tabela in FK.items():
        existentes = set(chaves(dados, tabela)) | {-1}  # o -1 já está no banco (schema.sql)
        usadas = {linha[coluna] for linha in dados["fato_transportes"]}
        assert usadas <= existentes, coluna


def test_toda_linha_do_fato_passa_no_contrato(dados):
    for linha in dados["fato_transportes"]:
        Viagem(**linha)


def test_categoria_so_no_aplicativo(dados):
    aplicativo = ID_DO_MODAL["transporte de aplicativo"]
    for linha in dados["fato_transportes"]:
        assert (linha["categoria_id"] != -1) == (linha["modal_id"] == aplicativo)


def test_metricas_positivas(dados):
    for linha in dados["fato_transportes"]:
        assert linha["duracao"] > 0 and linha["distancia"] > 0 and linha["preco"] >= 0


def test_volta_da_noite_pode_virar_o_dia(dados):
    assert any(linha["data_chegada_id"] > linha["data_saida_id"] for linha in dados["fato_transportes"])


# SCD tipo 2: quem trocou de turno no 2º semestre tem duas linhas na dim_usuario,
# e cada viagem aponta para a versão que valia no dia dela
def test_viagem_aponta_para_a_versao_do_aluno_naquela_data(dados):
    versoes = {}
    for linha in dados["dim_usuario"]:
        versoes.setdefault(linha["aluno_id"], []).append(linha)
    trocaram = [v for v in versoes.values() if len(v) == 2]
    assert trocaram, "a semente do teste precisa ter alguém que troca de turno"

    inicio_2_semestre = data_id(SEMESTRES[1][0])
    for antiga, nova in trocaram:
        assert not antiga["atual"] and nova["atual"]
        for linha in dados["fato_transportes"]:
            if linha["usuario_id"] == antiga["usuario_id"]:
                assert linha["data_saida_id"] < inicio_2_semestre
            if linha["usuario_id"] == nova["usuario_id"]:
                assert linha["data_saida_id"] >= inicio_2_semestre


def test_mesma_semente_mesmos_dados():
    primeira = gerar_dados(quantidade_alunos=20, semente=3)
    segunda = gerar_dados(quantidade_alunos=20, semente=3)
    for tabela in primeira:
        assert list(primeira[tabela]) == list(segunda[tabela]), tabela