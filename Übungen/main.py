import math
import random
import calc

res2 = calc.addition(5, 6)
print(res2)

res = math.factorial(5)
print(res)

res3 = math.pi
print(res3)

random_value = random.random()
print(random_value)

random_value2 = random.randint(1, 10)
print(random_value2)

lottery = ["John", "Mary", "Bob", "James", "Lisa"]
winner = random.choice(lottery)
print(winner)

winner = random.sample(lottery, 4)
print(winner)

random.shuffle(lottery)
print(lottery)
