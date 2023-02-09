class ReserveClient:

    def __init__(self, nome: str, cpf: str, telefone: int, email: str,
        sexo: str, nascimento: str, dados_bancario: str, senha: str) -> str:
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.nascimento = nascimento
        self.dados_bancarios = dados_bancario
        self.senha = senha

    def guest_registration(self, nome: str, cpf: str, telefone: int, email: str,
        sexo: str, nascimento: str, dados_bancario: str, senha: str):
        pass