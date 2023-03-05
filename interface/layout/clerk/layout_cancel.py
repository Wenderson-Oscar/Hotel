import PySimpleGUI as sg


class LayoutCancel:

    def __init__(self):
        """layout para cancelar reserva"""
        self.layout = [
            [sg.Text('Nome:', size=(12, 1)), sg.InputText(key='nome', size=(50,1))],
            [sg.Text('CPF:', size=(12, 1)), sg.InputText(key='cpf', size=(50,1))],
            [sg.T()],
            [sg.T(size=(23,1)), sg.Button('REGISTRAR', bind_return_key=True), sg.T(size=(2,1)), sg.Button('CANCELAR')]
        ]

        self.window = sg.Window('Cancelar Reserva', self.layout, size=(580,150))

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'CANCELAR':
                break
            elif event == 'REGISTRAR':
                #Validações
                #Logica
                sg.popup('logica do registro')
        self.window.close()


if __name__ == "__main__":
    obj = LayoutCancel()
    obj.run()
