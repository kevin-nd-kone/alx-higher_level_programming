#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = 0
if(number < 0):
    num = number * (-1)
    last_digit = (num%10)*(-1)
else:
    last_digit = number%10
if(last_digit > 5):
    print(f"Last digit of {number} is {last_digit} and is greather than 5")
elif(last_digit == 0):
    print(f"Last digit of {number} is {last_digit} and is 0")
elif(last_digit < 6 and last_digit!=0):
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
