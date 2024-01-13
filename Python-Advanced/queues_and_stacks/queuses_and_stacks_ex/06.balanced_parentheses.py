from collections import deque

sequence_of_parentheses = deque([el for el in input()])

opening_paren = ['{', '[', '(']

sequence_is_balanced = False

paren_combination = {
    '{': '}',
    '[': ']',
    '(': ')'
}

stack_of_paren = []

if len(sequence_of_parentheses) % 2 == 0:
    for paren in sequence_of_parentheses:
        if paren in opening_paren:
            stack_of_paren.append(paren)
        else:
            if paren != paren_combination[stack_of_paren.pop()]:
                break
    else:
        sequence_is_balanced = True

if sequence_is_balanced:
    print('YES')
else:
    print('NO')

