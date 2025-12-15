class Vehicles:
    def start(self):
        print('Vehicles starting')


class Car(Vehicles):
    def start(self):
        super().start()
        print('Car starting')

class ElectricCar(Vehicles):
    def start(self):
        super().start()



class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print('Tesla ready')

print(Tesla.mro())
tesla1 = Tesla()
tesla1.start()