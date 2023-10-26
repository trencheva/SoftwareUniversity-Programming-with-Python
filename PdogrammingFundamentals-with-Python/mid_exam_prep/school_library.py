def add_book(list_of_books: list, book_name: str):
    if book_name not in list_of_books:
        list_of_books.insert(0, book_name)
    return list_of_books


def take_book(list_of_books: list, book_name: str):
    if book_name in list_of_books:
        list_of_books.remove(book_name)
    return list_of_books


def swap_books(list_of_books: list, first_book_name: str, second_book_name: str):
    if first_book_name in list_of_books and second_book_name in list_of_books:
        first_index = list_of_books.index(first_book_name)
        second_index = list_of_books.index(second_book_name)
        list_of_books[first_index], list_of_books[second_index] = list_of_books[second_index], list_of_books[first_index]
    return list_of_books


def insert_book(list_of_books: list, book_name: str):
    if book_name not in list_of_books:
        list_of_books.append(book_name)
    return list_of_books


def check_book(list_of_books: list, book_index: int):
    book_name = ''
    if 0 <= book_index < len(list_of_books):
        book_name = list_of_books[book_index]
    print(book_name)


books_shelf = input().split('&')
command = input()
while command != 'Done':
    command = command.split(' | ')
    action = command[0]
    name = command[1]
    if action == 'Add Book':
        add_book(books_shelf, name)
    elif action == 'Take Book':
        take_book(books_shelf, name)
    elif action == 'Swap Books':
        second_name = command[2]
        swap_books(books_shelf, name, second_name)
    elif action == 'Insert Book':
        insert_book(books_shelf, name)
    elif action == 'Check Book':
        index = int(name)
        check_book(books_shelf, index)
    command = input()

print(', '.join(books_shelf))