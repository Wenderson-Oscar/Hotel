from app.models.database import DataBase
from interface_user import InterfaceUser
from typing import Type

class AccessDataBase:
    
    def __init__(self):
        self.conectar = DataBase().connect

    def user(self, user: Type[InterfaceUser]):
        use = user.type_user()
        print(use)
