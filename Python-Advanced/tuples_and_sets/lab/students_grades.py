n = int(input())
students_data = {}

for _ in range(n):
    name, grade = input().split()

    if name not in students_data.keys():
        students_data[name] = []
    students_data[name].append(float(grade))

for name, grades in students_data.items():
    formatted_grades = [str(f"{grade:.2f}") for grade in grades]
    avg_grade = sum(grades) / len(grades)
    print(f"{name} -> {' '.join(formatted_grades)} (avg: {avg_grade:.2f})")