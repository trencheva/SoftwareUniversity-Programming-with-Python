with open('../numbers.txt') as file_with_nums:
    nums = file_with_nums.readlines()
    print(sum(int(el) for el in nums))