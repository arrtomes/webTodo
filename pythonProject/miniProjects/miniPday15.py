""" Your task is to create a program that generates a random whole number. Here is how the program should behave
As you can see, the program first asks the user to enter a whole number. Then, once the user enters a number,
the program asks the user again to enter another number.
Then, the program returns a random number that falls between the two whole numbers."""

import random

num1 = int(input("Enter the lower bound number: "))
num2 = int(input("Enter the lower bound number: "))

print(random.randint(num1, num2))