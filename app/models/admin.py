from app.models.clerk import AttendantQuery

class AdminQuery(AttendantQuery):

  # CRUD / ADM
  def __create(self, txt: str) -> str:
    self.cursor.execute(txt)
    self.connect.commit()
    self.cursor.close()

  def __read(self, txt: str) -> str:
    self.cursor.execute(txt)
    for row in self.cursor.fetchall():
      return row

  def __update(self, txt: str) -> str:
    self.cursor.execute(txt)
    self.connect.commit()
    self.connect.close()

  def __delete(self, txt: str) -> str:
    self.cursor.execute(txt)
    self.connect.commit()
    self.connect.close()

