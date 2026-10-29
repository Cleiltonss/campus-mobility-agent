import random
from datetime import date, datetime, time, timedelta

from assistente.contrato import Viagem


MODAIS = {
            0: "ônibus",
            1: "metrô",
            2: "trem",
            3: "transporte de aplicativo",
            4: "carro",
            5: "moto",
            6: "bicicleta",
            7: "a pé",
        }


def periodo_dia(hora_id):
    if 0 <= hora_id and hora_id <= 5:
        return "madrugada"
    elif 6 <= hora_id and hora_id <= 11:
        return "manhã"
    elif 12 <= hora_id and hora_id <= 17:
        return "tarde"
    elif 18 <= hora_id and hora_id <= 23:
        return "noite"
    else:
        raise ValueError(f"Impossível essa hora utilizada: {hora_id}")


def linhas_dim_hora():
    lista = []
    for hora_id in range(24):
        dic = {}
        dic["hora_id"] = hora_id # hora_id: 0 a 24
        dic["periodo_dia"] = periodo_dia(hora_id) # periodo_dia: manhã, tarde, noite, madrugada
        # { hora_id: 0, periodo_dia: madrugada } 

        lista.append(dic)
    
    return lista


def linhas_dim_modal():
    lista = []
    for modal_id in range(len(MODAIS)):
        dic = {}
        dic["modal_id"] = modal_id
        dic["nome_modal"] = MODAIS[modal_id]

        lista.append(dic)

    return lista


# ---------------------------------------------------------------------------
# Daqui para baixo: o resto do gerador (as dimensões que faltavam e o fato).
# Os números são premissas inventadas e declaradas: cada um é uma decisão que
# dá para defender ou trocar. Nenhum é dado oficial.
# ---------------------------------------------------------------------------

NAO_SE_APLICA = -1

ID_DO_MODAL = {nome: modal_id for modal_id, nome in MODAIS.items()}

# nível de serviço do transporte de aplicativo; os outros modais usam o -1
CATEGORIAS = {
    0: "econômico",
    1: "conforto",
    2: "premium",
}

ANO = 2026

# ano letivo: aula de segunda a sexta, dentro de um semestre, fora de feriado
SEMESTRES = [
    (date(2026, 2, 23), date(2026, 7, 3)),
    (date(2026, 8, 3), date(2026, 12, 11)),
]
FERIADOS = {
    date(2026, 1, 1), date(2026, 1, 25), date(2026, 2, 16), date(2026, 2, 17),
    date(2026, 4, 3), date(2026, 4, 21), date(2026, 5, 1), date(2026, 6, 4),
    date(2026, 7, 9), date(2026, 9, 7), date(2026, 10, 12), date(2026, 11, 2),
    date(2026, 11, 15), date(2026, 11, 20), date(2026, 12, 25),
}

# na ordem de date.weekday(): segunda = 0, domingo = 6
NOMES_DIA = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

TURNOS = {
    "Matutino": {"inicio": time(7, 30), "fim": time(12, 10), "peso": 35},
    "Vespertino": {"inicio": time(13, 30), "fim": time(18, 10), "peso": 15},
    "Noturno": {"inicio": time(19, 0), "fim": time(22, 40), "peso": 35},
    "Integral": {"inicio": time(7, 30), "fim": time(17, 30), "peso": 15},
}

# lugares fixos: o campus e as duas estações onde o aluno troca para o ônibus
CAMPUS_ID = 0
ESTACAO_METRO_ID = 1
ESTACAO_TREM_ID = 2
LOCAIS_FIXOS = [
    {"local_id": CAMPUS_ID, "endereco": "Av. da Universidade, 1000", "bairro": "Butantã", "cidade": "São Paulo"},
    {"local_id": ESTACAO_METRO_ID, "endereco": "Estação Butantã (metrô)", "bairro": "Butantã", "cidade": "São Paulo"},
    {"local_id": ESTACAO_TREM_ID, "endereco": "Estação Cidade Universitária (trem)", "bairro": "Butantã", "cidade": "São Paulo"},
]

