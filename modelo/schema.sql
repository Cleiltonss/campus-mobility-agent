CREATE TABLE dim_modal (
    modal_id INTEGER PRIMARY KEY,
    nome_modal TEXT NOT NULL UNIQUE
);


CREATE TABLE dim_categoria (
    categoria_id INTEGER PRIMARY KEY,
    nome_categoria TEXT NOT NULL UNIQUE
);

CREATE TABLE dim_hora (
    hora_id INTEGER PRIMARY KEY,
    periodo_dia TEXT NOT NULL
);