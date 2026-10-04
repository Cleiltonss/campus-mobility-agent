CREATE TABLE dim_modal (
    modal_id INTEGER PRIMARY KEY,
    nome_modal TEXT NOT NULL UNIQUE
);

CREATE TABLE dim_categoria (
    categoria_id INTEGER PRIMARY KEY,
    nome_categoria TEXT NOT NULL UNIQUE
);

CREATE TABLE dim_hora (
    hora_id INTEGER PRIMARY KEY CHECK (hora_id BETWEEN 0 AND 23 OR hora_id = -1),
    periodo_dia TEXT NOT NULL 
);

CREATE TABLE dim_local (
    local_id INTEGER PRIMARY KEY,
    endereco TEXT NOT NULL,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    UNIQUE (endereco, bairro, cidade)
);

CREATE TABLE dim_data (
    data_id INTEGER PRIMARY KEY,
    nome_dia TEXT NOT NULL,
    dia INTEGER NOT NULL,
    mes INTEGER NOT NULL,
    ano INTEGER NOT NULL,
    UNIQUE (dia, mes, ano),
    tem_aula TEXT NOT NULL CHECK (tem_aula IN ('Sim', 'Não') OR tem_aula = 'Não se aplica'),
    ordem_dia INTEGER NOT NULL CHECK (ordem_dia BETWEEN 1 AND 7 OR ordem_dia = -1)
); 

CREATE TABLE dim_usuario (
    usuario_id INTEGER PRIMARY KEY,
    periodo TEXT NOT NULL CHECK (periodo IN ('Matutino', 'Vespertino', 'Noturno', 'Integral') OR periodo = 'Não se aplica')
);


-- membros "Não se aplica": toda dimensão tem chave -1

INSERT INTO dim_modal (modal_id, nome_modal) VALUES (-1, 'Não se aplica');

INSERT INTO dim_categoria (categoria_id, nome_categoria) VALUES (-1, 'Não se aplica');

INSERT INTO dim_hora (hora_id, periodo_dia) VALUES (-1, 'Não se aplica');

INSERT INTO dim_local (local_id, endereco, bairro, cidade) VALUES (-1, 'Não se aplica', 'Não se aplica', 'Não se aplica');

INSERT INTO dim_data (data_id, nome_dia, dia, mes, ano, tem_aula, ordem_dia) VALUES (-1, 'Não se aplica', -1, -1, -1, 'Não se aplica', -1);

INSERT INTO dim_usuario (usuario_id, periodo) VALUES (-1, 'Não se aplica');