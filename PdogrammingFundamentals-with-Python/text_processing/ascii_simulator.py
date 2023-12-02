start_of_the_range = ord(input())
end_of_the_range = ord(input())

some_string = input()
final_sum = 0

for character in some_string:
    if start_of_the_range < ord(character) < end_of_the_range:
        final_sum += ord(character)

print(final_sum)
