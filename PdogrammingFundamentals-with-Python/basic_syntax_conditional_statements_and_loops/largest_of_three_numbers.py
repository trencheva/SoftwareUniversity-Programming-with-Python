import sys

first_number = int(input())
second_number = int(input())
third_number = int(input())
largest_num = -sys.maxsize
if first_number > largest_num:
    largest_num = first_number
if second_number > largest_num:
    largest_num = second_number
if third_number > largest_num:
    largest_num = third_number
print(largest_num)