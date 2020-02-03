# Здесь буду пробовать всё новое, что узнаю
#
# ООП наследование
#
class SimpleUser:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def AgeName(self):
        return f" Имя:{self.name} Возраст:{str(self.age)}"


# наследование
class UserUpdate(SimpleUser):
    lastname: str
    origin: str
    _average: int

    def __init__(self, name, age, lastname, origin, average):
        super().__init__(name, age)
        self.lastname = lastname
        self.origin = origin
        self._average = average

    def NewAgeName(self):
        return f" Имя:{self.name} Возраст:{str(self.age)} Фамилия:{self.lastname} Город:{self.origin} Оценка:{str(self._average)}"


# _ инкапсуляция

gleb_new = UserUpdate("Gleb", 22, "Rengel", "Krsk", 4)
gleb_new.average = 5
print(gleb_new.NewAgeName(), gleb_new._average)

for x in range(1,5):
    for y in range (5,1,-1):
        print(x, y)

dict = {key: value for key, value in zip([1, 2, 3], ['a', 'b', 'c'])}
print (dict)
