from model import Model, FileAuthentication, Databases

class AutoIncrementPk:

    def __init__(self, model: Model):
        self.model = model

    
    def count_client(self):
        """contar a quantidade de hospede"""
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM hospede")
        result = cursor.fetchone()[0]
        #conn.close()
        return result
    
    def count_employee(self):
        """contar a quantidade de funcionario"""
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM funcionario")
        result = cursor.fetchone()[0]
        #conn.close()
        return result
    
    def count_service(self):
        """contar a quantidade de serviço existente"""
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM servico")
        result = cursor.fetchone()[0]
        #conn.close()
        return result
    
    def count_category(self):
        """contar a quantidade de categoria existente"""
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM categoria")
        result = cursor.fetchone()[0]
        #conn.close()
        return result
    
    def count_room(self):
        """contar a quantidade de quartos"""
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM quarto")
        result = cursor.fetchone()[0]
        #conn.close()
        return result


if __name__ == "__main__":
        file = FileAuthentication("authenticade.json")
        db = Databases()
        obj = AutoIncrementPk(Model(file, db))
        a = obj.count_client()
        b = obj.count_employee()
        c = obj.count_category()
        d = obj.count_service()
        e = obj.count_room()
        print(a, b, c, d, e)