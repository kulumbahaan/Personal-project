from lib import User, Librarian, Patron


p1 = User('Kulumba','kulumbahaan11@gmail.com', '123456')

print(p1)
print(p1.login('kuluts@gmail.com', '123456'))

print(p1.logout())
print(p1.change_password('987654'))
# print(p1.login('kulumbahaan11@gmail.com', '987654')

#librarian
l1 = Librarian('Bob', 'bob@example.com', 'librarian123', None)

#patron
p2 = Patron('Alice', 'alice@example.com', 'password123', [])
print(p2.search_book('The Great Gatsby'))