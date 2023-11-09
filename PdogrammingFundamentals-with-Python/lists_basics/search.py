n = int(input())
magic_word = input()
string_list = []
new_string_list = []

for i in range(n):
    string = input()
    string_list.append(string)

    if magic_word in string:
        new_string_list.append(string)

print(string_list)
print(new_string_list)