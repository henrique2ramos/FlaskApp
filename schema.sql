-- schema.sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    data_nascimento TEXT
);

CREATE TABLE IF NOT EXISTS instituicoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    co_municipio TEXT,
    qt_mat_bas INTEGER,
    qt_mat_prof INTEGER,
    qt_mat_eja INTEGER,
    qt_mat_esp INTEGER
);
