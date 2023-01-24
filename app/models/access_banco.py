from database import Banco

class Model:
    
    def __init__(self):
        self.conectar = Banco().connect