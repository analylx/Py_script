import PySimpleGUI as sg

sg.main()
form = sg.FlexForm('My first GUI')
layout = [ [sg.Text('Enter your name'), sg.InputText()],
           [sg.OK()] ]
button, (name,) = form.LayoutAndRead(layout)