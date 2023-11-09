def data_types(data_type: str, data):
    if type_of_the_data == 'int':
        return int(data) * 2
    elif type_of_the_data == 'real':
        result = float(data) * 1.5
        return f'{result:.2f}'
    elif type_of_the_data == 'string':
        return f'${data}$'


type_of_the_data = input()
data_input = input()
print(data_types(type_of_the_data, data_input))
