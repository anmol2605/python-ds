import PySimpleGUI as sg
import numpy as np

# Define the layout of the GUI
layout = [
    [sg.Text('Matrix Calculator', font=('Helvetica', 20))],
    [sg.Text('Matrix A:'), sg.InputText(key='-MATRIX_A-')],
    [sg.Text('Matrix B:'), sg.InputText(key='-MATRIX_B-')],
    [sg.Button('Add'), sg.Button('Subtract'), sg.Button('Multiply')],
    [sg.Text('Result:')],
    [sg.Output(size=(60, 20), key='-OUTPUT-')],
    [sg.Button('Exit')]
]

window = sg.Window('Matrix Calculator', layout, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event in ['Add', 'Subtract', 'Multiply']:
        matrix_a = np.array(eval(values['-MATRIX_A-']))
        matrix_b = np.array(eval(values['-MATRIX_B-']))
        
        if event == 'Add':
            result = matrix_a + matrix_b
        elif event == 'Subtract':
            result = matrix_a - matrix_b
        elif event == 'Multiply':
            result = np.dot(matrix_a, matrix_b)
        
        window['-OUTPUT-'].update('')
        print(result)

window.close()