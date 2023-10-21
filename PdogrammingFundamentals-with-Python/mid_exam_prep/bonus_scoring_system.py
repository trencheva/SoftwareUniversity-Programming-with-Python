from math import ceil
number_of_students = int(input())
number_of_the_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attended_lectures = 0
for current_student in range(number_of_students):
    student_attendance = int(input())
    total_bonus = student_attendance / number_of_the_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attended_lectures = student_attendance
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attended_lectures} lectures.")
