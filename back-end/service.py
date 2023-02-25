from model import Model, FileAuthentication, Databases
from automate_insertion_pk import AutoIncrementPk
from datetime import date

class Service:

    def __init__(self, descricao: str, preco: float, status: str, model: Model):
        self.descricao = descricao
        self.preco = preco
        self.status = status
        self.model = model


    def register_service(self, automate_pk: AutoIncrementPk):
        """inserir serviço no banco"""
        count_pk = automate_pk.count_employee()
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO servico (descricao, preco, status, pk_funcionario) VALUES (?,?,?,?)""", 
        (self.descricao, self.preco, self.status, count_pk))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'
    
    def enter_relationship_data(self, automate_pk: AutoIncrementPk):
        """inserir relacionamento de serviço no banco"""
        count_service_pk = automate_pk.count_service()
        count_category_pk = automate_pk.count_category()
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO reservar_servico (data_criacao, pk_servico, pk_categoria) VALUES 
        (?,?,?)""", (date.today(), count_service_pk, count_category_pk))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    model = Model(file, db)
    automate_pk = AutoIncrementPk(model)
    obj = Service('Cafe da manhã', 10, 'Ativo', model)
    a = obj.register_service(automate_pk)
    b = obj.enter_relationship_data(automate_pk)
    print(a)
    print()
    print(b)