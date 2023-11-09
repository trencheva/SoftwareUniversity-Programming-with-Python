number_of_lines = int(input())
last_bracket = ''
is_balanced = True
for current_line in range(number_of_lines):
    string = input()
    if string == "(" or string == ")":

        if last_bracket == '' and string == ')' or last_bracket == string:
            is_balanced = False

        last_bracket = string

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")