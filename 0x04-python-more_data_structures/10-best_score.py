#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    b_score = 0
    for key,value in a_dictionary.items():
        if b_score < value:
            b_score = value
            k = key
            return b_score
