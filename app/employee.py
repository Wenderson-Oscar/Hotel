from register import ReserveClient

class Employee(ReserveClient):

    def __init__(self, nome: str, cpf: str, telefone: int, email: str, sexo: str, nascimento: str, dados_bancario: str,
        cargo: str, matricula: str, data_admissao: str, nivel_acesso: None, senha: None) -> str:
        ReserveClient().__init__(nome, cpf, telefone, email, sexo, nascimento, dados_bancario, senha)
        self.cargo = cargo
        self.matricula = matricula
        self.data_admissao = data_admissao
        self.nivel_acesso = nivel_acesso


    def employee_registration(self):
        pass
