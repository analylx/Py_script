import PySimpleGUI as sg
# Very basic form.  Return values as a list
form = sg.FlexForm('Simple data entry form')  # begin with a blank form
layout = [[sg.Text('Please enter NE IP, NE type (1800/1200/1300/1050)')],
          [sg.Text('Ne IP', size=(15, 1)),
           sg.InputText('200.200.')],
          [sg.Text('Ne Type', size=(15, 1)),
           sg.InputText('')], [sg.Submit(), sg.Cancel()]]
button, values = form.LayoutAndRead(layout)
print(button, values[0], values[1])