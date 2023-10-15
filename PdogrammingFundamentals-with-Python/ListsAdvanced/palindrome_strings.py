words = input().split()
palindrome = input()

found_palindromes = [word for word in words if word == word[::-1]]
count_palindrome = words.count(palindrome)

print(found_palindromes)
print(f'Found palindrome {count_palindrome} times')