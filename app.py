from flask import Flask, request, jsonify
import sqlite3
import pandas as pd
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')

def executar_query(sql, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        if sql.strip().upper().startswith("SELECT"):
            return pd.read_sql_query(sql, conn, params=params)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        return None

@app.route('/')
def home():
    return jsonify({"status": "API Online", "rotas": ["/usuarios", "/instituicoes"]})


@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    df = executar_query("SELECT * FROM usuarios")
    return df.to_json(orient='records'), 200

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    d = request.json
    sql = "INSERT INTO usuarios (nome, cpf, data_nascimento) VALUES (?, ?, ?)"
    executar_query(sql, (d['nome'], d['cpf'], d.get('data_nascimento')))
    return jsonify({"mensagem": "Usuário inserido com sucesso"}), 201


@app.route('/instituicoes', methods=['GET'])
def listar_instituicoes():
    df = executar_query("SELECT * FROM instituicoes")
    return df.to_json(orient='records'), 200

@app.route('/instituicoes', methods=['POST'])
def criar_instituicao():
    d = request.json
    sql = """INSERT INTO instituicoes 
             (nome, co_municipio, qt_mat_bas, qt_mat_prof, qt_mat_eja, qt_mat_esp) 
             VALUES (?, ?, ?, ?, ?, ?)"""
    params = (
        d['nome'], 
        d.get('co_municipio'), 
        d.get('qt_mat_bas', 0), 
        d.get('qt_mat_prof', 0), 
        d.get('qt_mat_eja', 0), 
        d.get('qt_mat_esp', 0)
    )
    executar_query(sql, params)
    return jsonify({"mensagem": "Instituição inserida com sucesso"}), 201

if __name__ == '__main__':
    app.run(debug=True)