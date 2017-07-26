import math
import itertools
# Returns a list of tuples that are all possible combinations
def subsets(lst, length):
    return list(itertools.combinations(lst, length))

# N is the length of S (the set), k is the divisor 
def main(n, k, S):
    for i in reversed(range(2, n + 1)):
        sets = subsets(S, i)
        for elem in sets:
            two_tuples = subsets(elem, 2)
            if divisible_by_k(two_tuples, k):
                return i
            
# Should cache these values, as they are repeated
def divisible_by_k(ttp, k):
    for tp in ttp:
        if sum(tp) % k == 0:
            return False
    return True
    
n, k = input().strip().split(' ')
n = int(n)
k = int(k)
S = input().strip().split(' ')
S = list(map(int, S))
print(main(n, k, S))
