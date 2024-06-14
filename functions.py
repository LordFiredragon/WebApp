FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads the file of todos and returns list of todos. """
    with open(filepath, "r") as file_read:
        todos_read = file_read.readlines()
    return todos_read


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a todos item to the todos file. """
    with open(filepath, "w") as file_write:
        file_write.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
