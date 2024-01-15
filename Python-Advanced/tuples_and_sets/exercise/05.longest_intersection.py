n = int(input())
intersections = []

for _ in range(n):
    first, second = input().split('-')

    first_start, first_end = first.split(',')
    second_start, second_end = second.split(',')

    first_set = {number for number in range(int(first_start), int(first_end) + 1)}
    second_set = {number for number in range(int(second_start), int(second_end) + 1)}

    intersection = first_set.intersection(second_set)
    intersections.append(intersection)

intersections.sort(key=len)
longest_intersection = [str(el) for el in intersections.pop()]

print(f'Longest intersection is [{", ".join(longest_intersection)}] with length {len(longest_intersection)}')