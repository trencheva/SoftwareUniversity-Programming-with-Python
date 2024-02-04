import os
import re


def change_filenames(dir_name):
    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)

        if os.path.isfile(file_path):

            new_name = filename.replace(string_to_replace, string_to_replace_with)
            new_file = "/".join(re.split(r"[\\/]", file_path)[:-1]) + "/" + new_name
            os.rename(file_path, new_file)


def extensions_collector(dir_name):
    for filename in os.listdir(dir_name):
        file_path = os.path.join(dir_name, filename)

        if os.path.isfile(file_path):
            extension = filename.split('.')[-1]
            extensions[extension] = extensions.get(extension, []) + [filename]

        elif os.path.isdir(file_path):
            extensions_collector(file_path)


directory = input('Enter a directory: ')
change_names = input('Do you want to change characters in filenames? "y/n": ')
if change_names == 'y':
    string_to_replace = input("Enter a string to replace: ")
    string_to_replace_with = input("Enter a string to replace with: ")
    change_filenames(directory)

extensions = {}
result = []


try:
    extensions_collector(directory)
except FileNotFoundError:
    print('Directory not found!')


sorted_extensions = sorted(extensions.items(), key=lambda x: x[0])


for name, filenames in sorted_extensions:
    result.append(f'.{name}')

    for file in sorted(filenames):
        result.append(f'- - - {file}')


with open('files/report.txt', 'w') as output_file:
    output_file.write('\n'.join(result))

