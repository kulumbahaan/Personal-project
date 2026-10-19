


class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPassword: {self.password}"

    def login(self, email, password):
        if self.email == email and self.password == password:
            return True
        else:
            return False

    def logout(self):
        self.email = None
        self.password = None
        return f"{self.name} has successfully logged out."

    def change_password(self, new_password):
        self.password = new_password
        return f'Password has been updated successfully.'

class Librarian(User):
    def __init__(self, name, email, password, library):
        super().__init__(name, email, password)

        self.library = library

    def add_book(self, book):
        self.library.books[book.title] = book
        return f"{book.title} has been added Successfully."

    def remove_book(self, title):
        if title in self.library.books:
            del self.library.books[title]
            return f"Book removed successfully."
        else:
            return f"Book not found"

    def issue_book(self, book_title, patron_email):
        if book_title in self.library.books:
            book = self.library.books[book_title]
            if book.is_available:
                book.is_available = False
                return f"{book_title} has been issued to {patron_email}."
            else:
                return f"{book_title} is currently not available."

    def return_book(self, book_title, patron_email):
        if book_title in self.library.books:
            book = self.library.books[book_title]
            if not book.is_available:
                book.is_available = True
                return f"{book_title} has been returned by {patron_email}."
            else:
                return f"{book_title} was not issued to {patron_email}."

class Patron(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.borrowed_books = []

    def search_book(self, keyword):
       matches = []

       for book in self.library.books.values():
           if (keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()):
               matches.append(book)
       return matches

    def borrow_book(self, book_title, librarian_email):
        if book_title in self.library.books:
            book = self.library.books[book_title]
            if book.is_available:
                book.is_available = False
                self.borrowed_books.append(book)
                return f"{book_title} has been borrowed successfully."
            else:
                return f"{book_title} is currently not available."



