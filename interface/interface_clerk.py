import PySimpleGUI as sg


class ApplicationClerk:

    def __init__(self) -> None:
        menu_def = [['&Menu', ['&Cadastrar Hóspede', '&Serviço', '&Checkout', '&Cancelar Reserva']],
        ['&Ajuda', ['&Sobre']],
        ['&Configuração', ['&Sair']]]
        self.layout = [
            [sg.Menu(menu_def)],
            [sg.Text('Hotel borde', font=('Helvetica', 16), justification='center')],
            [sg.Button('Listar Todos os Clientes', key='listar_all'), 
            sg.Button('Consulta um Cliente', key='une_client'), 
            sg.Button('Consultar Cliente por Quarto', key='client_room'), 
            sg.Button('Listar Hóspede que já pagaram', key='list_client_checkout'),
            sg.Button('Listar Quartos Disponível', key='available_room'), 
            sg.Button('Listar Tipos de Serviços', key='list_service')],
            [sg.Button('Listar Categorias de Quartos', key='list room category'), 
            sg.Button('Consultar Hóspede que tenha Reserva', key='guest_who_has_reservation')],
            [sg.Column([[sg.Text('Área de Exibição')],[sg.Output(size=(150, 100), key='exibir')],], 
            vertical_alignment='center', justification='center')]
        ]

        self.window = sg.Window('Sistema de hotel', self.layout, element_justification='center',
        resizable=True, size=(1060, 640))


    def result(self, result):
        self.window['exibir'].update(f'{result}')

    def select_menu_clerk(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            # Menu paara clerk
            elif event == 'Cadastrar Hóspede':
                sg.popup('Aqui onde tera um layout temporario para cadastro')
                self.result('Cadastro de hospede')
            elif event == 'Serviço':
                sg.popup('Sistema onde sera registado os tipos de serviços')
                self.result('serviço')
            elif event == 'Checkout':
                sg.popup('layout temporario onde sera registrado o checkout')
                self.result('checkout')
            elif event == 'Cancelar Reserva':
                sg.popup('janela temporaria onde ira pegar os dados do hospede para cancelar a reserva')
                self.result('Cancelar reserva')
            # outros
            elif event == 'Sobre':
                sg.popup('Sobre', 'Desenvolvido por: Wenderson Oscar Santos Silva')
            elif event == 'Sair':
                self.window.close()
            # Consultas
            if event == 'listar_all':
                self.result('Listar Todos os Clientes do sistema de Hotel!')
            if event == 'une_client':
                self.result('Consulta um Cliente')
            if event == 'client_room':
                self.result('Consultar Cliente por Quarto')
            if event == 'list_client_checkout':
                self.result('Listar Hóspede que já pagaram')
            if event == 'available_room':
                self.result('Listar Quartos Disponível')
            if event == 'list_service':
                self.result('Listar Tipos de Serviços')
            if event == 'list room category':
                self.result('Listar Categorias de Quartos')
            if event == 'guest_who_has_reservation':
                self.result('Consultar Hóspede que tenha Reserva')

        self.window.close()


if __name__ == "__main__":
    o = ApplicationClerk()
    o.select_menu_clerk()