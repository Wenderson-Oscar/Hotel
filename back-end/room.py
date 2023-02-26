from model import Model, FileAuthentication, Databases
from automate_insertion_pk import AutoIncrementPk

class Room:

    def __init__(self, descricao: str, numero_quarto: int, capacidade: int,
    observacao: str, status: str, model: Model):
        self.descricao = descricao
        self.numero_quarto = numero_quarto
        self.capacidade = capacidade
        self.obervacao = observacao
        self.status =  status
        self.model = model

    
    def register_room(self, automate_pk: AutoIncrementPk):
        """inserir quarto no banco"""
        count_category_pk = automate_pk.count_category()
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO quarto (descricao, numero_quarto, capacidade, observacao, status, 
        pk_categoria) VALUES (?,?,?,?,?,?)""", (self.descricao, self.numero_quarto, self.capacidade, 
        self.obervacao, self.status, count_category_pk))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    model = Model(file, db)
    count_pk = AutoIncrementPk(model)
    obj = Room('Quarto Simples', 1, 2, 'Quarto Simples para duas pessoas', 'Reservado', model)
    a = obj.register_room(count_pk)
    print(a)
