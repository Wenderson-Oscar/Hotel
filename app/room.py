class Room:

    def __init__(self, descricao: str, numero_quarto: int, capacidade: int,
    observacao: str, status: str):
        self.descricao = descricao
        self.numero_quarto = numero_quarto
        self.capacidade = capacidade
        self.obervacao = observacao
        self.status =  status

    
    def register_room(self):
        pass