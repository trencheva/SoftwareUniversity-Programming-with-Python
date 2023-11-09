n = int(input())
result = 0
for character in range(n):
    letter = input()
    result += ord(letter)
print(f"The sum equals: {result}.")
