def add_book(lst: list, book: str) -> list:
    if book not in lst:
        lst.insert(0, book)
    return lst


def take_book(lst: list, book: str) -> list:
    if book in lst:
        lst.remove(book)
    return lst


def swap_books(lst: list, book1: str, book2: str) -> list:
    if book1 in lst and book2 in lst:
        ind_book1 = lst.index(book1)
        ind_book2 = lst.index(book2)

        lst[ind_book2], lst[ind_book1] = lst[ind_book1], lst[ind_book2]
    return lst


def insert_book(lst: list, book: str) -> list:
    if book not in lst:
        lst.append(book)
    return lst


def check_book(lst: list, index: int) -> None:
    if 0 <= index < len(lst):
        print(lst[index])


book_shelf = input().split('&')

while True:
    com = input().split(' | ')
    if com[0] == 'Done':
        break

    if com[0] == 'Add Book':
        book_shelf = add_book(book_shelf, com[1])
    elif com[0] == 'Take Book':
        book_shelf = take_book(book_shelf, com[1])
    elif com[0] == 'Swap Books':
        book_shelf = swap_books(book_shelf, com[1], com[2])
    elif com[0] == 'Insert Book':
        book_shelf = insert_book(book_shelf, com[1])
    elif com[0] == 'Check Book':
        check_book(book_shelf, int(com[1]))

print(', '.join(book_shelf))
