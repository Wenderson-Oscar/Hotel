from model import Model, FileAuthentication, Databases

class Service:

    def __init__(self, descricao: str, preco: float, status: str, pk_funcionario: int ,model: Model):
        self.descricao = descricao
        self.preco = preco
        self.status = status
        self.pk_funcionario = pk_funcionario
        self.model = model


    def register_service(self):
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO servico (descricao, preco, status, pk_funcionario) VALUES (?,?,?,?)""", 
        (self.descricao, self.preco, self.status, self.pk_funcionario))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    obj = Service('Cafe da manhã', 10, 'Ativo', 1, Model(file, db))
    a = obj.register_service()
    print(a)