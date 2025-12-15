class Animal:
    def move(self):
        print("двигается")

class Swimming(Animal):
    def move(self):
        super().move()
        print("плавает")

class Flying(Animal):
    def move(self):
        super().move()
        print("летает")

class Duck(Swimming, Flying):
    def move(self):
        super().move()
        print("летает и плавает")

# MRO - method resolution order
# порядок поиска методов
print(Duck.mro())
duck = Duck()
duck.move()