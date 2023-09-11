#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = ()
    for i in range(2):
        a = tuple_a[i] if i < len(tuple_a) else 0
        b = tuple_b[i] if i < len(tuple_b) else 0
        sum += (a + b,)
    return sum
