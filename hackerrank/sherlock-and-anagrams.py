#!/bin/python3

import math
import os
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s: str):
    base = ord('a')
    characters = {}
    N = len(s)
    for char in s:
        if char not in characters:
            characters[char] = 0
        characters[char] += 1

    # this counts single character substrings
    return_val = 0
    for char in characters.keys():
        freq = characters[char]
        return_val += ((freq - 1) * freq) // 2

    # time for substrings
    sub_len = 2
    while sub_len != N:
        for i in range(0, N - sub_len):
            # a is the implicit first substring
            a_chars = [0] * 26
            # generating character counts for a
            for a_i in range(i, i + sub_len):
                char = s[a_i]
                index = ord(char) - base
                a_chars[index] += 1
            for j in range(i + 1, N - sub_len + 1):
                b_chars = [0] * 26
                for b_i in range(j, j + sub_len):
                    char = s[b_i]
                    index = ord(char) - base
                    b_chars[index] += 1
                if b_chars == a_chars:
                    return_val += 1
        sub_len += 1
    return return_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
