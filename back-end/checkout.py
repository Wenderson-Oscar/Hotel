from model import Model, FileAuthentication, Databases
from automate_insertion_pk import AutoIncrementPk
from datetime import datetime

class Checkout:

    def __init__(self, valor_consumo: float, valor_pago: float, model: Model) -> None:
        self.valor_consumo = valor_consumo
        self.valor_pago = valor_pago
        self.model = model


    def register_checkout(self, automate_pk: AutoIncrementPk):
        count_employee_pk = automate_pk.count_employee()
        count_reserve_pk = automate_pk.count_reserve()
        count_client_pk = automate_pk.count_client()
        count_room_pk = automate_pk.count_room()
        count_category_pk = automate_pk.count_category()
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO checkout (valor_consumo, valor_pago, data_criacao, pk_funcionario,
        pk_reserva, pk_reserva_hospede, pk_reserva_quarto, pk_reserva_categoria) VALUES (?,?,?,?,?,?,?,?)""",
        (self.valor_consumo, self.valor_pago, datetime.today(), count_employee_pk, count_reserve_pk, 
        count_client_pk, count_room_pk, count_room_pk))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'
    
    def calculate_total(self):
        pass
    

if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    model = Model(file, db)
    count_pk = AutoIncrementPk(model)
    obj = Checkout(300, 320, model)
    a = obj.register_checkout(count_pk)
    print(a)
