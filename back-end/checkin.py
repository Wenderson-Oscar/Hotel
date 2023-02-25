from model import Model, FileAuthentication, Databases
from automate_insertion_pk import AutoIncrementPk
from datetime import datetime

class Checkin:

    def __init__(self, model: Model) -> None:
        self.model = model


    def register_checkin(self, automate_pk: AutoIncrementPk):
        count_employee_pk = automate_pk.count_employee()
        count_reserve_pk = automate_pk.count_reserve()
        count_client_pk = automate_pk.count_client()
        count_room_pk = automate_pk.count_room()
        count_category_pk = automate_pk.count_category()
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO checkin (data_criacao, pk_funcionario, pk_reserva, pk_reserva_hospede,
        pk_reserva_quarto, pk_reserva_categoria) VALUES (?,?,?,?,?,?)""", (datetime.today(), 
        count_employee_pk, count_reserve_pk, count_client_pk, count_room_pk, count_category_pk))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'
    

if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    model = Model(file, db)
    count_pk = AutoIncrementPk(model)
    obj = Checkin(model)
    a = obj.register_checkin(count_pk)
    print(a)