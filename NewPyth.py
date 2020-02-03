# Здесь буду пробовать всё новое, что узнаю
#
# OOП основы
#
class Format:
    pass
name = "Ericson"
age = 24
print (f" Привет, меня зовут {name}, мой возраст {age}")

class SimpleUser:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def AgeName (self):
        return f" Имя:{self.name} Возраст:{str(self.age)}"

maxim = SimpleUser("Maxim",22)
gleb = SimpleUser("Gleb",21)

#maxim.name = "Дружок"
#gleb.age = 22

person = {'first_name': 'John', 'age': 53}
print (maxim.name, maxim.age)
print (gleb.name, gleb.age)
print (gleb.AgeName())
print (person)


def lineReceived(self, line: bytes):
    content = line.decode()

    if self.login is not None:
        content = f"Message from {self.login}: {content}"

        for user in self.factory.clients:
            if user is not self:
                user.sendLine(content.encode())
    else:
        if content.startswith("login:"):
            login = content.replace("login:", "")
            self.sendLine("Welcome!".encode())

        else:
            self.sendLine("Invalid login".encode())

