rows, cols = [int(el) for el in input().split(', ')]

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

max_sum_of_elements = float('-inf')
for row_index in range(rows-1):
    for col_index in range(cols-1):

        first_element = matrix[row_index][col_index]
        element_right = matrix[row_index][col_index+1]
        element_under = matrix[row_index+1][col_index]
        element_diagonal = matrix[row_index+1][col_index+1]
        sum_of_elements = first_element + element_right + element_diagonal + element_under

        if sum_of_elements > max_sum_of_elements:
            max_sum_of_elements = sum_of_elements

            sub_matrix = [[first_element, element_right], [element_under, element_diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum_of_elements)