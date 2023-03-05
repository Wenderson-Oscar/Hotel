import PySimpleGUI as sg


class RegisterRoom:

    def __init__(self):
        """layout para registrar quarto"""
        self.layout = [
            [sg.Text('Descrição:', size=(20, 1)), sg.InputText(key='descricao', size=(50,1))],
            [sg.Text('Número do Quarto:', size=(20, 1)), sg.InputText(key='numero_quarto', size=(50,1))],
            [sg.Text('Capacidade:', size=(20, 1)), sg.InputText(key='capacidade', size=(5,1))],
            [sg.Text('Observação:', size=(20, 1)), sg.InputText(key='observacao', size=(50,1))],
            [sg.Text('Status:', size=(20, 1)), sg.Radio('Disponível', 'status', key='status_d', default=True),
             sg.Radio('Indisponível', 'status', key='status_i')],
            [sg.Text('Número da Categoria:', size=(20, 1)), sg.Input(key='numero_categoria', size=(50,1))],
            [sg.T()],
            [sg.T(size=(23,1)), sg.Button('REGISTRAR', bind_return_key=True), sg.T(size=(2,1)), sg.Button('CANCELAR')]
        ]

        self.window = sg.Window('Registrar Quarto', self.layout, size=(580,240), finalize=True)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'CANCELAR':
                break
            elif event == 'REGISTRAR':
                # Validações
                # Lógica
                sg.popup('Quarto registrado com sucesso!')
        self.window.close()


if __name__ == "__main__":
    obj = RegisterRoom()
    obj.run()
