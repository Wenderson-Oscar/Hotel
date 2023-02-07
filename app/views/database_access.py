from app.models.database import DataBase
from interface_user import InterfaceUser
from typing import Type
from admin import AdminQuery

   
class Database:
    def __init__(self, data):
        self.data = data
        
    def access(self, user):
        if user.login():
            return self.data
        else:
            return "Acesso negado."
            
data = {"user1": {"password": "1234", "data": "Dados do usuário 1"},
        "user2": {"password": "5678", "data": "Dados do usuário 2"}}
        
users = [User(username, info["password"]) for username, info in data.items()]
        
for user in users:
    db = Database(data[user.username]["data"])
    print(db.access(user))
