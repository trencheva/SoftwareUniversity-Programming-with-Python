expression = input()

index_paren = []

for index in range(len(expression)):
    if expression[index] == '(':
        index_paren.append(index)
    elif expression[index] == ')':
        start_index = index_paren.pop()
        end_index = index + 1
        print(expression[start_index:end_index])
