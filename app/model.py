from database import DataBase
from abc import ABC, abstractmethod
from typing import Type
import json
import os


class OpenJson:

    def __init__(self, file_authenticade: dict):
        self.file_authenticade = file_authenticade
        self.url = os.path.join(os.getcwd(), self.file_authenticade)


    def open_file(self):
        with open(self.url, 'r') as self.file:
            self.dice = json.load(self.file)
            return self.dice


class Model:

    def __init__(self):
        self.data = DataBase()

    
    def login(self, username: str, password: str, file_authenticade: OpenJson) -> bool:
        self.authenticade = file_authenticade.open_file()
        for row in self.authenticade.values():
            if username == row.get('username')  and password == row.get('password'):
                return self.data.connect
            else:
                return "Acesso Negado!"

a = OpenJson("authenticade.json")
d = Model()
c = d.login('admin','admin',a)
print(c)
