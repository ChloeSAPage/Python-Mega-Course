import PySimpleGUI as sg
import converters

label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter Kilometeres", key="kms")
miles_button = sg.Button("Convert")
 
output = sg.Text(key="output")
 
 
window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = float(values["kms"])
            result = converters.km_to_miles(km)
            window['output'].update(value=f"{result} miles")
        case sg.WIN_CLOSED:
            break
 
window.close()