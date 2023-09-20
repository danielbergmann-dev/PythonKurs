class Animal:
    def __init__(self, name, age, color, fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print(f"{self.name} is sleeping")

    def move_fast(self):
        print(f"{self.name} is moving fast")


class Tiger(Animal):
    def move_fast(self):
        print("Tigers are moving very fast")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")


class Owl(Animal):
    def __init__(self, name, age, color, fav_food, hunting_time):
        super().__init__(name, age, color, fav_food)
        self.hunting_time = hunting_time

    def sleep(self):
        super().sleep()
        print(f"{self.name} sleep during the day")
        print(self.age)


dog = Dog("Rex", 5, "brown", "meat")
dog.bark()
dog.sleep()
print(dog.name)

cat = Cat("Miau", 3, "black", "fish")

tiger = Tiger("Tiger", 10, "yellow", "meat")
tiger.move_fast()

owl = Owl("Owl", 2, "white", "mice", "night")
owl.sleep()
print(owl.name)
print(owl.hunting_time)
