from functions import *
import time
date = time.strftime("%d/%m/%Y, %H:%M:%S")
print(date)
print(date)

while True:

    user_promp = input("type add or show or edit or exit or complete: ")
    todo = user_promp
    todo = todo.strip()


    if user_promp.startswith('add') or user_promp.startswith('new') :
        todo = user_promp[4:]+"\n"
        #file = open('todostore.txt', 'r')
        #todos = file.readlines()
        #file.close()

        #file = open('todostore.txt', 'w')
        #file.writelines(todos)
        #file.close()
        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_promp.startswith('show'):

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.title()
            showvar = f"{index + 1}: {item.capitalize()}"
            print(showvar)

    elif user_promp.startswith('edit'):
        try:
            number = int(user_promp[5:])
            number = number - 1

            todos = get_todos()

            edittedtask = input("enter in the edited task: ")+'\n'
            todos[number] = edittedtask
            write_todos(todos)
        except ValueError:
            print("Invalid command.")
            continue


    elif  user_promp.startswith('complete')  :
        try:
            removeval = int(user_promp[9:])
            removeval = removeval - 1

            todos = get_todos()
            removeddone = todos[removeval]

            todos.pop(removeval)


            write_todos(todos)



            message =f"Task: {removeddone.strip('\n')} was removed successfully"
            print(message)

        except IndexError:
            print("there is no item with that number")
            continue

    elif 'exit' in user_promp:
        break
    else:
        print('enter valid input')
