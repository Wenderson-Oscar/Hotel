from register import ReserveClient
from model import Model
from datetime import datetime
from model import FileAuthentication, Databases


class Employee:

    def __init__(self, nome: str, cpf: str, telefone: int, email: str, sexo: str, nascimento: str, dados_bancario: str,
        cargo: str, matricula: str, model: Model, nivel_acesso: str = None, senha: str = None) -> str:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.nascimento = nascimento
        self.dados_bancarios = dados_bancario
        self.cargo = cargo
        self.matricula = matricula
        self.nivel_acesso = nivel_acesso
        self.senha = senha
        self.model = model


    def employee_registration(self):
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO funcionario (nome, cpf, telefone, email, sexo, data_nascimento, dados_bancario,
        cargo, matricula, data_adimissao, nivel_acesso, senha_acesso) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (self.nome,
        self.cpf, self.telefone, self.email, self.sexo, self.nascimento, self.dados_bancarios, self.cargo,
        self.matricula, datetime.today(), self.nivel_acesso, self.senha))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


if __name__ == "__main__":
    a = FileAuthentication("authenticade.json")
    c = Databases()
    cliente = Employee('Maria','22332122342','88800210','mariaclara@gmail.com','F','2001-08-23','4','Cozinheira',
    '1', Model(a,c))
    a = cliente.employee_registration()
    print(a)
