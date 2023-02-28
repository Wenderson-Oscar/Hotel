from model import Model, FileAuthentication, Databases


class Room:

    def __init__(self, room_cateogy: int, descricao: str, numero_quarto: int, capacidade: int,
    observacao: str, status: str, model: Model):
        self.room_category = room_cateogy
        self.descricao = descricao
        self.numero_quarto = numero_quarto
        self.capacidade = capacidade
        self.obervacao = observacao
        self.status =  status
        self.model = model

    
    def register_room(self):
        """inserir quarto no banco"""
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO quarto (descricao, numero_quarto, capacidade, observacao, status, 
        pk_categoria) VALUES (:descricao,:numero_quarto,:capacidade,:observacao,:status,:pk_categoria)""", 
        (self.descricao, self.numero_quarto, self.capacidade, self.obervacao, self.status, self.room_category))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    model = Model(file, db)
    obj = Room(2,'Quarto Simples', 2, 1, 'Quarto Simples, básico', 'Reservado', model)
    a = obj.register_room()
    print(a)
