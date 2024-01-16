n = int(input())
longest_intersection = set()

for _ in range(n):
    first, second = input().split('-')

    first_start, first_end = first.split(',')
    second_start, second_end = second.split(',')

    first_set = {number for number in range(int(first_start), int(first_end) + 1)}
    second_set = {number for number in range(int(second_start), int(second_end) + 1)}

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection


print(f'Longest intersection is [{", ".join([str(x)for x in longest_intersection])}] with length {len(longest_intersection)}')