class Car:
    #Инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.fined = False

def drive_to(self, destination):
        print(f'{self.color}, {destination}')

if __name__ == "__main__":
    car_mersedes = Car(color='red', model='Mercedes')
    car_bmw = Car(color='blue', model='BMW')
    print(car_mersedes)
    print(car_mersedes.color, car_mersedes.model)
    car_mersedes.color = 'green'
    print(car_mersedes.color, car_mersedes.model)
    print(car_bmw)
    print(car_bmw.color, car_bmw.model)
    car_bmw.fined = True
    print(car_bmw.fined)