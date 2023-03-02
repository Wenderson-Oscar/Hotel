import PySimpleGUI as sg
from interface_clerk import ApplicationClerk


class ApplicationAdmin:

    def __init__(self) -> None:
        menu_def = [['&Ajuda', ['&Tutorial', '&Sobre']]]
        self.layout = [
            [sg.Menu(menu_def)],
            [sg.Text('Hotel borde', justification='center')],
            [sg.Button('Cadastrar Funcionario')],
            [sg.Button('Cadastrar Categoria')],
            [sg.Button('Cadastrar Quarto')],
            [sg.Button('Cadastrar Serviços')],
            [sg.Button('Consultas')]
        ]

        self.window = sg.Window('Sistema de hotel', self.layout, element_justification='center',
        resizable=True, size=(600, 600))


    def select_menu_admin(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            # Menu
            elif event == 'Sobre':
                sg.popup('Sobre', 'Desenvolvido por: Wenderson Oscar Santos Silva')
            elif event == 'Tutorial':
                sg.popup('Tutorial')
            elif event == 'Cadastrar Hóspede':
                sg.popup('Cadastro de hospede')
            elif event == 'Serviço':
                sg.popup('serviço')
            elif event == 'Checkout':
                sg.popup('checkout')
            elif event == 'Cancelar Reserva':
                sg.popup('Cancelar reserva')
            # Criações
            if event == 'Cadastrar Categoria':
                sg.popup('Cadastrar Categoria')
            if event == 'Cadastrar Quarto':
                sg.popup('Cadastrar Quarto')
            if event == 'Cadastrar Funcionario':
                sg.popup('Cadastrar Funcionario')
            if event == 'Cadastrar Serviços':
                sg.popup('Cadastrar Serviços')
            # Mudar de Janela
            if event == 'Consultas':
                consult = ApplicationClerk()
                self.window.close()
                consult.select_menu_clerk()


        self.window.close()


if __name__ == "__main__":
    o = ApplicationAdmin()
    o.select_menu_admin()