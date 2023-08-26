class Car:
    def __init__(self):
        self.car_brand = None
        self.car_model = None
        self.car_year = None
        self.xPos = 5
        self.yPos = 5

    def drive(self,x,y):
        self.xPos = x
        self.yPos = y
        print("Car is driving to: ",self.xPos,self.yPos)

    def printPosition(self):
        print("X-Position: ",self.xPos)
        print("Y-Position: ",self.yPos)

car1 = Car()    # Instanz von Car
car1.car_brand = "BMW"
print(car1.car_brand)
car1.printPosition()
car1.drive(5,10)

