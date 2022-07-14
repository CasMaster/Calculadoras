from PySimpleGUI import PySimpleGUI as sg
import Calculadora_de_Circulos

# Layout
sg.theme('Dark Green 3')
layout = [
    [Calculadora_de_Circulos.welcome()]

]
# Janela
janela = sg.Window('Calculadora de Circulos', layout)

# ler os eventos
while True:
    evetos, valores = janela.read()
    if evetos == sg.WINDOW_CLOSED:
        break
