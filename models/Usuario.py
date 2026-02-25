class Usuario:
    def __init__(self, id, nome, cpf, data_nascimento):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
            "data_nascimento": self.data_nascimento
        }


print(__name__)
if __name__ == "__main__":
    usuario = Usuario(1, "Maria", "1215888888", "2026-04-09")
    print(usuario)
