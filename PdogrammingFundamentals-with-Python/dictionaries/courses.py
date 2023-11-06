final_information = {}
while True:
    command = input()
    if ':' not in command:
        break

    course_name, student_name = command.split(' : ')
    if course_name not in final_information.keys():
        final_information[course_name] = []
    final_information[course_name].append(student_name)

for course_name, students in final_information.items():
    registered_students = final_information[course_name]
    print(f'{course_name}: {len(registered_students)}')
    for student in registered_students:
        print(f'-- {student}')
