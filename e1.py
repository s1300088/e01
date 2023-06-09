print("What is your name?")
name = input()
print("Hello, "+ name + "!")

import random

a = random.randint(1, 6)
b = random.randint(1, 6)

print("Rolling dice...")

print("Die 1: ", a)
print("Die 2: ", b)

print("Total value: ", (a+b))
if a + b >= 7:
    print(name, "win!")
else:
    print(name, "lose!")