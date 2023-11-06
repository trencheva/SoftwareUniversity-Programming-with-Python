final_information = {}
while True:
    command = input()
    if command == 'End':
        break

    company_name, employee_id = command.split(' -> ')

    if company_name not in final_information.keys():
        final_information[company_name] = []
    if employee_id not in final_information[company_name]:
        final_information[company_name].append(employee_id)

for company_name, employee_id in final_information.items():
    result = '\n-- '.join(employee_id)
    print(f"{company_name}\n-- {result}")