class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car driving")

class ElectricCar(Car):
    def charge(self):
        print("ElectricCar charging")

b = input("Enter brand: ")
ec = ElectricCar()
print("Brand:", b)
ec.start()
ec.drive()
ec.charge()
