from abc import ABC, abstractmethod
from admin import AdminQuery
from clerk import AttendantQuery
from app.models.database import DataBase


class InterfaceUser(ABC):

    def login(self, username: str, password: str) -> str:
      if username == self.username and password == self.password:
          return True
      else:
          return False

    def access(self, user):
        if user.login():
            return DataBase().conect
        else:
            return "Acesso negado."
            