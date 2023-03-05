import PySimpleGUI as sg


class LayoutCheckout:

    def __init__(self):
        """layout para fazer pagamento"""
        self.layout = [
            [sg.Text('Valor de Consumo:', size=(23, 1)), sg.InputText(key='consumo_valor', size=(50,1))],
            [sg.Text('Valor Pago:', size=(23, 1)), sg.InputText(key='valor_pago', size=(50,1))],
            [sg.Text('Funcionario Responsavel:', size=(23, 1)), sg.InputText(key='funcionario', size=(50,1))],
            [sg.Text('N° Categoria:', size=(23, 1)), sg.InputText(key='n_categoria', size=(50,1))],
            [sg.Text('N° Quarto:', size=(23, 1)), sg.InputText(key='n_quarto', size=(50,1))],
            [sg.T()],
            [sg.T(size=(23,1)), sg.Button('REGISTRAR', bind_return_key=True), sg.T(size=(2,1)), sg.Button('CANCELAR')]
        ]

        self.window = sg.Window('Fazer Checkout', self.layout, size=(580,250))

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
    obj = LayoutCheckout()
    obj.run()
