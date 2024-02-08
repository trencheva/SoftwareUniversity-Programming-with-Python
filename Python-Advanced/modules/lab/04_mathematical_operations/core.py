def multiply(first_n, second_n):
    return first_n * second_n


def divide(first_n, second_n):
    return first_n / second_n


def add(first_n, second_n):
    return first_n + second_n


def subtract(first_n, second_n):
    return first_n - second_n


def power(first_n, second_n):
    return first_n ** second_n


sign_mapper = {
    '*': multiply,
    '/': divide,
    '-': subtract,
    '+': add,
    '^': power,
}


def execute_expression(exp):

    first_num_as_str, sign, second_num_as_str = exp.split()
    first_num = float(first_num_as_str)
    second_num = int(second_num_as_str)

    return sign_mapper[sign](first_num, second_num)

