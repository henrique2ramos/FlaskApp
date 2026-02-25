from flask import Flask, request, jsonify
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

def executar_query(sql, params=()):
    with sqlite3.connect(DB_PATH) as conn:
        if sql.strip().upper().startswith("SELECT"):
            return pd.read_sql_query(sql, conn, params=params)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        return None

@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    df = executar_query("SELECT * FROM usuarios")
    return df.to_json(orient='records'), 200

@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.json
    colunas = ', '.join(dados.keys())
    placeholders = ', '.join(['?'] * len(dados))
    sql = f"INSERT INTO usuarios ({colunas}) VALUES ({placeholders})"
    executar_query(sql, list(dados.values()))
    return jsonify({"status": "sucesso", "mensagem": "Usuario inserido"}), 201

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    executar_query("DELETE FROM usuarios WHERE id = ?", (id,))
    return jsonify({"status": "sucesso"}), 200

@app.route('/instituicoes', methods=['GET'])
def listar_instituicoes():
    df = executar_query("SELECT * FROM instituicoes")
    return df.to_json(orient='records'), 200

@app.route('/instituicoes', methods=['POST'])
def criar_instituicao():
    dados = request.json
    colunas = ', '.join(dados.keys())
    placeholders = ', '.join(['?'] * len(dados))
    sql = f"INSERT INTO instituicoes ({colunas}) VALUES ({placeholders})"
    executar_query(sql, list(dados.values()))
    return jsonify({"status": "sucesso"}), 201

@app.route('/instituicoes/<int:id>', methods=['DELETE'])
def deletar_instituicao(id):
    executar_query("DELETE FROM instituicoes WHERE id = ?", (id,))
    return jsonify({"status": "sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)