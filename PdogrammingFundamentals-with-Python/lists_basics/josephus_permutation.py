list_of_people = input().split(' ')
k = int(input())
executed_people = []
counter = 0

while len(list_of_people) != 0:
    for i in list_of_people:
        counter += 1
        if counter % k == 0:
            executed_people.append(i)
    for j in executed_people:
        if j in list_of_people:
            list_of_people.remove(j)
print('[' + ','.join(executed_people) + ']')

