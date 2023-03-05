import PySimpleGUI as sg


class LayoutQueryCpf:

    def __init__(self):
        """Interface para formulario de pesquisa, pesquisa hóspede pelo cpf"""
        self.layout = [
            [sg.Text('CPF:', size=(12, 1)), sg.InputText(key='cpf', size=(50,1))],
            [sg.T()],
            [sg.T(size=(23,1)), sg.Button('PESQUISAR', bind_return_key=True), sg.T(size=(2,1)), sg.Button('CANCELAR')]
        ]

        self.window = sg.Window('Pesquisar Cliente', self.layout, size=(580,100))

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'CANCELAR':
                break
            elif event == 'PESQUISAR':
                #Validações
                #Logica
                sg.popup('logica da consulta')
        self.window.close()


class LayoutQueryRoom:

    def __init__(self):
        """Interface para formulario de pesquisa, pesquisa hóspede pelo N° Quarto"""
        self.layout = [
            [sg.Text('N° Quarto:', size=(12, 1)), sg.InputText(key='n_quarto', size=(50,1))],
            [sg.T()],
            [sg.T(size=(23,1)), sg.Button('PESQUISAR', bind_return_key=True), sg.T(size=(2,1)), sg.Button('CANCELAR')]
        ]

        self.window = sg.Window('Pesquisar Cliente', self.layout, size=(580,100))

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'CANCELAR':
                break
            elif event == 'PESQUISAR':
                #Validações
                #Logica
                sg.popup('logica da consulta')
        self.window.close()


class LayoutQueryPaid:

    def __init__(self):
        """Interface para formulario de pesquisa, pesquisa hóspede que já pagaram pelo cpf"""
        self.layout = [
            [sg.Text('CPF:', size=(12, 1)), sg.InputText(key='cpf', size=(50,1))],
            [sg.T()],
            [sg.T(size=(23,1)), sg.Button('PESQUISAR', bind_return_key=True), sg.T(size=(2,1)), sg.Button('CANCELAR')]
        ]

        self.window = sg.Window('Pesquisar Cliente', self.layout, size=(580,100))

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'CANCELAR':
                break
            elif event == 'PESQUISAR':
                #Validações
                #Logica
                sg.popup('logica da consulta')
        self.window.close()


class LayoutQueryCheckin:

    def __init__(self):
        """Interface para formulario de pesquisa, pesquisa hóspede que tem checkin registrado,
        pesquisa pelo nome"""
        self.layout = [
            [sg.Text('Nome:', size=(12, 1)), sg.InputText(key='nome', size=(50,1))],
            [sg.T()],
            [sg.T(size=(23,1)), sg.Button('PESQUISAR', bind_return_key=True), sg.T(size=(2,1)), sg.Button('CANCELAR')]
        ]

        self.window = sg.Window('Pesquisar Cliente', self.layout, size=(580,100))

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'CANCELAR':
                break
            elif event == 'PESQUISAR':
                #Validações
                #Logica
                sg.popup('logica da consulta')
        self.window.close()


if __name__ == "__main__":
    obj = LayoutQueryCheckin()
    obj.run()
