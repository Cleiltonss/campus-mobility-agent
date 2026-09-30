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


-- membros "Não se aplica": toda dimensão tem chave -1

INSERT INTO dim_modal (modal_id, nome_modal) VALUES (-1, 'Não se aplica');

INSERT INTO dim_categoria (categoria_id, nome_categoria) VALUES (-1, 'Não se aplica');

INSERT INTO dim_hora (hora_id, periodo_dia) VALUES (-1, 'Não se aplica');

