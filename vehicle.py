class Vehicle:
    def __init__(self, newName):
        self.name = newName
        self.wheels = 0
        self.ingition = False
        self.passengers = []

    def num_wheels(self, wheels):
        self.wheels = wheels

    def ignition(self, key):
        self.ignition = key

    def add_passengers(self, passenger):
        self.passengers.append(passenger)

def main():
    myCar = Vehicle("Bronco")
    myCar.num_wheels(4)
    myCar.add_passengers("Madison")
    print(myCar.name, myCar.wheels, myCar.passengers)

if __name__ == '__main__':
    main()
