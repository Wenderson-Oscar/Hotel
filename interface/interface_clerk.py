import PySimpleGUI as sg
from layout.clerk.layout_client import RegisterClient
from layout.clerk.layout_client_service import LayoutService
from layout.clerk.layout_checkout import LayoutCheckout
from layout.clerk.layout_cancel import LayoutCancel
from layout.clerk.layout_query import LayoutQueryCpf, LayoutQueryRoom, LayoutQueryPaid, LayoutQueryCheckin


class ApplicationClerk:

    def __init__(self) -> None:
        """interface do atendente"""
        menu_def = [['&Menu', ['&Cadastrar Hóspede', '&Serviço', '&Checkout', '&Cancelar Reserva']],
        ['&Ajuda', ['&Sobre']],
        ['&Configuração', ['&Sair']]]
        self.layout = [
            [sg.Menu(menu_def)],
            [sg.Text('Hotel borde', font=('Helvetica', 16), justification='center')],
            [sg.Button('Listar Todos os Clientes', key='listar_all'), 
            sg.Button('Consulta um Cliente', key='une_client'), 
            sg.Button('Consultar Cliente por Quarto', key='client_room'), 
            sg.Button('Consulta Hóspede que já pago', key='client_checkout'),
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

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            # Menu paara clerk
            elif event == 'Cadastrar Hóspede':
                layout_client = RegisterClient()
                layout_client.run()
                self.result('Cadastro Realizado')
            elif event == 'Serviço':
                layout_client_service = LayoutService()
                layout_client_service.run()
                self.result('Pedido Feito')
            elif event == 'Checkout':
                layout_checkout = LayoutCheckout()
                layout_checkout.run()
                self.result('Pagamento Realizado')
            elif event == 'Cancelar Reserva':
                layout_cancel = LayoutCancel()
                layout_cancel.run()
                self.result('Reserva Cancelada')
            # outros
            elif event == 'Sobre':
                sg.popup('Sobre', 'Desenvolvido por: Wenderson Oscar Santos Silva')
            elif event == 'Sair':
                self.window.close()
            # Consultas
            if event == 'listar_all':
                self.result('Listar Todos os Clientes do sistema de Hotel!')
            if event == 'une_client':
                layout_query1 = LayoutQueryCpf()
                layout_query1.run()
                self.result('Consulta um Cliente')
            if event == 'client_room':
                layout_query2 = LayoutQueryRoom()
                layout_query2.run()
                self.result('Consultar Cliente por Quarto')
            if event == 'client_checkout':
                layout_query3 = LayoutQueryPaid()
                layout_query3.run()
                self.result('Listar Hóspede que já pagaram')
            if event == 'available_room':
                self.result('Listar Quartos Disponível')
            if event == 'list_service':
                self.result('Listar Tipos de Serviços')
            if event == 'list room category':
                self.result('Listar Categorias de Quartos')
            if event == 'guest_who_has_reservation':
                layout_query4 = LayoutQueryCheckin()
                layout_query4.run()
                self.result('Consultar Hóspede que tenha Reserva')

        self.window.close()


if __name__ == "__main__":
    o = ApplicationClerk()
    o.run()