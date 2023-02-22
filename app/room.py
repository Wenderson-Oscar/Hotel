from model import Model, FileAuthentication, Databases

class Room:

    def __init__(self, descricao: str, numero_quarto: int, capacidade: int,
    observacao: str, status: str, pk_categoria: int, model: Model):
        self.descricao = descricao
        self.numero_quarto = numero_quarto
        self.capacidade = capacidade
        self.obervacao = observacao
        self.status =  status
        self.model = model
        self.pk_categoria = pk_categoria

    
    def register_room(self):
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO quarto (descricao, numero_quarto, capacidade, observacao, status, 
        pk_categoria) VALUES (?,?,?,?,?,?)""", (self.descricao, self.numero_quarto, self.capacidade, self.obervacao, self.status,
        self.pk_categoria))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    obj = Room('Quarto Simples', 1, 2, 'Quarto Simples para duas pessoas', 'Ativo', 1, Model(file, db))
    a = obj.register_room()
    print(a)
