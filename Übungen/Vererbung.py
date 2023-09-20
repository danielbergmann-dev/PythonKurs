class Animal:
    def __init__(self, name, age, color, fav_food):
        self.name = name
        self.age = age
        self.color = color
        self.fav_food = fav_food

    def sleep(self):
        print(" is sleeping")

    def move_fast(self):
        print(" is moving fast")


class Tiger(Animal):
    def move_fast(self):
        print(" Tigers are moving very fast")

class Dog(Animal):

   def bark(self):
       print(" is barking")

class Cat(Animal):
   def meow(self):
        print(" is meowing")

dog = Dog("Rex", 5, "brown", "meat")
dog.bark()
dog.sleep()
print(dog.name)

cat = Cat("Miau", 3, "black", "fish")
cat.meow()
cat.sleep()
print(cat.name)
print(cat.fav_food)
cat.move_fast()

tiger = Tiger("Tiger", 10, "yellow", "meat")
tiger.move_fast()