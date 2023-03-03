import PySimpleGUI as sg
from interface_clerk import ApplicationClerk


class ApplicationAdmin:

    def __init__(self) -> None:
        menu_def = [['&Ajuda', ['&Sobre']], ['&Configuração', ['&Sair']]
        ]
        self.layout = [
            [sg.Menu(menu_def)],
            [sg.Text('Hotel borde', justification='center')],
            [sg.Button('Cadastrar Funcionario', key='register_employee'),
            sg.Button('Cadastrar Categoria', key='register category'),
            sg.Button('Cadastrar Quarto', key='register_room'),
            sg.Button('Cadastrar Serviços', key='register_service'),
            sg.Button('Consultas')],
            [sg.Column([[sg.Text('Área de Exibição')],[sg.Output(size=(150, 100), key='exibir')],], 
            vertical_alignment='center', justification='center')]
        ]

        self.window = sg.Window('Sistema de hotel', self.layout, element_justification='center',
        resizable=True, size=(1060, 640))


    def result(self, result):
        self.window['exibir'].update(f'{result}')

    def select_menu_admin(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            # Menu
            elif event == 'Sobre':
                sg.popup('Sobre', 'Desenvolvido por: Wenderson Oscar Santos Silva')
            elif event == 'Sair':
                self.window.close()
            # Criações
            if event == 'register category':
                sg.popup('Layout Temporario','Layout temporario onde sera possível registra categoria')
                self.result('Cadastrar Categoria')
            if event == 'register_room':
                sg.popup('Layout Temporario','Layout temporario onde sera possível registra')
                self.result('Cadastrar Quarto')
            if event == 'register_employee':
                sg.popup('Layout Temporario','Layout temporario onde sera possível registra')
                self.result('Cadastrar Funcionario')
            if event == 'register_service':
                sg.popup('Layout Temporario','Layout temporario onde sera possível registra')
                self.result('Cadastrar Serviços')
            # Mudar de Janela
            if event == 'Consultas':
                consult = ApplicationClerk()
                self.window.close()
                consult.select_menu_clerk()


        self.window.close()


if __name__ == "__main__":
    o = ApplicationAdmin()
    o.select_menu_admin()