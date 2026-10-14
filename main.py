from lib import User


p1 = User('Kulumba','kulumbahaan11@gmail.com', '123456')

print(p1)
print(p1.login('kuluts@gmail.com', '123456'))

print(p1.logout())
print(p1.change_password('987654'))
# print(p1.login('kulumbahaan11@gmail.com', '987654'))
