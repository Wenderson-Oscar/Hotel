from model import FileAuthentication, Model, Databases

class Category:

    def __init__(self, descricao: str, valor: float, model: Model):
        self.descricao = descricao
        self.valor = valor
        self.model = model


    def register_category(self):
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO categoria (descricao, valor) VALUES (?,?)""", (self.descricao, self.valor))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    obj = Category('Simples', 300, Model(file, db))
    a = obj.register_category()
    print(a)
    