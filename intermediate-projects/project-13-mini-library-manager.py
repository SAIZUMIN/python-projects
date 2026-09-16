books = ['Python Basics', 'Web Development', 'Networking Fundamentals']
borrowed = [False, False, False]

while True:
    print('=====LIBRARY MANAGER=====')
    print('1. View Books')
    print('2. Add Books')
    print('3. Search Books')
    print('4. Borrow Books')
    print('5. Return Books')
    print('6. Exit')
    print('=========================')

    choice = input('Enter choice: ')
    if choice == '6':
        print('Thank You for using Mini Library Manager!')
        break

    elif choice == '1':
        print('=====BOOKS=====')

        for i in range(len(books)):
            if borrowed[i]:
                print(f'{i+1}. {books[i]} - Borrowed')
            else:
                print(f'{i+1}. {books[i]} - Available')
    
    elif choice == '2':
        book_name = input('Enter books name: ').title()
        if book_name != '':
            books.append(book_name)
            borrowed.append(False)
            print('Book successfully added!')
        else:
            print('Error. Book name is empty!')

    elif choice == '3':
        book_name = input('Enter book name: ').title()
        if book_name in books:
            position = books.index(book_name)
            if borrowed[position]:
                print(f'Book: {book_name} is Borrowed')
            else:
                print(f'Book: {book_name} is Available')
        else:
            print('Book not in the library!')

    elif choice == '4':
        book_name = input('Enter book name: ').title()
        if book_name in books:
            position = books.index(book_name)
            if borrowed[position] == False:
                borrowed[position] = True
                print('Book borrowed successfully!')
            else:
                print('Book is not available!')
        else:
            print('Book not in library!')

    elif choice == '5':
        book_name = input('Enter book name: ').title()
        if book_name in books:
            position = books.index(book_name)
            if borrowed[position] == True:
                borrowed[position] = False

                print('Book return successfully!')
            else:
                print('Book is already available!')
        else:
            print('Book not in library')
    
