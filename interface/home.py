import PySimpleGUI as sg
from interface_clerk import ApplicationClerk
from interface_admin import ApplicationAdmin


class HotelSystem:

    def __init__(self):
        self.layout_main = [
            [sg.Text('Hotel borde', justification='center')],
            [sg.Text('Sistema de Login', font=('Helvetica', 20), justification='center')],
            [sg.Text('Usuário:'), sg.Input(key='usuario')],
            [sg.Text('Senha:'), sg.Input(key='senha', password_char='*')],
            [sg.Button('Entrar', size=(10, 1), button_color=('white', '#4B8BBE')),
            sg.Button('Sair', size=(10, 1), button_color=('white', '#B02B2C'))]
            ]

        self.window = sg.Window('Sistema de hotel', self.layout_main, element_justification='center',
        resizable=True, size=(600, 600))


    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'Sair':
                break
            if values['usuario'] == 'admin' and values['senha'] == 'admin':
                interface_admin = ApplicationAdmin()
                self.window.close()
                interface_admin.select_menu_admin()
            elif values['usuario'] == 'clerk' and values['senha'] == '123':
                app = ApplicationClerk()
                self.window.close()
                app.select_menu_clerk()
            else:
                sg.popup('Usuário ou senha inválidos!')

        self.window.close()

if __name__ == "__main__":
    oj = HotelSystem()
    oj.run()