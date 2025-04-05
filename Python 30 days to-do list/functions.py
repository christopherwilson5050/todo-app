def get_todos(filepath='todostore.txt'):
    with open(filepath, 'r') as file_funct:
        todos_funct = file_funct.readlines()

    return todos_funct

def write_todos(local_todos,filepath='todostore.txt'):
    with open(filepath, 'w') as file:
        file.writelines(local_todos)

if __name__ == '__main__':
    print('hello world')