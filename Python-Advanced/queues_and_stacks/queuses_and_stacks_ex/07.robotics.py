from collections import deque
from datetime import datetime, timedelta

robots_data = {}
for r in input().split(';'):
    name, time_needed = r.split('-')
    robots_data[name] = [int(time_needed), 0]

products = deque()

starting_time = datetime.strptime(input(), "%H:%M:%S")

product = input()
while product != 'End':
    products.append(product)
    product = input()

while products:
    starting_time += timedelta(0, 1)
    product = products.popleft()

    free_robots = []

    for name, value in robots_data.items():
        if value[1] != 0:
            robots_data[name][1] -= 1

        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots_data[robot_name][1] = data[0]

    print(f"{robot_name} - {product} [{starting_time.strftime('%H:%M:%S')}]")


