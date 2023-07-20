import PySimpleGUI as sg
import converters

enter_feet = sg.Text("Enter feet:"), sg.InputText(key="feet")

enter_inches = sg.Text("Enter inches:"), sg.InputText(key="inches")

convert = sg.Button("Convert")

output = sg.Text(key="output")

exit_button = sg.Button("Exit")

window = sg.Window("Converter", layout = [[enter_feet, enter_inches], [convert, exit_button, output]])

while True:
    event, value =  window.read()
    match event:
        case "Convert":
            try:
                feet = float(value["feet"])
                inches = float(value["inches"])

                result = str(converters.convert(feet, inches)) + " m"
                window["output"].update(result)
            except ValueError:
                sg.popup("Please enter a value")
    
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()