import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do. ")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
layout = [[label], [input_box, add_button]]

window = sg.Window('My To-Do App', layout=layout)
window.read()
window.close()