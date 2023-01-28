import sqlite3

class Banco:

  def __init__(self) -> None:
    self.connect = sqlite3.connect("sqlite3.db")
    self.cursor = self.connect.cursor()
    self.__create_tables()


  def __create_tables(self) -> str:
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS hospede 
    (
      id_hospede INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
      nome VARCHAR(100),
      cpf VARCHAR(11), 
      email VARCHAR(100), 
      telefone VARCHAR(30),
      sexo CHAR(1), 
      data_nascimento DATE, 
      dados_bancarios VARCHAR(100),
      senha_bancaria VARCHAR(50), 
      data_criacao DATETIME
    )
    """)
    self.cursor.execute("""CREATE TABLE IF NOT EXISTS funcionario
    (
      id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
      nome VARCHAR(100),
      cpf VARCHAR(11), 
      email VARCHAR(100), 
      telefone VARHCAR(30), 
      sexo CHAR(1),
      data_nascimento DATE, 
      endereco VARCHAR(100), 
      matricula VARCHAR(100),
      dados_bancario VARCHAR(100), 
      nivel_acesso CHAR(1), 
      senha_acesso VARCHAR(100),
      cargo VARCHAR(100), 
      data_adimissao DATETIME, 
      data_criacao DATETIME
    )
    """)
    self.cursor.execute(""" CREATE TABLE IF NOT EXISTS categoria
    (
      id_categoria INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      descricao VARCHAR(100),
      valor FLOAT
    )
    """)
    self.cursor.execute(""" CREATE TABLE IF NOT EXISTS servico
    (
      id_servico INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      descricao VARHCAR(100),
      preco FLOAT,
      status VARCHAR(45),
      pk_funcionario INTEGER NOT NULL,
      CONSTRAINT pk_funcionario_idfuncionario
      FOREIGN KEY (pk_funcionario)
      REFERENCES funcionario(id_funcionario)
      ON DELETE CASCADE
    )
    """)
    self.cursor.execute(""" CREATE TABLE IF NOT EXISTS reservar_servico
    (
      id_reservar_servico INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      data_criacao DATE,
      pk_servico INTEGER NOT NULL,
      pk_categoria INTEGER NOT NULL,
      CONSTRAINT pk_servico_pk_categoria_ids
      FOREIGN KEY (pk_servico)
      REFERENCES servico(id_servico)
      FOREIGN KEY (pk_categoria)
      REFERENCES categoria(id_categoria)
      ON DELETE CASCADE
    )
    """)
    self.cursor.execute(""" CREATE TABLE IF NOT EXISTS quarto
    (
      id_quarto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      descricao VARCHAR(100),
      numero_quarto INTEGER,
      capacidade INTEGER,
      observacao VARCHAR(200),
      status VARCHAR(50),
      pk_categoria INTEGER NOT NULL,
      CONSTRAINT pk_categoria_id_categoria
      FOREIGN KEY (pk_categoria)
      REFERENCES categoria(id_categoria)
      ON DELETE CASCADE
    )
    """)
    self.cursor.execute(""" CREATE TABLE IF NOT EXISTS reserva
    (
      id_reserva INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      quant_hospedes INTEGER,
      antecipacao FLOAT,
      entrava_prevista DATETIME,
      saida_prevista DATETIME,
      data_criacao DATETIME,
      pk_hospede INTEGER NOT NULL,
      pk_quarto INTEGER NOT NULL,
      pk_quarto_categoria INTEGER NOT NULL,
      CONSTRAINT pk_hospode_id_hospede
      FOREIGN KEY (pk_hospede)
      REFERENCES hospede (id_hospede)
      CONSTRAINT pk_quarto_id_quarto
      FOREIGN KEY (pk_quarto)
      REFERENCES quarto(id_quarto)
      CONSTRAINT pk_quarto_categoria_pk_categoria
      FOREIGN KEY (pk_quarto_categoria)
      REFERENCES quarto(pk_categoria)
      ON DELETE CASCADE
    )
    """)
    self.cursor.execute(""" CREATE TABLE IF NOT EXISTS checkin
    (
      id_checkin INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      data_criacao DATETIME,
      pk_funcionario INTEGER NOT NULL,
      pk_reserva INTEGER NOT NULL,
      pk_reserva_hospede INTEGER NOT NULL,
      pk_reserva_quarto INTEGER NOT NULL,
      pk_reserva_categoria INTEGER NOT NULL,
      CONSTRAINT pk_funcionario_id_funcionario_in
      FOREIGN KEY(pk_funcionario)
      REFERENCES funcionario (id_funcionario)
      CONSTRAINT pk_reserva_reservahospede_reservaquarto_reservacategoria_in
      FOREIGN KEY (
        pk_reserva,
        pk_reserva_hospede,
        pk_reserva_quarto, 
        pk_reserva_categoria
      )
      REFERENCES reserva (id_reserva, pk_hospede, pk_quarto, pk_categoria)
      ON DELETE CASCADE
    )
    """)
    self.cursor.execute(""" CREATE TABLE IF NOT EXISTS checkout 
    (
      id_checkout INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
      valor_consumo FLOAT,
      valor_pago FLOAT,
      data_criacao DATETIME,
      pk_funcionario INTEGER NOT NULL,
      pk_reserva INTEGER NOT NULL,
      pk_reserva_hospede INTEGER NOT NULL,
      pk_reserva_quarto INTEGER NOT NULL,
      pk_reserva_categoria INTEGER NOT NULL,
      CONSTRAINT pk_funcionario_id_funcionario_out
      FOREIGN KEY (pk_funcionario)
      REFERENCES funcionario (id_funcionario)
      CONSTRAINT pk_funcionario_reserva_reservahospede_reservaquarto_reservacategoria_out
      FOREIGN KEY (
        pk_reserva,
        pk_reserva_hospede,
        pk_reserva_quarto,
        pk_reserva_categoria
        )
      REFERENCES reserva (id_reserva, pk_hospede, pk_quarto, pk_cateogira)
      ON DELETE CASCADE
    )
    """)
    self.connect.commit()
    self.cursor.close()

  # CRUD / ADM
  def _create(self, txt: str) -> str:
    self.cursor.execute(txt)
    self.connect.commit()
    self.cursor.close()

  def _read(self, txt: str) -> str:
    self.cursor.execute(txt)
    for row in self.cursor.fetchall():
      return row

  def _update(self, txt: str) -> str:
    self.cursor.execute(txt)
    self.connect.commit()
    self.connect.close()

  def _delete(self, txt: str) -> str:
    self.cursor.execute(txt)
    self.connect.commit()
    self.connect.close()

  # Read Function ADM/CLERK

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
    INNER JOIN reserva ON hospede.id_hospede = reserva.pk_hospede AND
    INNER JOIN quarto ON quarto.id_quarto = reserva.pk_quarto""")
    for row in self.cursor.fetchall():
      return row

  def _search_customer_by_room_number(self, number: int) -> str:
    self.cursor.execute(f"""
    SELECT 
    hospede.nome, hospede.sexo, hospede.telefone, quarto.descricao, 
    quarto.capacidade, quarto.observacao, quarto.status, quarto.numero_quarto
    FROM hospede 
    WHERE quarto.numero_quarto = {number}
    INNER JOIN reserva ON hospede.id_hospede = reserva.pk_hospede AND
    INNER JOIN quarto ON quarto.id_quarto = reserva.pk_quarto AND
    INNER JOIN categoria ON categoria.id_categoria = quarto.pk_categoria""")
    for row in self.cursor.fetchall():
      return row

  def _check_the_customer_total_payable(self, cpf: str) -> str:
    pass

  def _search_for_available_rooms(self) -> str:
    pass

  def search_types_of_services(self) -> str:
    pass

  def list_room_categories(self) -> str:
    pass

  def search_person_by_checkin(self, cpf: str) -> str:
    pass


if __name__ == "__main__":
  obj = Banco()