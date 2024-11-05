class Book():

    available = True

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


    def borrow():
         available = False

    def return_book():
        available = True

    def is_available():
        return available 
    

class Person():

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def get_info(self):
        return f'Imię i nazwisko: {self.name} \n numer identyfikacyjny: {self.id_number}'
    

class Reader(Person):

    borrowed_books = []

    def __init__(self, name, id_number):
        super().__init__(name, id_number)
        
    def borrow_book(book: Book):
        if available == True:
            return borrowed_books.append(book)
        else:
            print("Książka jest niedostępna")

    def return_book(book: Book):
        return borrowed_books.pop(book)
    

class Librarian(Person):

    def __init__(self, name, id_number):
        super().__init__(name, id_number)

    
    def check_availability(book: Book):
        if available == True:
            return f'Książka {book} jest dostępna'
        else:
            return f'Książka {book} jest niedostępna'
        
    def register_book(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        return book1 = Book("W pustyni i w puszczy", "Henryk Sienkiewicz", "556897")
    


