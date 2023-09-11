#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = ()

    tuple_len = max(len(tuple_a), len(tuple_b))

    for i in range(tuple_len):
        a = tuple_a[i] if i < len(tuple_a) else 0
        b = tuple_b[i] if i < len(tuple_b) else 0
        sum += (a + b,)
    return sum
