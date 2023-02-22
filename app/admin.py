from employee import Employee
from model import FileAuthentication, Databases, Model

class AdminQuery(Employee):

  # CRUD / ADM
  def __create(self, txt: str) -> str:
    conn = self.model.database.connect()
    cursor = conn.cursor()
    cursor.execute(txt)
    conn.commit()
    conn.close()

  def get_create(self, txt: str):
    return self.__create(txt)

  def __read(self, txt: str) -> str:
    conn = self.model.database.connect()
    cursor = conn.cursor()
    cursor.execute(txt)
    for row in cursor.fetchall():
      return row

  def get_read(self, txt: str):
    return self.__read(txt)

  def __update(self, txt: str) -> str:
    conn = self.model.database.connect()
    cursor = conn.cursor()
    cursor.execute(txt)
    conn.commit()
    conn.close()

  def get_update(self, txt):
    return self.__update(txt)

  def __delete(self, txt: str) -> str:
    conn = self.model.database.connect()
    cursor = conn.cursor()
    cursor.execute(txt)
    self.conn.commit()
    self.conn.close()

  def get_delete(self, txt):
    return self.__delete(txt)


if __name__ == "__main__":
  file = FileAuthentication("authenticade.json")
  bd = Databases()
  teste = AdminQuery('Oscar','12332112332122','988888817','oscar@gmail.com','M','2002-02-02','0','Gerente','213',Model(file, bd),'1','admin')
  a = teste.get_read("SELECT * FROM funcionario")
  print(a)
