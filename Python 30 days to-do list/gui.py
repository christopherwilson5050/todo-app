from functions import *
import FreeSimpleGUI as fsg

lable = fsg.Text("Type in tasks to-do: ")
input_box = fsg.InputText(tooltip="Enter a task to do")
add_button = fsg.Button("Add")

inputWindow = fsg.Window('My To-Do App', layout=[[lable, input_box],[add_button]] )
inputWindow.read()
inputWindow.close()