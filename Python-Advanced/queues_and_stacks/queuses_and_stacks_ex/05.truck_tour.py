from collections import deque

n_petrol_pumps = int(input())
amount_of_petrol = 0
index = 0
data = deque()

for _ in range(n_petrol_pumps):
    data.append([int(token) for token in input().split()])

pumps_data_copy = data.copy()


while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    amount_of_petrol += petrol

    if amount_of_petrol >= distance:
        amount_of_petrol -= distance
    else:
        index += 1
        data.rotate(-1)
        pumps_data_copy = data.copy()
        amount_of_petrol = 0

print(index)