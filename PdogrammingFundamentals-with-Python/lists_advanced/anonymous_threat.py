input_line = input().split()
command = input().split()
while command[0] != '3:1':
    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(input_line) - 1:
            end_index = len(input_line) - 1
        merged_elements = ''.join(input_line[start_index:end_index + 1])
        input_line[start_index:end_index + 1] = [merged_elements]
    elif command[0] == 'divide':
        index = int(command[1])
        partitions = int(command[2])
        element = input_line[index]
        divided_partition = []
        partition_length = len(element) // partitions
        for current_element_index in range(partitions):
            if current_element_index != partitions - 1:
                divided_partition.append(element[current_element_index * partition_length: (current_element_index + 1) * partition_length])
            else:
                divided_partition.append(element[current_element_index * partition_length:])
        input_line[index:index + 1] = divided_partition

    command = input().split()
print(" ".join(input_line))
