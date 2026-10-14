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

    def remove_book(self, book):
        if book in self.library.books:

           self.library.books.remove(book)
           return f"Book removed successful"
        else:
            return f"Book not found"


