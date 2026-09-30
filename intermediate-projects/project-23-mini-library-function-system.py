books = {
    'Python Basics': {
        'Author': 'John Smith',
        'Available': True
    },
    'Web Development': {
        'Author': 'Jane Doe',
        'Available': True
    },
    'Networking Fundamentals': {
        'Author': 'Mike Lee',
        'Available': False
    }
}

def view_books(books):
    count = 0
    for book in books:
        count += 1
        if books[book]['Available']:
            print(f"{count}. {book} - {books[book]['Author']} - Available")
        else:
            print(f"{count}. {book} - {books[book]['Author']} - Borrowed")


def add_book(books):
    book_name = input('Enter book name: ').title()
    if book_name == '' or book_name in books:
        print('Invalid Book name!')
    else:
        author_name = input('Enter author name: ')
        if author_name == '':
            print('Invalid Author name!')
        else:
            books[book_name] = {
                'Author': author_name,
                'Available': True
            }
            print('Book successfully added!')

def search_book(books):
    book_name = input('Enter book name: ').title()
    if book_name in books:
        print('Book found!')
        if books[book_name]['Available']:
            print(
                f'Title: {book_name}'
                f"\nAuthor: {books[book_name]['Author']}"
                f"\nStatus: Availabe"
            )
        else:
            print(
                f'Title: {book_name}'
                f"\nAuthor: {books[book_name]['Author']}"
                f"\nStatus: Borrowed"
            )
    else:
        print('Book not found!')

def borrow_book(books):
    book_name = input('Enter book name: ').title()
    if book_name in books and books[book_name]['Available'] == True:
        print('Book borrowed successfully!')
        books[book_name]['Available'] = False
    else:
        print('Book Unavailable!')

def return_book(books):
    book_name = input('Enter book name: ').title()
    if book_name in books and books[book_name]['Available'] == False:
        print('Book successfully return!')
        books[book_name]['Available'] = True
    else:
        print('Invalid Action!')

def delete_book(books):
    book_name = input('Enter book name: ').title()
    if book_name in books:
        books.pop(book_name)
        print('Book successfully deleted!')
    else:
        print('Book not found!')
def show_available_book(books):
    count = 0 
    for book in books:
        if books[book]['Available'] == True:
            count += 1
    return count
    
while True:
    print('===== LIBRARY SYSTEM =====')
    print('1. View Book')
    print('2. Add Book')
    print('3. Search Book')
    print('4. Borrow Book')
    print('5. Return Book')
    print('6. Delete Book')
    print('7. Show Available Book')
    print('8. Exit')
    print('==========================')

    choice = input('Enter choice :')
    if choice == '8':
        print('Thank you for using Library System!')
        break

    elif choice == '1':
        view_books(books)

    elif choice == '2':
        add_book(books)

    elif choice == '3':
        search_book(books)

    elif choice == '4':
        borrow_book(books)

    elif choice == '5':
        return_book(books)

    elif choice == '6':
        delete_book(books)

    elif choice == '7':
        available = show_available_book(books)
        print(f"Available Book: {available}")

    else:
        print('Invalid choice!')