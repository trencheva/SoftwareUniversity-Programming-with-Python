num = int(input())
pieces = {}
for _ in range(num):
    piece, composer, key = input().split('|')
    pieces[piece] = [composer, key]

while True:
    command = input().split('|')
    if command[0] == 'Stop':
        break

    action = command[0]
    piece = command[1]

    if action == 'Add':
        composer = command[2]
        key = command[3]
        if piece not in pieces.keys():
            pieces[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif action == 'Remove':
        if piece not in pieces.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")
    elif action == 'ChangeKey':
        new_key = command[2]
        if piece not in pieces.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")
