import hashlib


def user_registration(username: str, password: str, data: dict, information: dict):
    if username in data:
        print('This username already exist.')
    else:
        data[username] = password
        name = input("Enter your name:")
        email = input("Enter your e-mail address:")
        phone_number = input("Enter your phone number:")
        city = input("Enter your home city:")
        information[username] = [name, email, phone_number, city]
        return data, information


def user_login(username: str, password: str, data: dict):
    if username in data and password == data[username]:
        return True
    else:
        if username not in data:
            flag = 'username'
        else:
            flag = 'password'
        print(f'Wrong {flag}!')


def user_profile(username: str, information: dict):
    print(f'{username} information:')
    print('\n'.join(information[username]))


def change_password(username, new_pass, data: dict):
    data[username] = new_pass
    return data


def hashing_password(plain_password):
    h = hashlib.new("SHA256")
    h.update(plain_password.encode())
    return h.hexdigest()


user_credentials = {}
user_profile_information = {}


while True:
    print('Menu')
    print('1.User Registration')
    print('2.User Login')
    print('3.View Profile')
    print('4.Change Password.')
    print('5.Exit')
    input_choice = input('Choose from the Menu and enter your choice:')
    if input_choice == '5':
        print('Goodbye!')
        break

    if input_choice != '1' and input_choice != '2' and input_choice != '3' and input_choice != '4':
        print('Invalid choice!')
        print()

    else:
        input_username = input("Enter your username:")
        input_password = input("Enter your password:")
        input_password = hashing_password(input_password)
        if input_choice == '1':
            user_registration(input_username, input_password, user_credentials, user_profile_information)

        elif input_choice == '2':
            user_login(input_username, input_password, user_credentials)

        elif input_choice == '3':
            if user_login(input_username, input_password, user_credentials) is True:
                user_profile(input_username, user_profile_information)

        elif input_choice == '4':
            if user_login(input_username, input_password, user_credentials) is True:
                new_password = input("enter new password:")
                hashing_password(new_password)
                change_password(input_username, new_password, user_credentials)
                print('You successfully changed your password!')

