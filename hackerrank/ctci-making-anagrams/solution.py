from string import ascii_lowercase


LOWERCASE_START = 97

def number_needed(a, b):
    charsA = [0] * 26
    charsB = [0] * 26    
    for i in range(min(len(a), len(b))):
        charsA[char_to_index(a[i])] += 1
        charsB[char_to_index(b[i])] += 1
    # tailcase
    if len(a) > len(b):
        for i in range(len(b), len(a)):
            charsA[char_to_index(a[i])] += 1
    elif len(a) < len(b):
        for i in range(len(a), len(b)):
            charsB[char_to_index(b[i])] += 1
    # now, we find the difference of all the characters
    diff = 0
    for i in range(26):
        diff += abs(charsA[i] - charsB[i])
    return diff

def char_to_index(c):
    return (ord(c) - LOWERCASE_START)
    

a = input().strip()
b = input().strip()

print(number_needed(a, b))
