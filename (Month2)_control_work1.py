class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age



    def get_name(self):
        return self.__name


    def get_age(self):
        return self.__age


    def set_name(self, new_name):
        self.__name = new_name


    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Возраст не может быть отрицательным!")


    def make_sound(self):
        return "Some generic animal sound: "

class Dog(Animal):
    def make_sound(self):
        return "woof woof"


class Cat(Animal):
    def make_sound(self):
        return "meow meow"


dog1 = Dog("Reks", 2)
cat1 = Cat("Karen", 1)


print(dog1.get_name(), dog1.get_age(), "лет", ":", dog1.make_sound())
print(cat1.get_name(), cat1.get_age(), "лет", ":", cat1.make_sound())




print('\nПосле изменений: ')
dog1.set_name("Pumba")
dog1.set_age(3)
print(dog1.get_name(), dog1.get_age(), "лет", ":", dog1.make_sound())

cat1.set_name('Elza')
cat1.set_age(4)
print(cat1.get_name(), cat1.get_age(), "лет", ":", cat1.make_sound())

