from database import DataBase
from abc import ABC, abstractmethod
from typing import Type
import json
import os

class OpenJson:

    def __init__(self, file_authenticade: str):
        self.file_authenticade = file_authenticade
        self.url = os.path.join(os.getcwd(), self.file_authenticade)



    def open_json(self):
        with open(self.url, 'r') as self.file:
            self.dice = json.load(self.file)
            print(self.dice)


class Authenticade:

    def senha(self):
        self.senhas = {'admin': {'username': 'admin', 'password': 'admin'},
        'clerk': {'username': 'clerk', 'password': '123'}}


class Login(ABC):


    @abstractmethod
    def login(self, username: str, password: str):
        if username == self.username and password == self.password:
            return True
        else:
            return False


class Model:

    def __init__(self):
        self.data = DataBase()

    
    def access(self, user: Type[Login]):
        if user.login():
            return self.data.connect
        else:
            return 'Acesso Negado'


obj = OpenJson("authenticade.json")
obj.open_json()