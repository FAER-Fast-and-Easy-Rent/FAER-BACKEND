import os


def write_to_tmp(file):
    file_path = f'temp/{file}'
    with open(file_path, 'wb+') as f:
        f.write(file.read())
    print(file.name, file_path)
    return file_path


def remove_from_tmp(file_path):
    os.remove(file_path)
    print(f'File removed :{file_path}')
