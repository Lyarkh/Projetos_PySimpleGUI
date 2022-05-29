import PySimpleGUI as sg 

# Tipos de elementos utilizados na tela do GUI, criando o layout
layout = [
    [sg.Input(key='-INPUT-'), sg.Spin(
        ['km to mile', 
        'kg to pound', 
        'sec to min'], key='-UNITS-'), 
    sg.Button('Converter', key='-CONVERT-')],
    [sg.Text('Output', key='-OUTPUT-')]
    
]

# Criando tela do PySimpleGUI
window = sg.Window('Converter', layout)

# Loop Principal
while True:
    event, values = window.read()

    # Evento para caso clique no 'X', o aplicativo feche e pare o loop
    if event == sg.WIN_CLOSED:
        break

    # Pegando valor do input caso clique no botão com key '-CONVERT-'
    if event == '-CONVERT-':    
        input_value = values['-INPUT-']

        # Verificando se o valor é numérico
        if input_value.isnumeric():
            
            # Match case para calcular de acordo com a opção selecionada no 'spin'
            match values['-UNITS-']:
                case 'km to mile':
                    output = round(float(input_value) * 0.06214, 2)
                    output_string = f'{input_value} km are {output} miles.'

                case 'kg to pound':
                    output = round(float(input_value) * 2.20462, 2)
                    output_string = f'{input_value} kg are {output} pounds.'

                case 'sec to min':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} seconds are {output} minutes.'
            
        # Imprimindo resultado do calculo de acordo com a oçpão escolhida
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please enter a number')

# Fechando janela criada da aplicação
window.close()