# (bairro, cidade, km até o campus, trilho que leva até perto do campus, peso)
# peso = quantos alunos moram ali, em proporção. Os dois "Centro" são de
# propósito: GROUP BY bairro sem a cidade junta São Paulo e Osasco.
BAIRROS = [
    ("Butantã", "São Paulo", 1.8, None, 8),
    ("Rio Pequeno", "São Paulo", 4, None, 6),
    ("Jaguaré", "São Paulo", 4, None, 5),
    ("Pinheiros", "São Paulo", 5, "metrô", 7),
    ("Vila Madalena", "São Paulo", 6, "metrô", 5),
    ("Lapa", "São Paulo", 8, None, 5),
    ("Perdizes", "São Paulo", 8, None, 4),
    ("Bela Vista", "São Paulo", 9, "metrô", 5),
    ("Campo Limpo", "São Paulo", 10, None, 5),
    ("Centro", "São Paulo", 11, "metrô", 5),
    ("Vila Mariana", "São Paulo", 11, "metrô", 4),
    ("Santo Amaro", "São Paulo", 12, "trem", 4),
    ("Capão Redondo", "São Paulo", 14, None, 4),
    ("Jabaquara", "São Paulo", 15, "metrô", 3),
    ("Mooca", "São Paulo", 15, "metrô", 3),
    ("Santana", "São Paulo", 16, "metrô", 3),
    ("Tatuapé", "São Paulo", 17, "metrô", 3),
    ("Itaquera", "São Paulo", 27, "metrô", 3),
    ("Centro", "Osasco", 11, "trem", 6),
    ("Presidente Altino", "Osasco", 9, "trem", 4),
    ("Centro", "Taboão da Serra", 10, None, 3),
]

RUAS = [
    "Rua das Acácias", "Rua dos Ipês", "Rua das Palmeiras", "Rua São João",
    "Rua Sete de Setembro", "Rua Santa Rita", "Av. Brasil", "Rua da Paz",
    "Rua do Comércio", "Rua Primavera", "Rua das Hortênsias", "Rua Dom Pedro II",
    "Rua Tiradentes", "Rua Boa Esperança", "Rua XV de Novembro", "Rua dos Jasmins",
    "Rua Santo Antônio", "Rua Rio Branco", "Rua das Orquídeas", "Rua Bela Cintra",
]

# velocidade de porta a porta (km/h) e espera média no ponto (min)
VELOCIDADE = {
    "ônibus": 18, "metrô": 32, "trem": 35, "transporte de aplicativo": 24,
    "carro": 24, "moto": 30, "bicicleta": 14, "a pé": 4.5,
}
ESPERA = {"ônibus": 8, "metrô": 5, "trem": 7, "transporte de aplicativo": 5}

# modais que pegam trânsito: no horário de pico demoram mais
NO_TRANSITO = {"ônibus", "transporte de aplicativo", "carro", "moto"}
HORAS_DE_PICO = {6, 7, 8, 17, 18, 19}
FATOR_PICO = 1.3

# preço por trecho, em reais: tarifa cheia, sem integração nem meia-passagem
TARIFA = {"ônibus": 5.00, "metrô": 5.20, "trem": 5.20}
# carro e moto: só o combustível
CUSTO_POR_KM = {"carro": 0.60, "moto": 0.25}
FATOR_CATEGORIA = {0: 1.0, 1: 1.3, 2: 2.0}

CHANCE_PRESENCA = 0.85            # vai à aula num dia de aula
CHANCE_APLICATIVO_NO_DIA = 0.04   # atrasou ou choveu: naquele dia vai de aplicativo
CHANCE_TROCA_DE_TURNO = 0.04      # muda de turno no 2º semestre (SCD tipo 2)


def data_id(dia):
    return dia.year * 10000 + dia.month * 100 + dia.day


def tem_aula(dia):
    if dia.weekday() >= 5 or dia in FERIADOS:
        return False
    return any(inicio <= dia <= fim for inicio, fim in SEMESTRES)


def linhas_dim_categoria():
    lista = []
    for categoria_id, nome_categoria in CATEGORIAS.items():
        dic = {}
        dic["categoria_id"] = categoria_id
        dic["nome_categoria"] = nome_categoria

        lista.append(dic)

    return lista


def linhas_dim_data():
    lista = []
    dia = date(ANO, 1, 1)
    while dia.year == ANO:
        dic = {}
        dic["data_id"] = data_id(dia)
        dic["nome_dia"] = NOMES_DIA[dia.weekday()]
        dic["dia"] = dia.day
        dic["mes"] = dia.month
        dic["ano"] = dia.year
        dic["tem_aula"] = "Sim" if tem_aula(dia) else "Não"
        dic["ordem_dia"] = (dia.weekday() + 1) % 7 + 1  # domingo = 1, sábado = 7

        lista.append(dic)
        dia += timedelta(days=1)

    return lista


def sortear_periodo(rng, menos=None):
    opcoes = [periodo for periodo in TURNOS if periodo != menos]
    pesos = [TURNOS[periodo]["peso"] for periodo in opcoes]
    return rng.choices(opcoes, weights=pesos)[0]


