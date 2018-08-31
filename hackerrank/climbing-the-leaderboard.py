#!/bin/python3

import math
import os
import random
import re
import sys

"""
[100, 50, 40, 20, 10] length 5

value: 5
start = 0, end = 5
middle = (end - start / 2) + start = 2 (40)
if = return middle
if < query func(middle + 1, end)
if > query func(start, middle)

value: 5
start = 3, end = 5
middle = 4 (10)
query func(5, 5)

if start == end, return start;
"""                        

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores: list, alice: list) -> list:
    # generate list of unique scores
    unique_scores = []
    last_val = None
    for score in scores:
        if score != last_val:
            last_val = score
            unique_scores.append(score)

    rankings = [binary_search_index(unique_scores, a, 0, len(unique_scores)) + 1 for a in alice]
    return rankings
    

# this returns the index where the value would be inserted using binary-search
# we want the value + 1 for the place (since places start @1)
def binary_search_index(lst: list, value: int, start: int, end: int) -> int:
    if start == end:
        return start
    
    middle_index = ((end - start) // 2) + start
    middle_val = lst[middle_index]
    if value == middle_val:
        return middle_index
    if value < middle_val:
        return binary_search_index(lst, value, middle_index + 1, end)
    if value > middle_val:
        return binary_search_index(lst, value, start, middle_index)    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
