from collections import deque

programmers_time = deque(int(x) for x in input().split())
tasks = [int(x) for x in input().split()]

ducks_count = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while programmers_time and tasks:
    current_time = programmers_time.popleft()
    current_task = tasks.pop()

    result = current_task * current_time

    if 0 <= result <= 60:
        ducks_count["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        ducks_count["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        ducks_count["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        ducks_count["Small Yellow Rubber Ducky"] += 1
    elif result > 240:
        tasks.append(current_task - 2)
        programmers_time.append(current_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

[print(f"{name}: {count}") for name, count in ducks_count.items()]




