from model import Model
from datetime import datetime
from model import FileAuthentication, Databases

class ReserveClient:

    def __init__(self, nome: str, cpf: str, telefone: int, email: str,
        sexo: str, nascimento: str, dados_bancario: str, senha: str, model: Model) -> str:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.nascimento = nascimento
        self.dados_bancarios = dados_bancario
        self.senha = senha
        self.model = model


    def guest_registration(self):
        self.database.connect.execute("""INSERT INTO hospede (nome, cpf, telefone, email, sexo, data_nascimento, 
        dados_bancarios, senha_bancaria, data_criacao) VALUES (?,?,?,?,?,?,?,?,?)""", (self.nome, self.cpf, self.telefone, self.email,
        self.sexo, self.nascimento, self.dados_bancarios, self.senha, datetime.today()))
        self.database.connect.commit()
        self.database.connect.close()
        return 'reservado com sucesso'

if __name__ == "__main__":
    a = FileAuthentication("authenticade.json")
    c = Databases()
    cliente = ReserveClient('Maria','22332122322','88100200','maria@gmail.com','F','2003-06-27','3','222',Model(a,c))
    a = cliente.guest_registration()
