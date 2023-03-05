import PySimpleGUI as sg


class RegisterCategory:

    def __init__(self):
        """layout para registrar categoria de quarto"""
        self.layout = [
            [sg.Text('Descrição:', size=(10, 1)), sg.InputText(key='descricao', size=(50,1))],
            [sg.Text('Valor:', size=(10, 1)), sg.InputText(key='valor', size=(50,1))],
            [sg.T()],
            [sg.T(size=(23,1)), sg.Button('REGISTRAR', bind_return_key=True), sg.T(size=(2,1)), sg.Button('CANCELAR')]
        ]

        self.window = sg.Window('Registrar Categoria', self.layout, size=(580,140), finalize=True)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'CANCELAR':
                break
            elif event == 'REGISTRAR':
                # Validações
                # Lógica
                sg.popup('Categoria registrada com sucesso!')
        self.window.close()


if __name__ == "__main__":
    obj = RegisterCategory()
    obj.run()
