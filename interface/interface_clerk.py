import PySimpleGUI as sg


class ApplicationClerk:

    def __init__(self) -> None:
        menu_def = [['&Menu', ['&Cadastrar Hóspede', '&Serviço', '&Checkout', '&Cancelar Reserva']],
        ['&Ajuda', ['&Tutorial', '&Sobre']],
        ['&Voltar', ['&Voltar Admin']]]
        self.layout = [
            [sg.Menu(menu_def)],
            [sg.Text('Hotel borde', justification='center')],
            [sg.Button('Listar Todos os Clientes')],
            [sg.Button('Consulta um Cliente')],
            [sg.Button('Consultar Cliente por Quarto')],
            [sg.Button('Listar Hóspede que já pagaram')],
            [sg.Button('Listar Quartos Disponível')],
            [sg.Button('Listar Tipos de Serviços')],
            [sg.Button('Listar Categorias de Quartos')],
            [sg.Button('Consultar Hóspede que tenha Reserva')],
        ]

        self.window = sg.Window('Sistema de hotel', self.layout, element_justification='center',
        resizable=True, size=(600, 600))


    def select_menu_clerk(self):
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
            elif event == 'Voltar Admin':
                sg.popup('Voltar para admin')
            # Consultas
            if event == 'Listar Todos os Clientes':
                sg.popup('Lista Todos os CLientes')
            if event == 'Consulta um Cliente':
                sg.popup('Consulta um Cliente')
            if event == 'Consultar Cliente por Quarto':
                sg.popup('Consultar Cliente por Quarto')
            if event == 'Listar Hóspede que já pagaram':
                sg.popup('Listar Hóspede que já pagaram')
            if event == 'Listar Quartos Disponível':
                sg.popup('Listar Quartos Disponível')
            if event == 'Listar Tipos de Serviços':
                sg.popup('Listar Tipos de Serviços')
            if event == 'Listar Categorias de Quartos':
                sg.popup('Listar Categorias de Quartos')
            if event == 'Consultar Hóspede que tenha Reserva':
                sg.popup('Consultar Hóspede que tenha Reserva')

        self.window.close()


if __name__ == "__main__":
    o = ApplicationClerk()
    o.select_menu_clerk()