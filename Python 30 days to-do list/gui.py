from functions import *
import FreeSimpleGUI as fsg

lable = fsg.Text("Type in tasks to-do: ")
input_box = fsg.InputText(tooltip="Enter a task to do", key="addtask")
add_button = fsg.Button("Add")
list_todo = fsg.Listbox(values=get_todos(), key='listtodos',enable_events=True, size=[50, 20])
edit_button = fsg.Button("Edit")


inputWindow = fsg.Window('My To-Do App',
                         layout=[[lable, input_box,add_button],[list_todo,edit_button]],
                         font=('Arial', 12) )
while True:
    event, values = inputWindow.read()
    match event:
        case "Add":
            todos = get_todos()
            addtodo = values['addtask'] + '\n'
            todos.append(addtodo)
            write_todos(todos)
            inputWindow['listtodos'].update(values=todos)
        case fsg.WIN_CLOSED:
            break
        case 'Edit':
            todo_edit = values['listtodos'][0]
            new_todo = values['addtask']
            todos = get_todos()
            index=todos.index(todo_edit)
            todos[index] = new_todo
            write_todos(todos)
            inputWindow['listtodos'].update(values=todos)
        case 'listtodos':
            inputWindow['addtask'].update(value=values['listtodos'][0])



inputWindow.close()