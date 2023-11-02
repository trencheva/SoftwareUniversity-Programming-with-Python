corresponding_course = None
students = {}
list_of_students = []
while True:
    students_info = input()
    if ':' not in students_info:
        corresponding_course = students_info
        break

    list_of_students.append(students_info)

for student in list_of_students:
    name, id, course = student.split(":")
    if course.startswith(corresponding_course[0:3]):
        students[name] = int(id)

for k, v in students.items():
    print(f'{k} - {v}')




