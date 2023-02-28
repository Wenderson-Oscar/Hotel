from model import Model, FileAuthentication, Databases


class CancelHosting:

    def __init__(self, nome: str, cpf: str, model: Model) -> None:
        self.nome = nome
        self.cpf = cpf
        self.model = model


    def cancel_client(self):
        """Cancelar hospede e tudo relacionado"""
        conn = self.model.database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM hospede WHERE hospede.nome = :nome_param AND hospede.cpf = :cpf_param"""
        parametros = {'nome_param': self.nome, 'cpf_param': self.cpf}
        cursor.execute(sql, parametros)
        conn.commit()
        conn.close()
        return 'HOSPEDE DELETADO, ASSIM COMO TUDO RELACIONADO AO CLIENTE!'
    

if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    model = Model(file, db)
    obj = CancelHosting('Joana Silva', '99332126322', model)
    a = obj.cancel_client()
    print(a)
