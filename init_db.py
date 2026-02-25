import sqlite3

def init():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            data_nascimento TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS instituicoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            co_municipio TEXT,
            qt_mat_bas INTEGER,
            qt_mat_prof INTEGER,
            qt_mat_eja INTEGER,
            qt_mat_esp INTEGER
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Banco de dados criado com os campos específicos de Usuário e Instituição!")

if __name__ == '__main__':
    init()