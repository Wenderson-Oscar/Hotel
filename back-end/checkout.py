from model import Model, FileAuthentication, Databases
from automate_insertion_pk import AutoIncrementPk
from datetime import datetime, date

class Checkout:

    def __init__(self, valor_consumo: float, valor_pago: float, model: Model) -> None:
        self.valor_consumo = valor_consumo
        self.valor_pago = valor_pago
        self.model = model


    def register_checkout(self, automate_pk: AutoIncrementPk):
        """Insere os dados no checkout"""
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
        count_client_pk, count_room_pk, count_category_pk))
        conn.commit()
        conn.close()
        return 'Dados Inseridos'


class CalculateValueClient:

    def __init__(self, model: Model):
        self.model = model

    
    def calculate_value_total(self, automate_pk: AutoIncrementPk):
        """faz o calculo de pagamento total considerando diaria, multa, serviço"""
        count_reserva_pk = automate_pk.count_reserve()
        conn = self.model.database.connect()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT 
            r.quant_hospedes * c.valor + COALESCE(serv.preco, 0) AS preco_total,
            strftime('%s', r.saida_prevista) - strftime('%s', r.entrada_prevista) AS num_dias,
            CASE 
                WHEN ? > strftime('%s', r.saida_prevista, 'localtime')
                THEN (strftime('%s', r.saida_prevista, 'localtime')
            - strftime('%s', r.entrada_prevista, 'localtime')) / 86400 * (c.valor * 0.1)
            ELSE 0 
            END AS multa
        FROM reserva r
        INNER JOIN quarto q ON q.id_quarto = r.pk_quarto
        INNER JOIN categoria c ON c.id_categoria = q.pk_categoria
        LEFT JOIN reservar_servico rs ON c.id_categoria = rs.pk_categoria
        LEFT JOIN servico serv ON serv.id_servico = rs.pk_servico
        WHERE r.pk_hospede = ? """, (date.today(), str(count_reserva_pk)))
        result = cursor.fetchone()
        conn.close()
        if result is not None:
            return result[0]
        else:
            return 'Não a dados para calcular!'


if __name__ == "__main__":
    file = FileAuthentication("authenticade.json")
    db = Databases()
    model = Model(file, db)
    count_pk = AutoIncrementPk(model)
    obj1 = CalculateValueClient(model)
    #b = obj1.calculate_value_total(count_pk)
    #print(b)
    obj = Checkout(1610, 1610, model)
    a = obj.register_checkout(count_pk)
    print(a)
