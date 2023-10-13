def time_to_answer_the_questions(first: int, second: int, third: int, students: int):
    total_answers_per_hour = first + second + third
    hours = 1
    while students > 0:
        if hours % 4 != 0:
            students -= total_answers_per_hour
        hours += 1
    return hours - 1


first_employee_students_per_hour = int(input())
second_employee_students_per_hour = int(input())
third_employee_students_per_hour = int(input())
number_of_students = int(input())
time_needed = time_to_answer_the_questions(first_employee_students_per_hour, second_employee_students_per_hour, third_employee_students_per_hour, number_of_students)
print(f'Time needed: {time_needed}h.')