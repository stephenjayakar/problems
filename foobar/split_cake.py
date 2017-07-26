# Python 2.7
from math import sqrt
def answer(s):
    length = len(s)
    factors = factor(length)
    for chunkSize in factors:
        string_list = split_string(s, chunkSize)
        if (all_equal(string_list)):
            return length//chunkSize
    return 1

# Checks if all the values in a list are equal to each other
def all_equal(l):
    length = len(l)
    for i in range(length-1):
        if (l[i] != l[i+1]):
            return False
    return True
        
# Splits a string into chunks of n length
def split_string(s, n):
    string_list = []
    for i in range(len(s) // n):
        index = i * n
        string_list.append(s[index:index+n])
    return string_list
        
# Returns int list of factors    
def factor(c):
    factors = []
    for i in range(2, 1 + int(sqrt(c))):
        if (c % i == 0):
            factors.append(i)
            value = c // i
            if (value <= c//2 and value != i):
                factors.append(value)
    factors.sort()
    return factors

def tests():
    string_1 = "abcabcabcabc"
    string_2 = "abccbaabccba"
    print answer(string_1)
    print answer(string_2)
