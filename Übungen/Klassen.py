class Car:
    def __init__(self, car_brand, car_model, car_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_year = car_year
        self.xPos = 5
        self.yPos = 5

    def drive(self, x, y):
        self.xPos = x
        self.yPos = y
        print("Car is driving to: ", self.xPos, self.yPos)

    def printPosition(self):
        print("Car stand on: ", self.xPos, self.yPos)


car1 = Car("BMW", "A3", "2023")  # Instanz von Car
print(car1.car_brand)
print(car1.car_model)
print(car1.car_year)
car1.printPosition()
car1.drive(5, 10)
