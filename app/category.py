from model import FileAuthentication, Model, Databases


class RoomCategory:

    def __init__(self, descricao: str, valor: float, model: Model):
        self.descricao = descricao
        self.valor = valor
        self.model = model


    def register_category(self):
        """inserir dados do checkin"""
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO categoria (descricao, valor) VALUES (:descricao,:valor)""", (self.descricao, self.valor))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    obj = RoomCategory('Luxo', 800, Model(file, db))
    a = obj.register_category()
    print(a)
    