from model import Model, FileAuthentication, Databases
from datetime import datetime
from automate_insertion_pk import AutoIncrementPk

class ReserveClient:

    def __init__(self, quant_hospedes: int, entrada_prevista: str,
                 saida_prevista: str, model: Model, antecipacao: float = None) -> None:
        self.quant_hospedes = quant_hospedes
        self.antecipacao = antecipacao
        self.entrada_prevista = entrada_prevista
        self.saida_prevista = saida_prevista
        self.model = model

    
    def register_reserve(self, automate_pk: AutoIncrementPk):
        """inserir reserva do cliente no banco"""
        count_client_pk = automate_pk.count_client()
        count_room_pk = automate_pk.count_room()
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO reserva (quant_hospedes, antecipacao, entrada_prevista, saida_prevista,
        data_criacao, pk_hospede, pk_quarto, pk_quarto_categoria) VALUES (?,?,?,?,?,?,?,?)""", 
        (self.quant_hospedes, self.antecipacao, self.entrada_prevista, self.saida_prevista, datetime.today(),
        count_client_pk, count_room_pk, count_room_pk))
        conn.commit()
        conn.close()
        return 'Registrado com Sucesso'
    

if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    model = Model(file, db)
    count_pk = AutoIncrementPk(model)
    obj = ReserveClient(2,'2023-02-30', '2023-03-02', model)
    a = obj.register_reserve(count_pk)
    print(a)