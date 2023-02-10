from database import DataBase
from abc import ABC, abstractmethod
from typing import Type
import json
import os

class OpenJson:

    def __init__(self, file_authenticade: dict):
        self.file_authenticade = file_authenticade
        self.url = os.path.join(os.getcwd(), self.file_authenticade)


    def open_json(self):
        with open(self.url, 'r') as self.file:
            self.dice = json.load(self.file)
            return self.dice


class LoginAbstrat():

    
    def login(self, username: str, password: str) -> bool:
        if username == self.username and password == self.password:
            return True
        else:
            return False


class Model:

    def __init__(self):
        self.data = DataBase()

    
    def access(self,username: str, password: str, user: LoginAbstrat):
        if user.login(username, password):
            return self.data.connect
        else:
            return 'Acesso Negado'

acs = OpenJson("authenticade.json")
model = Model()
authentication_file = {'username': 'admin', 'password': 'admin'}
result = model.access('admin', 'admin', acs)
if result == 'Acesso Negado':
    print(result)
else:
    print('Conexão com banco de dados realizada com sucesso!')
