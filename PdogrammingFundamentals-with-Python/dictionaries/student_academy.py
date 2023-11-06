students_dict = {}
n = int(input())
for current_student in range(n):
    name = input()
    grade = float(input())

    if name not in students_dict.keys():
        students_dict[name] = []
    students_dict[name].append(grade)

for name, grades in students_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
        