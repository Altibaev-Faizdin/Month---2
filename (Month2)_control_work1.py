class Animal:
    def __init__(self, name, age):
        self._name = name        # защищённые атрибуты
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    # --- property для age ---
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            print("Возраст не может быть отрицательным!")

    def make_sound(self):
        return "Some generic animal sound"


class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"


dog1 = Dog("Reks", 2)
cat1 = Cat("Karen", 1)

print(f"{dog1.name}, {dog1.age} лет: {dog1.make_sound()}")
print(f"{cat1.name}, {cat1.age} лет: {cat1.make_sound()}")

print("\nПосле изменений:")

dog1.name = "Pumba"
dog1.age = 3
print(f"{dog1.name}, {dog1.age} лет: {dog1.make_sound()}")

cat1.name = "Elza"
cat1.age = 4
print(f"{cat1.name}, {cat1.age} лет: {cat1.make_sound()}")

