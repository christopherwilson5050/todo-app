from functions import *
import FreeSimpleGUI as fsg

lable = fsg.Text("Type in tasks to-do: ")
input_box = fsg.InputText(tooltip="Enter a task to do", key="addtask")
add_button = fsg.Button("Add")

inputWindow = fsg.Window('My To-Do App',
                         layout=[[lable, input_box,add_button]],
                         font=('Arial', 12) )
while True:
    event, values = inputWindow.read()
    match event:
        case "Add":
            todos = get_todos()
            addtodo = values['addtask'] + '\n'
            todos.append(addtodo)
            write_todos(todos)
        case fsg.WIN_CLOSED:
            break


inputWindow.close()