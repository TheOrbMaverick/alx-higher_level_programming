#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
	string = "positive"
elif number == 0:
	string = "zero"
else:
	string = "negetive"
print(f"{number} is {string}")
