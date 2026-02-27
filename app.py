from flask import Flask, request, jsonify

from models.Usuario import Usuario
from models.InstituicaoEnsino import InstituicaoEnsino
from helpers.data import getInstituicoesEnsino

app = Flask(__name__)

usuarios = []
instituicoesEnsino = getInstituicoesEnsino()

@app.get("/")
def index():
    return '{"versao":"2.0.0"}', 200


@app.get("/usuarios")
def getUsuarios():
    return jsonify([u.to_json() for u in usuarios]), 200

@app.get("/usuarios/<int:id>")
def getUsuariosById(id: int):
    return jsonify(usuarios[id].to_json()), 200

@app.post("/usuarios")
def setUsuarios():
    data = request.get_json()
    
    novo = Usuario(
        id=len(usuarios),
        nome=data['nome'],
        cpf=data.get('cpf', ''),
        data_nascimento=data.get('data_nascimento', '')
    )
    usuarios.append(novo)
    return jsonify(novo.to_json()), 201

@app.put("/usuarios/<int:id>")
def updateUsuario(id: int):
    data = request.get_json()
    
    usuarios[id] = Usuario(
        id=id,
        nome=data['nome'],
        cpf=data.get('cpf', usuarios[id].cpf),
        data_nascimento=data.get('data_nascimento', usuarios[id].data_nascimento)
    )
    return jsonify(usuarios[id].to_json()), 200

@app.patch("/usuarios/<int:id>")
def patchUsuario(id: int):
    data = request.get_json()
    u = usuarios[id]
    u.nome = data.get('nome', u.nome)
    u.cpf = data.get('cpf', u.cpf)
    u.data_nascimento = data.get('data_nascimento', u.data_nascimento)
    
    return jsonify(u.to_json()), 200

@app.delete("/usuarios/<int:id>")
def deleteUsuario(id: int):
    removido = usuarios.pop(id)
    return jsonify(removido.to_json()), 200



@app.get("/instituicoesensino")
def getInstituicoes():
    return jsonify([i.to_json() for i in instituicoesEnsino]), 200

@app.get("/instituicoesensino/<int:id>")
def getInstituicoesById(id: int):
    return jsonify(instituicoesEnsino[id].to_json()), 200

@app.post("/instituicoesensino")
def createInstituicao():
    data = request.get_json()
    
    nova = InstituicaoEnsino(
        codigo=len(instituicoesEnsino),
        nome=data['nome'],
        co_uf=data.get('co_uf', ''),
        co_municipio=data.get('co_municipio', ''),
        qt_mat_bas=data.get('qt_mat_bas', 0),
        qt_mat_prof=data.get('qt_mat_prof', 0),
        qt_mat_eja=data.get('qt_mat_eja', 0),
        qt_mat_esp=data.get('qt_mat_esp', 0)
    )
    instituicoesEnsino.append(nova)
    return jsonify(nova.to_json()), 201

@app.put("/instituicoesensino/<int:id>")
def updateInstituicao(id: int):
    data = request.get_json()
    ie = instituicoesEnsino[id]
    
    ie.nome = data.get('nome', ie.nome)
    ie.co_uf = data.get('co_uf', ie.co_uf)
    ie.co_municipio = data.get('co_municipio', ie.co_municipio)
    
    return jsonify(ie.to_json()), 200

@app.delete("/instituicoesensino/<int:id>")
def deleteInstituicao(id: int):
    removida = instituicoesEnsino.pop(id)
    return jsonify(removida.to_json()), 200

if __name__ == '__main__':
    app.run(debug=True)