import PySimpleGUI as sg                        # Part 1 - The import

class Tela:
    def __init__(self):
        #layout:
        layout = [
             [sg.Text("Diretório de Origem: "), sg.Input()],
             [sg.Text("Diretório de Destino: "), sg.Input()],
             [sg.Button('Ok')] 
        ]
        #janela:
        window = sg.Window('Copy Diretory', layout)   
        #extrair dados
        self.event, self.values = window.Read()

    def Start(self):
        print(self.values)
        print( type(self.values))

#tela = Tela()
#tela.Start()