def novo_trecho(modal, origem_id, destino_id, distancia, categoria_id=NAO_SE_APLICA):
    return {
        "modal": modal,
        "categoria_id": categoria_id,
        "origem_id": origem_id,
        "destino_id": destino_id,
        "distancia": round(distancia, 2),
    }


# os trechos da ida, da casa até o campus; a volta é a mesma rota ao contrário
def sortear_rota(rng, casa_id, distancia, trilho):
    if distancia < 2.5:
        modal = rng.choices(["a pé", "bicicleta"], weights=[75, 25])[0]
        return [novo_trecho(modal, casa_id, CAMPUS_ID, distancia)]

    opcoes = ["público", "transporte de aplicativo", "carro", "moto", "bicicleta"]
    pesos = [62, 10, 15, 5, 8 if distancia <= 8 else 0]
    escolha = rng.choices(opcoes, weights=pesos)[0]

    if escolha == "público":
        if trilho == "metrô" and rng.random() < 0.7:
            return [
                novo_trecho("metrô", casa_id, ESTACAO_METRO_ID, distancia - 2.0),
                novo_trecho("ônibus", ESTACAO_METRO_ID, CAMPUS_ID, 2.0),
            ]
        if trilho == "trem" and rng.random() < 0.7:
            return [
                novo_trecho("trem", casa_id, ESTACAO_TREM_ID, distancia - 1.5),
                novo_trecho("ônibus", ESTACAO_TREM_ID, CAMPUS_ID, 1.5),
            ]
        return [novo_trecho("ônibus", casa_id, CAMPUS_ID, distancia)]

    if escolha == "transporte de aplicativo":
        categoria_id = rng.choices(list(CATEGORIAS), weights=[75, 20, 5])[0]
        return [novo_trecho(escolha, casa_id, CAMPUS_ID, distancia, categoria_id)]

    return [novo_trecho(escolha, casa_id, CAMPUS_ID, distancia)]


def rota_de_volta(rota):
    volta = []
    for trecho in reversed(rota):
        volta.append(novo_trecho(trecho["modal"], trecho["destino_id"], trecho["origem_id"], trecho["distancia"], trecho["categoria_id"]))
    return volta


def sortear_alunos(rng, quantidade):
    locais = [dict(local) for local in LOCAIS_FIXOS]
    local_do_endereco = {(local["endereco"], local["bairro"], local["cidade"]): local["local_id"] for local in locais}
    pesos_bairros = [bairro[4] for bairro in BAIRROS]
    alunos = []
    usuario_id = 0

    for aluno_id in range(1, quantidade + 1):
        bairro, cidade, km, trilho, _ = rng.choices(BAIRROS, weights=pesos_bairros)[0]
        endereco = f"{rng.choice(RUAS)}, {rng.randint(1, 1500)}"

        # mesmo endereço é a mesma linha da dim_local (irmãos, república)
        chave = (endereco, bairro, cidade)
        if chave not in local_do_endereco:
            local_id = len(locais)
            local_do_endereco[chave] = local_id
            locais.append({"local_id": local_id, "endereco": endereco, "bairro": bairro, "cidade": cidade})
        casa_id = local_do_endereco[chave]
        distancia = km * rng.uniform(0.7, 1.3)

        # uma versão por turno: quem troca de turno ganha um usuario_id novo
        periodo = sortear_periodo(rng)
        usuario_id += 1
        versoes = [{"usuario_id": usuario_id, "periodo": periodo, "desde": date(ANO, 1, 1)}]
        if rng.random() < CHANCE_TROCA_DE_TURNO:
            usuario_id += 1
            versoes.append({"usuario_id": usuario_id, "periodo": sortear_periodo(rng, menos=periodo), "desde": SEMESTRES[1][0]})

        alunos.append({
            "aluno_id": aluno_id,
            "casa_id": casa_id,
            "distancia": distancia,
            "rota": sortear_rota(rng, casa_id, distancia, trilho),
            "versoes": versoes,
        })

    return locais, alunos


def linhas_dim_usuario(alunos):
    lista = []
    for aluno in alunos:
        for versao in aluno["versoes"]:
            dic = {}
            dic["usuario_id"] = versao["usuario_id"]
            dic["aluno_id"] = aluno["aluno_id"]
            dic["periodo"] = versao["periodo"]
            dic["atual"] = versao is aluno["versoes"][-1]

            lista.append(dic)

    return lista


def versao_no_dia(aluno, dia):
    vigente = aluno["versoes"][0]
    for versao in aluno["versoes"]:
        if versao["desde"] <= dia:
            vigente = versao
    return vigente


