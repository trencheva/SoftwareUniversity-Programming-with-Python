def softuni_students(*args, **kwargs):
    result = ''
    invalid_students = []
    students = {}

    for student_data in args:
        student_id, name = student_data
        if student_id in kwargs.keys():
            students[name] = kwargs[student_id]
        else:
            invalid_students.append(name)
    res = dict(sorted(students.items(), key=lambda x: x[0]))
    for name, course in res.items():

        result += f'*** A student with the username {name} has successfully finished the course {course}!\n'

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(el for el in sorted(invalid_students))}"
    return result


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
