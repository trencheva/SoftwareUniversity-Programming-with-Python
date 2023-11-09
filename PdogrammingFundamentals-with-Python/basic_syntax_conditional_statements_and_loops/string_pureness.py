n = int(input())
for i in range(n):
    string_is_clean = True
    string = input()
    for j in string:
        if j == "," or j == "." or j == "_":
            string_is_clean = False
            break
    if string_is_clean:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")