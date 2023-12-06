some_string = input()
numbers_list = []
non_numbers_list = []
final_string = ''
for char in some_string:
    if char.isdigit():
        numbers_list.append(char)
    else:
        non_numbers_list.append(char)

even_index_nums = [int(numbers_list[index]) for index in range(len(numbers_list)) if index % 2 == 0]
odd_index_nums = [int(numbers_list[index]) for index in range(len(numbers_list)) if index % 2 != 0]

for index in range(len(even_index_nums)):
    len_taken_string = even_index_nums[index]
    len_skipped_string = odd_index_nums[index]
    final_string += ''.join(non_numbers_list[:len_taken_string])

    non_numbers_list = non_numbers_list[len_taken_string:]
    non_numbers_list = non_numbers_list[len_skipped_string:]

print(final_string)