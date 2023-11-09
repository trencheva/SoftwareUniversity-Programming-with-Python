def add(some_schedule, title):
    if title not in some_schedule:
        some_schedule.append(title)
    return some_schedule


def insert(some_schedule, title, index):
    if title not in some_schedule:
        some_schedule.insert(index, title)
    return some_schedule


def remove(some_schedule, title):
    if title in some_schedule:
        title_index = some_schedule.index(title)
        if title_index + 1 in range(len(some_schedule)):
            if 'Exercise' in some_schedule[title_index + 1]:
                some_schedule.pop(title_index + 1)
        some_schedule.remove(title)
    return some_schedule


def swap(some_schedule, first_title, second_title):
    if first_title in some_schedule and second_title in some_schedule:
        first_title_index = some_schedule.index(first_title)
        second_title_index = some_schedule.index(second_title)
        first_has_exercise = False
        second_has_exercise = False
        if first_title_index + 1 in range(len(some_schedule)):
            first_has_exercise = 'Exercise' in some_schedule[first_title_index + 1]
        if second_title_index + 1 in range(len(some_schedule)):
            second_has_exercise = 'Exercise' in some_schedule[second_title_index + 1]
        some_schedule[first_title_index], some_schedule[second_title_index] = some_schedule[second_title_index], some_schedule[first_title_index]
        if first_has_exercise and second_has_exercise:
            some_schedule[first_title_index + 1], some_schedule[second_title_index+1] = some_schedule[second_title_index+1], some_schedule[first_title_index+1]
        elif not first_has_exercise and second_has_exercise:
            some_schedule.insert(first_title_index + 1, some_schedule.pop(second_title_index + 1))
        elif first_has_exercise and not second_has_exercise:
            some_schedule.insert(second_title_index + 1), some_schedule.pop(first_title_index + 1)
    return some_schedule


def exercise(some_schedule, title):
    if title in some_schedule and f'{title}-Exercise' not in some_schedule:
        lesson_index = some_schedule.index(title)
        some_schedule.insert(lesson_index + 1, f'{title}-Exercise')
    elif title not in some_schedule:
        some_schedule.append(title)
        some_schedule.append(f'{title}-Exercise')
    return some_schedule


schedule = input().split(', ')
command = input().split(':')
while len(command) > 1:
    lesson_title = command[1]
    if len(command) > 2:
        lesson_title_or_index = command[2]
    if command[0] == 'Add':
        schedule = add(schedule, lesson_title)
    elif command[0] == 'Insert':
        schedule = insert(schedule, lesson_title, int(lesson_title_or_index))
    elif command[0] == 'Remove':
        schedule = remove(schedule, lesson_title)
    elif command[0] == 'Swap':
        schedule = swap(schedule, lesson_title, lesson_title_or_index)
    elif command[0] == 'Exercise':
       schedule = exercise(schedule, lesson_title)
    command = input().split(':')


for index, lesson_name in enumerate(schedule):
    print(f'{index +1}.{lesson_name}')

