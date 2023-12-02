message = input().split(' | ')
english_message = ''

for word in message:
    english_word = ''
    english_letter = ''
    for letter in word.split():
        if letter == '.-':
            english_letter = 'A'
        elif letter == '-...':
            english_letter = 'B'
        elif letter == '-.-.':
            english_letter = 'C'
        elif letter == '-..':
            english_letter = 'D'
        elif letter == '.':
            english_letter = 'E'
        elif letter == '..-.':
            english_letter = 'F'
        elif letter == '--.':
            english_letter = 'G'
        elif letter == '....':
            english_letter = 'H'
        elif letter == '..':
            english_letter = 'I'
        elif letter == '.---':
            english_letter = 'J'
        elif letter == '-.-':
            english_letter = 'K'
        elif letter == '.-..':
            english_letter = 'L'
        elif letter == '--':
            english_letter = 'M'
        elif letter == '-.':
            english_letter = 'N'
        elif letter == '---':
            english_letter = 'O'
        elif letter == '.--.':
            english_letter = 'P'
        elif letter == '--.-':
            english_letter = 'Q'
        elif letter == '.-.':
            english_letter = 'R'
        elif letter == '...':
            english_letter = 'S'
        elif letter == '-':
            english_letter = 'T'
        elif letter == '..-':
            english_letter = 'U'
        elif letter == '...-':
            english_letter = 'V'
        elif letter == '.--':
            english_letter = 'W'
        elif letter == '-..-':
            english_letter = 'X'
        elif letter == '-.--':
            english_letter = 'Y'
        elif letter == '--..':
            english_letter = 'Z'
        english_word += english_letter
    english_message += english_word + ' '

print(english_message)