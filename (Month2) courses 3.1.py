from abc import ABC, abstractmethod


# абтрактный класс
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("гав гав")

    def test(self):
        print("test test")

class Cat(Animal):
    def make_sound(self):
        print("мяяяяяу")
    def test(self):
        print("test test")

puppy = Dog()
puppy.make_sound()

# ощибка, потому что у Cat есть не все нужные методы
kitten = Cat()
kitten.make_sound()