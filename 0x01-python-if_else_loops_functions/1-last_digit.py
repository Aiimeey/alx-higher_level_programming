#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = number % 10
if number < 0:
    last_num *= -1
if last_num > 5:
    str = "Last digit of {} is {} and is greater than 5"
elif last_num == 0:
    str = "Last digit of {} is {} and is 0"
else:
    str = "Last digit of {} is {} and is less than 6 and not 0"
print(str.format(number, last_num))
