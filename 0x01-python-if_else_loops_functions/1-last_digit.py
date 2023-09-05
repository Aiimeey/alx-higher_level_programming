#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = 10
if number < 0:
    mod *= -1
last_num = number % mod
if last_num > 5:
    str = "Last digit of {} is {} and is greater than 5"
elif last_num == 0:
    str = "Last digit of {} is {} and is 0"
else:
    str = "Last digit of {} is {} and is less than 6 and not 0"
print(str.format(number, last_num))