def duracao_trecho(rng, modal, distancia, hora):
    minutos = distancia / VELOCIDADE[modal] * 60 + ESPERA.get(modal, 0)
    if modal in NO_TRANSITO and hora in HORAS_DE_PICO:
        minutos *= FATOR_PICO
    return max(1, round(minutos * rng.uniform(0.85, 1.25)))


def preco_trecho(rng, trecho, duracao, hora):
    modal = trecho["modal"]
    if modal in TARIFA:
        return TARIFA[modal]
    if modal in CUSTO_POR_KM:
        return round(CUSTO_POR_KM[modal] * trecho["distancia"], 2)
    if modal == "transporte de aplicativo":
        preco = (3.00 + 1.50 * trecho["distancia"] + 0.30 * duracao) * FATOR_CATEGORIA[trecho["categoria_id"]]
        if hora in HORAS_DE_PICO:
            preco *= rng.choice([1.0, 1.2, 1.5])  # tarifa dinâmica
        return round(max(preco, 8.00), 2)
    return 0.0  # bicicleta e a pé


def linhas_do_percurso(rng, rota, duracoes, saida, usuario_id):
    for trecho, duracao in zip(rota, duracoes):
        chegada = saida + timedelta(minutes=duracao)
        linha = {
            "modal_id": ID_DO_MODAL[trecho["modal"]],
            "categoria_id": trecho["categoria_id"],
            "origem_id": trecho["origem_id"],
            "destino_id": trecho["destino_id"],
            "hora_saida_id": saida.hour,
            "hora_chegada_id": chegada.hour,
            "data_saida_id": data_id(saida.date()),
            "data_chegada_id": data_id(chegada.date()),
            "usuario_id": usuario_id,
            "duracao": duracao,
            "distancia": trecho["distancia"],
            "preco": preco_trecho(rng, trecho, duracao, saida.hour),
        }
        Viagem(**linha)  # o contrato recusa a viagem impossível antes de ela chegar ao banco
        yield linha
        saida = chegada + timedelta(minutes=rng.randint(2, 8))  # baldeação


# devolve as linhas uma a uma (yield): com 7.000 alunos são milhões de
# linhas, e uma lista com todas elas não cabe folgada na memória
def linhas_fato(rng, alunos, dias_com_aula):
    for aluno in alunos:
        for dia in dias_com_aula:
            if rng.random() > CHANCE_PRESENCA:
                continue
            versao = versao_no_dia(aluno, dia)
            turno = TURNOS[versao["periodo"]]
            rota = aluno["rota"]
            if rng.random() < CHANCE_APLICATIVO_NO_DIA:
                rota = [novo_trecho("transporte de aplicativo", aluno["casa_id"], CAMPUS_ID, aluno["distancia"], 0)]

            # ida: sai de casa a tempo de chegar antes da aula
            inicio_aula = datetime.combine(dia, turno["inicio"])
            duracoes = [duracao_trecho(rng, trecho["modal"], trecho["distancia"], inicio_aula.hour) for trecho in rota]
            folga = rng.randint(5, 20) + 5 * (len(rota) - 1)
            saida = inicio_aula - timedelta(minutes=sum(duracoes) + folga)
            yield from linhas_do_percurso(rng, rota, duracoes, saida, versao["usuario_id"])

            # volta: sai do campus depois da aula
            volta = rota_de_volta(rota)
            saida = datetime.combine(dia, turno["fim"]) + timedelta(minutes=rng.randint(0, 40))
            duracoes = [duracao_trecho(rng, trecho["modal"], trecho["distancia"], saida.hour) for trecho in volta]
            yield from linhas_do_percurso(rng, volta, duracoes, saida, versao["usuario_id"])


# todas as tabelas, na ordem da carga (dimensões antes do fato, por causa das FKs).
# Mesma semente, mesmos dados: o golden set depende disso.
def gerar_dados(quantidade_alunos=7000, semente=42):
    rng = random.Random(semente)
    locais, alunos = sortear_alunos(rng, quantidade_alunos)
    dim_data = linhas_dim_data()
    dias_com_aula = [date(linha["ano"], linha["mes"], linha["dia"]) for linha in dim_data if linha["tem_aula"] == "Sim"]
    return {
        "dim_modal": linhas_dim_modal(),
        "dim_categoria": linhas_dim_categoria(),
        "dim_hora": linhas_dim_hora(),
        "dim_local": locais,
        "dim_data": dim_data,
        "dim_usuario": linhas_dim_usuario(alunos),
        "fato_transportes": linhas_fato(rng, alunos, dias_com_aula),
    }