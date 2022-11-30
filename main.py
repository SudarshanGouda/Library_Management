
if __name__=='__main__':

    from Lib import Library
    from Data import Books

    Books_in_lib=Books
    my_lib=Library(Books_in_lib,'sudarshan')

    Library_closed=False

    while not Library_closed:

        choice_of_user=input('Please pick your choice\n'
                                 'D. Display Book \n'
                                 'L. Lend a book \n'
                                 'A. Add a book \n'
                                 'R. Return Book \n'
                                 'Q Quit').lower()

        if choice_of_user=='q':
            print(' Thank you for the visit')
            exit()

        else:
            try:
                if choice_of_user == 'd':
                    my_lib.display_book()

                elif choice_of_user == 'l':
                    book = input("Enter the name of the book you want to lend:")
                    user = input("Enter your name")
                    my_lib.lend_book(book,user)

                elif choice_of_user == 'a':
                    book = input("Enter the name of the book you want to add:")
                    my_lib.add_book(book)

                else:
                    book = input("Enter the name of the book you want to return:")
                    my_lib.return_book(book)

            except Exception as e:
                print(e)
                print('Choise is not right')

            next_choise=input('Want to continue Y or N').lower()

            if next_choise=='y':
                continue
            else:
                exit()


