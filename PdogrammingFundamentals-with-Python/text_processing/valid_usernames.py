def character_validator(text: str):
    for char in text:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True


def length_validator(text: str):
    if 2 < len(text) < 17:
        return True
    return False


usernames = input().split(', ')
is_valid = False

for username in usernames:
    if character_validator(username) and length_validator(username) is True:
        print(username)

