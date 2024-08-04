import os

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
    return "File not found."

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    return "Write operation successful."

def append_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
    return "Append operation successful."

def delete_file(file_name):
    os.remove(file_name)
    return "Delete operation successful."


file_operations = {
    'read': read_file,
    'write': write_file,
    'append': append_file,
    'delete': delete_file
}


def file_manager(file_name, operation, content=None):
    if operation in file_operations:
        if operation in ['write', 'append']:
            return file_operations[operation](file_name, content)
        else:
            return file_operations[operation](file_name)
    else:
        return "Invalid operation."



print(file_manager('example.txt', 'write', 'Hello, World!'))
print(file_manager('example.txt', 'read'))
print(file_manager('example.txt', 'append', ' This is an appended text.'))
print(file_manager('example.txt', 'read'))
print(file_manager('example.txt', 'delete'))
print(file_manager('example.txt', 'read'))
