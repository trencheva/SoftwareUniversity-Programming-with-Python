def password_validator(characters: str):
    list_of_errors = []
    if not 6 <= len(characters) <= 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not characters.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digit_counter = 0
    for char in characters:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()

password_errors = password_validator(password)
if not password_errors:
    print('Password is valid')
else:
    print('\n'.join(password_errors))
