from app.models.database import DataBase
from interface_user import InterfaceUser

class AttendantQuery(DataBase, InterfaceUser):
  # Read Function 

  def __init__(self, username: str, passwod: str):
    self.username = username
    self.password = passwod


  def _list_all_guests(self) -> str:
    self.cursor.execute("""
    SELECT 
    hospede.nome, hospede.cpf, hospede.data_criacao
    FROM hospede 
    INNER JOIN reserva ON hospede.id_hospede = reserva.pk_hospede""")
    for row in self.cursor.fetchall():
      return row

  def _search_guest(self, cpf: str) -> str:
    self.cursor.execute(f"""
    SELECT 
    hospede.nome, hospede.cpf, hospede.sexo, hospede.email, 
    hospede.telefone, hospede.data_criacao, quarto.numero_quarto
    FROM hospede 
    WHERE hospede.cpf = {cpf}
    INNER JOIN reserva ON hospede.id_hospede = reserva.pk_hospede 
    INNER JOIN quarto ON quarto.id_quarto = reserva.pk_quarto""")
    for row in self.cursor.fetchall():
      return row

  def _search_customer_by_room_number(self, numero: int) -> str:
    self.cursor.execute(f"""
    SELECT 
    hospede.nome, hospede.sexo, hospede.telefone, quarto.descricao, 
    quarto.capacidade, quarto.observacao, quarto.status, quarto.numero_quarto,
    categoria.descricao, categoria.valor
    FROM hospede 
    WHERE quarto.numero_quarto = {numero}
    INNER JOIN reserva ON hospede.id_hospede = reserva.pk_hospede 
    INNER JOIN quarto ON quarto.id_quarto = reserva.pk_quarto 
    INNER JOIN categoria ON categoria.id_categoria = quarto.pk_categoria""")
    for row in self.cursor.fetchall():
      return row

  def _check_the_customer_total_payable(self, cpf: str) -> str:
    self.cursor.execute(f"""
    SELECT 
    hospede.nome, hospede.cpf, quarto,numero_quarto, quarto.observacao, 
    categoria.descricao, categoria.valor, reserva.entrada_prevista, reserva.saida_prevista,
    reserva.data_criacao, checkin.data_criacao, checkout.valor_consumo,
    checkout.valor_pago, checkout.data_criacao
    FROM hospede
    WHERE hospede.cpf = {cpf}
    INNER JOIN reserva ON hospede.id_hospede = reserva.pk_hospede 
    INNER JOIN quarto ON quarto.id_quarto = reserva.pk_quarto 
    INNER JOIN categoria ON categoria.id_categoria = quarto.pk_categoria 
    INNER JOIN checkin ON reserva.id_reserva = checkin.pk_reserva_hospede 
    INNER JOIN checkout ON reserva.id_reserva = checkout.pk_reserva_hospede
    """)
    for row in self.cursor.fetchall():
      return row

  def _search_for_available_rooms(self) -> str:
    self.cursor.execute("""
    SELECT 
    quarto.status, quarto.numero_quarto, quarto.descricao, categoria.descricao,
    categoria.valor 
    FROM quarto
    WHERE quarto.status = 'disponivel'
    INNER JOIN categoria ON categoria.id_categoria = quarto.pk_categoria""")

  def _search_types_of_services(self) -> str:
    self.cursor.execute("""
    SELECT 
    servico.descricao, servico.preco, servico.status
    funcionario.nome, funcionario.cargo
    FROM servico
    INNER JOIN funcionario ON funcionario.id_funcionario = servico.pk_funcionario""")
    for row in self.cursor.fetchall():
      return row

  def _list_room_categories(self) -> str:
    self.cursor.execute("""
    SELECT 
    quarto.descricao, quarto.numero_quarto, quarto.capacidade,
    quarto.status, categoria.descricao, categoria.valor
    FROM quarto
    INNER JOIN categoria ON categoria.id_categoria = quarto.pk_categoria""")
    for row in self.cursor.fetchall():
      return row

  def _search_person_by_checkin(self, nome: str) -> str:
    self.cursor.execute(f"""
    SELECT 
    hospede.nome, reserva.entrada_prevista, reserva.saida_prevista, 
    reserva.data_criacao, checkin.data_criacao
    FROM hospede
    WHERE hospede.nome = {nome}
    INNER JOIN reserva ON hospede.id_hospede = reserva.pk_hospede
    INNER JOIN checkin ON reserva.id_reserva = checkin.pk_reserva_hospede
    """)
    for row in self.cursor.fetchall():
      return row

  # INSERT Function 

  def _guest_registration(self, nome: str, cpf: str, telefone: int, email: str,
    sexo: str, nascimento: str, dados_bancario: str, senha: str):
    pass

  def _employee_registration(self, nome: str, cpf: str, email: str, telefone: str,
    sexo: str, endereco: str, nascimento: str, dados_bancario: str, cargo: str,
    matricula: str, data_admissao: str, nivel_acesso: None ,senha_acesso: None):
    pass

  def _register_room(self, descricao: str, numero_quarto: int, capacidade: int,
    observacao: str, status: str):
    pass

  def _register_category(self, descricao: str, valor: float):
    pass

  def _register_service(self, descricao: str, preco: float, status: str):
    pass
