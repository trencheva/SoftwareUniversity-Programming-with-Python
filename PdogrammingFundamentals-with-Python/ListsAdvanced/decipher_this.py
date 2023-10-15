secret_massage = input().split()

deciphered_message = []
new_word = []
for word in secret_massage:
    new_word = [char for char in word]
    first_letter = ''.join([character for character in new_word if character.isdigit()])
    new_word[0:len(first_letter)] = chr(int(first_letter))
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    deciphered_message.append(''.join(new_word))
print(' '.join(deciphered_message))

