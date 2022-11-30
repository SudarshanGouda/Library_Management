class Library:

    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.landDict={}

    def display_book(self):
        print(f'List of book available in library{self.name}')
        for book in self.booklist:
            print(book)

    def lend_book(self,book,reader):
        if self.booklist.count(book)>0:
            if book is not self.landDict.keys():
                self.landDict.update({book:reader})
                print('you can collect your book')
            else:
                print (f'book is already with {self.landDict([book])}')
        else:
            print('Book is not in Library')

    def add_book(self,book):
        self.booklist.append(book)
        print('Book is added to list')

    def return_book(self,book):
        self.landDict.pop(book)