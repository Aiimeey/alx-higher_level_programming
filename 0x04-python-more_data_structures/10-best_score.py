#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    if a_dictionary is not None:
        b_score = max(a_dictionary)
        return b_score
