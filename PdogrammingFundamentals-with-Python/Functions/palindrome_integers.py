def is_palindrome(number: str) -> bool:
    if number == number[::-1]:
        return True
    return False


numbers_as_string = input().split(', ')
for current_number in numbers_as_string:
    print(is_palindrome(current_number))
