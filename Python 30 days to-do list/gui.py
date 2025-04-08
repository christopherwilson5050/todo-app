from functions import *
import FreeSimpleGUI as fsg
import time

fsg.theme('DarkTeal12')

time_lable = fsg.Text('', key="clock")
lable = fsg.Text("Type in tasks to-do: ")
input_box = fsg.InputText(tooltip="Enter a task to do", key="addtask")
add_button = fsg.Button("Add")
list_todo = fsg.Listbox(values=get_todos(), key='listtodos',enable_events=True, size=[50, 20])
edit_button = fsg.Button("Edit")
completed_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")

inputWindow = fsg.Window('My To-Do App',
                         layout=[[time_lable],[lable, input_box,add_button],[list_todo,edit_button, completed_button],[exit_button]],
                         font=('Arial', 12) )
while True:
    event, values = inputWindow.read(timeout=10)
    inputWindow['clock'].update(value=time.strftime("%d/%m/%Y, %H:%M:%S"))
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
            try:
                todo_edit = values['listtodos'][0]
                new_todo = values['addtask']
                todos = get_todos()
                index=todos.index(todo_edit)
                todos[index] = new_todo
                write_todos(todos)
                inputWindow['listtodos'].update(values=todos)
            except IndexError:
                fsg.popup('Please select a task to edit.',font=('Arial', 12))
        case 'listtodos':
            inputWindow['addtask'].update(value=values['listtodos'][0])
        case 'Complete':
            try:
                todo_complete = values['listtodos'][0]
                todos = get_todos()
                todos.remove(todo_complete)
                write_todos(todos)
                inputWindow['listtodos'].update(values=todos)
                inputWindow['addtask'].update(value='')
            except IndexError:
                fsg.popup('Please select a task to complete.',font=('Arial', 12))
        case 'Exit':
            break







inputWindow.close()